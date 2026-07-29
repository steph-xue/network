from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import json

from .models import User, Post, Follow, Like, Dislike


# Directs the user to the homepage with all posts
def index(request):

    # Gets all posts ordered in reverse chronological order
    all_posts = Post.objects.all().order_by("id").reverse()

    # Gets all Like objects
    all_likes = Like.objects.all()

    # Creates a list of all the post IDs the current user has liked
    your_liked_post_ids = []
    try:
        for like in all_likes:
            if like.user.id == request.user.id:
                your_liked_post_ids.append(like.post.id)
    except:
        your_liked_post_ids = []

    # Gets all Dislike objects
    all_dislikes = Dislike.objects.all()

    # Creates a list of all the post IDs the current user has disliked
    your_disliked_post_ids = []
    try:
        for dislike in all_dislikes:
            if dislike.user.id == request.user.id:
                your_disliked_post_ids.append(dislike.post.id)
    except:
        your_disliked_post_ids = []

    # Pagination - determines which page to show and allows a maximum of 10 posts per page
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)

    # Directs the user to the homepage with all posts ordered in reverse chronological order
    return render(request, "network/index.html", {
        "page_posts": page_posts,
        "your_liked_post_ids": your_liked_post_ids,
        "your_disliked_post_ids": your_disliked_post_ids
    })


# Logs the user in
def login_view(request):

    # POST - Allows the user to submit login information
    if request.method == "POST":

        # Attempts to sign the user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Checks if authentication was successful and redirects the user to the homepage
        # Returns an error message if the username and/or password is invalid
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })

    # GET - Directs the user to the login page
    else:
        return render(request, "network/login.html")


# Logs the user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Allows the user to register for a new account
def register(request):

    # POST - Allows the user to submit information to register for a new account
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensures the password matches the confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempts to create a new user and redirects the user to the homepage
        # Returns an error message if the username is already taken
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    # GET - Directs the user to the register page
    else:
        return render(request, "network/register.html")


# Allows the user to create a new post
@login_required
def create(request):

    # POST - Allows the user to submit new post information
    if request.method == "POST":

        # Gets the content and the user who posted it
        current_user = request.user
        content = request.POST["content"]

        # Checks to make sure the content field is not empty
        if content == "":
            return render(request, "network/create.html", {
                "message": "Content field cannot be empty."
            })

        # Creates a new post and saves it in the database
        post = Post(
            content = content,
            user = current_user
        )
        post.save()

        # Redirects the user to the homepage with all posts
        return HttpResponseRedirect(reverse("index"))

    # GET - Directs the user to the create new post page
    else:
        return render(request, "network/create.html")


# Directs the user to a specific user's profile
def profile(request, user_id):

    # Gets all posts of the specific user ordered in reverse chronological order
    profile_user = User.objects.get(pk=user_id)
    user_posts = Post.objects.filter(user=profile_user).order_by("id").reverse()

    # Pagination - determines which page to show and allows a maximum of 10 posts per page
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)

    # Gets the specific user's followers and the users they are following
    followers = Follow.objects.filter(user_following=profile_user)
    following = Follow.objects.filter(user_follower=profile_user)

    # Determines if the current user is following the profile's user
    try:
        if len(followers.filter(user_follower=request.user)) != 0:
            is_following = True
        else:
            is_following = False
    except:
        is_following = False

    # Directs the user to the specific user's profile with all posts ordered in reverse chronological order
    return render(request, "network/profile.html", {
        "page_posts": page_posts,
        "profile_user": profile_user,
        "followers": followers,
        "following": following,
        "is_following": is_following
    })


# Allows the user to follow the profile
@login_required
def follow(request):

    # Gets the current user and the profile's user
    current_user = request.user
    profile_user_id = int(request.POST["follow"])
    profile_user = User.objects.get(pk=profile_user_id)

    # Creates and saves a follow object where the current user follows the profile's user
    follow = Follow(
        user_follower=current_user,
        user_following=profile_user
    )
    follow.save()

    # Redirects the user to the same profile
    user_id = profile_user.id
    return HttpResponseRedirect(reverse("profile", kwargs={'user_id': user_id}))


# Allows the user to unfollow the profile
@login_required
def unfollow(request):

    # Gets the current user and the profile's user
    current_user = request.user
    profile_user_id = int(request.POST["unfollow"])
    profile_user = User.objects.get(pk=profile_user_id)

    # Deletes the follow object so that the current user unfollows the profile's user
    follow = Follow.objects.get(user_follower=current_user, user_following=profile_user)
    follow.delete()

    # Redirects the user to the same profile
    user_id = profile_user.id
    return HttpResponseRedirect(reverse("profile", kwargs={'user_id': user_id}))


