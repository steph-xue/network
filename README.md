# Network Project
The network project allows the user to view, create, like, and dislike posts, as well as follow other users in a social media based networking web application.
<br></br>

## Network App
**Login**
- Allows the user to login to their account
&nbsp;

![Login](/network/static/network/images/login.png?raw=true "Login")
<br></br>

**Register for a New Account**
- Allows the user to register for a new account
&nbsp;

![Register](/network/static/network/images/register.png?raw=true "Register")
<br></br>

## Features where login authentication is not needed:
**1. Viewing all posts page (homepage)**  
   - The user can view a list of all posts (sorted in reverse chronological order)
   - This can be accessed via the 'Network' logo or 'All Posts' tab
   - Each post displays the following:
     - User who made the post (with a hyperlink to their profile)
     - Post content
     - Date and time post was made
     - Number of likes and dislikes
     - **Note**: Functions to edit, like, remove a like, dislike, and remove a dislike are only avaliable to users with login authentication
&nbsp;

![All Posts](/network/static/network/images/all_posts.png?raw=true "All Posts")
<br></br>   

**Pagination Feature**
![Pagination](/network/static/network/images/pagination.png?raw=true "Pagination")
All functions that show posts on the web application uses pagination, which separates the posts into separate pages with a maximum of 10 posts per page. The user can use the previous and next buttons, as well as the page numbers, to access different pages of posts.
<br></br>   
   
**2. Viewing a specific user's profile**  
   - You can access a specific user's profile by clicking on the user's username hyperlink on a post
   - Your own profile can be accessed by clicking on your username tab in the navigation bar
   - Each profile displays the following:
      - The user's username
      - The number of people who follow the user and the number of people who the user follows
      - All of the user's posts (sorted in reverse chronological order)
      - **Note**: Functions to follow and unfollow a user on their profile are only avaliable to users with login authentication
&nbsp;

![Profile](/network/static/network/images/profile.png?raw=true "Profile")
<br></br>


## Features where login authentication is needed:
**1. Creating a new post**
   - Can be accessed via the 'Create Post' tab
   - Users can create a new post by providing the post's contents
   - The new post will specify the user as the creator of the post, and will display the date and time the post was made
&nbsp;

![Create Post](/network/static/network/images/create.png?raw=true "Create Post")
<br></br>

**2. Editing a post**
   - Users can edit a post they previously made
   - This can be done by clicking on the edit button displayed underneath their own post
   - A pop up modal will allow the user to make changes to the post content and save the changes
&nbsp;

![Edit Button](/network/static/network/images/edit_button.png?raw=true "Edit Button")
<br></br>
![Edit Post](/network/static/network/images/edit.png?raw=true "Edit Post")
<br></br>

**3. Following/Unfollowing a user**
   - Users can follow and unfollow other users
   - This can be done by clicking on the follow or unfollow button located on a specific user's profile page
&nbsp;

![Follow](/network/static/network/images/follow.png?raw=true "Follow")
<br></br>
![Unfollow](/network/static/network/images/unfollow.png?raw=true "Unfollow")
<br></br>

**4. Liking/Removing a like from a post**
   - Users can like or remove a like from a specific post
   - This can be done by clicking on the like or remove like button located at the bottom of a user's posts
&nbsp;

![Like](/network/static/network/images/like.png?raw=true "Like")
<br></br>
![Remove like](/network/static/network/images/remove_like.png?raw=true "Remove Like")
<br></br>

**5. Disliking/Removing a dislike from a post**
   - Users can dislike or remove a dislike from a specific post
   - This can be done by clicking on the dislike or remove dislike button located at the bottom of a user's posts
&nbsp;

![Dislike](/network/static/network/images/dislike.png?raw=true "Dislike")
<br></br>
![Remove dislike](/network/static/network/images/remove_dislike.png?raw=true "Remove Dislike")
<br></br>

**6. Viewing following posts page**
   - The user can view a list of posts only from users who they currently follow (sorted in reverse chronological order)
   - This can be accessed via the 'Following' tab
&nbsp;

![Following Posts](/network/static/network/images/following.png?raw=true "Following Posts")
<br></br>

## Languages & Frameworks
- The email project was created using Django, a Python-based web framework, for the backend
- JavaScript was utilized for the front end to create a mix of possible user interactions

## How to Run
- Install the latest version of python
- Install Django by typing in the command line 'pip3 install Django'
- The web application can be run on your local server by typing in the command line 'python3 manage.py runserver'
