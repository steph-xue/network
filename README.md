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
![Pagination](/network/static/network/images/pagination.png?raw=true "Pagination")
<br></br>   
   
**2. Viewing a specific user's profile**  
   - The
&nbsp;

![Profile](/network/static/network/images/profile.png?raw=true "Profile")
<br></br>


## Features where login authentication is needed:
**1. Creating a new post**
&nbsp;

![Create Post](/network/static/network/images/create.png?raw=true "Create Post")
<br></br>

**2. Editing a post**
&nbsp;

![Edit Button](/network/static/network/images/edit_button.png?raw=true "Edit Button")
<br></br>
![Edit Post](/network/static/network/images/edit.png?raw=true "Edit Post")
<br></br>

**3. Following/Unfollowing a user**
&nbsp;

![Follow](/network/static/network/images/follow.png?raw=true "Follow")
<br></br>
![Unfollow](/network/static/network/images/unfollow.png?raw=true "Unfollow")
<br></br>

**4. Liking/Removing a like from a post**
&nbsp;

![Like](/network/static/network/images/like.png?raw=true "Like")
<br></br>
![Remove like](/network/static/network/images/remove_like.png?raw=true "Remove Like")
<br></br>

**5. Disliking/Removing a dislike from a post**
&nbsp;

![Dislike](/network/static/network/images/dislike.png?raw=true "Dislike")
<br></br>
![Remove dislike](/network/static/network/images/remove_dislike.png?raw=true "Remove Dislike")
<br></br>

**6. Viewing following posts page**
&nbsp;

![Following Posts](/network/static/network/images/following.png?raw=true "Following Posts")
<br></br>


## Specifications and How to Run
- The email project was created using Django, a Python-based web framework, for the backend and JavaScript for the front end to create a mix of possible user interactions
- The web application can be run in the terminal using 'python3 manage.py runserver'