# Directs the user to the following page to view posts from only the users they follow
@login_required
def following(request):

    # Gets all Follow objects where the user is a follower of another user
    following = Follow.objects.filter(user_follower=request.user)

    # Gets all posts ordered in reverse chronological order
    all_posts = Post.objects.all().order_by("id").reverse()

    # Creates an empty list to collect posts from followed users
    following_posts = []

    # Checks if the post's user is someone the current user follows, and adds it to the following posts list
    for post in all_posts:
        for follow in following:
            if follow.user_following == post.user:
                following_posts.append(post)

    # Pagination - determines which page to show and allows a maximum of 10 posts per page
    paginator = Paginator(following_posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)

    # Directs the user to the following page with posts ordered in reverse chronological order
    return render(request, "network/following.html", {
        "page_posts": page_posts
    })


# Allows the user to edit a post
@login_required
def edit(request, post_id):

    # POST - Allows the user to edit and save the edits to the database
    if request.method == "POST":

        # Gets the JSON data posted to the backend
        data = json.loads(request.body)

        # Gets the post to edit and saves the edits to the database
        post = Post.objects.get(pk=post_id)
        post.content = data["content"]
        post.save()

        # Returns a JSON response telling the user if the edit was successful
        return JsonResponse({"message": "Edit saved successfully", "data": data["content"]})


# Allows the user to like a post
@login_required
def add_like(request, post_id):

    # Gets the current user and the post they liked
    current_user = request.user
    post = Post.objects.get(pk=post_id)

    # Creates and saves a like object for the user and the post they liked
    new_like = Like(
        post=post,
        user=current_user
    )
    new_like.save()

    # Returns a JSON response telling the user if adding the like was successful
    return JsonResponse({"message": "Like added successfully"})


# Allows the user to remove a like from a post
@login_required
def remove_like(request, post_id):

    # Gets the current user and the post to remove the like from
    current_user = request.user
    post = Post.objects.get(pk=post_id)

    # Deletes the like object for the user and the post they previously liked
    like = Like.objects.get(post=post, user=current_user)
    like.delete()

    # Returns a JSON response telling the user if removing the like was successful
    return JsonResponse({"message": "Like removed successfully"})


# Allows the user to retrieve their own like status of a post
@login_required
def like_status(request, post_id):

    # Gets the current user and the post to retrieve their like status from
    current_user = request.user
    post = Post.objects.get(pk=post_id)

    # Determines if the user has liked the post
    liked = False
    try:
        like = Like.objects.get(post=post, user=current_user)
        if like is not None:
            liked = True
        else:
            liked = False
    except:
        liked = False

    count = 0

    # Returns a JSON response with the user's like status of the post
    return JsonResponse({"liked": liked})


# Allows the user to retrieve the total number of likes of a post
@login_required
def like_count(request, post_id):

    # Gets the post to retrieve the total number of likes from
    post = Post.objects.get(pk=post_id)

    # Gets all the like objects of the post
    likes = Like.objects.filter(post=post)

    # Determines how many likes the post has
    count = len(likes)

    # Returns a JSON response with the total number of likes of the post
    return JsonResponse({"count": count})


# Allows the user to dislike a post
@login_required
def add_dislike(request, post_id):

    # Gets the current user and the post they disliked
    current_user = request.user
    post = Post.objects.get(pk=post_id)

    # Creates and saves a dislike object for the user and the post they disliked
    new_dislike = Dislike(
        post=post,
        user=current_user
    )
    new_dislike.save()

    # Returns a JSON response telling the user if adding the dislike was successful
    return JsonResponse({"message": "Dislike added successfully"})


# Allows the user to remove a dislike from a post
@login_required
def remove_dislike(request, post_id):

    # Gets the current user and the post to remove the dislike from
    current_user = request.user
    post = Post.objects.get(pk=post_id)

    # Deletes the dislike object for the user and the post they previously disliked
    dislike = Dislike.objects.get(post=post, user=current_user)
    dislike.delete()

    # Returns a JSON response telling the user if removing the dislike was successful
    return JsonResponse({"message": "Dislike removed successfully"})


# Allows the user to retrieve their own dislike status of a post
@login_required
def dislike_status(request, post_id):

    # Gets the current user and the post to retrieve their dislike status from
    current_user = request.user
    post = Post.objects.get(pk=post_id)

    # Determines if the user has disliked the post
    disliked = False
    try:
        dislike = Dislike.objects.get(post=post, user=current_user)
        if dislike is not None:
            disliked = True
        else:
            disliked = False
    except:
        disliked = False

    # Returns a JSON response with the user's dislike status of the post
    return JsonResponse({"disliked": disliked})


# Allows the user to retrieve the total number of dislikes of a post
@login_required
def dislike_count(request, post_id):

    # Gets the post to retrieve the total number of dislikes from
    post = Post.objects.get(pk=post_id)

    # Gets all the dislike objects of the post
    dislikes = Dislike.objects.filter(post=post)

    # Determines how many dislikes the post has
    count = len(dislikes)

    # Returns a JSON response with the total number of dislikes of the post
    return JsonResponse({"count": count})
