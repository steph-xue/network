<h1 align="center">
  Network
</h1>

<h4 align="center">
  A full-stack social networking web application where users can create posts, edit posts, <br>
  like/dislike posts made by others, and follow other users to build a personalized feed.
</h4>

<p align="center">
  <img src="docs/screenshots/all_posts.png?raw=true" alt="All Posts" width="500">
</p>

<br>

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [Getting Started](#getting-started)
  
<br>

## Overview

This project recreates the core experience of a social media platform, allowing users to create and edit posts, like or dislike posts made by others, follow other users, and build a personalized feed based on the accounts they follow. The frontend is built with JavaScript, HTML, CSS, and Bootstrap, and handles actions such as liking, disliking, and editing posts without reloading the page, giving those interactions a fast, responsive feel. The backend is built with Django and Python, and manages user accounts, posts, follower relationships, likes, and dislikes, storing all of it in a SQLite database. Posts are paginated across every view that lists them, including the homepage, individual profiles, and each user’s personalized following feed, keeping the interface organized as the amount of content grows.

<br>

## Features

### Authentication
Users can log in with an existing account or register for a new one. Once logged in, users gain access to posting, liking, disliking, following, and editing their own posts, while all posts remain visible to logged out visitors.

<p align="center"><b>Login</b></p>
<p align="center"><img src="docs/screenshots/login.png?raw=true" alt="Login" width="700"></p>

<p align="center"><b>Register</b></p>
<p align="center"><img src="docs/screenshots/register.png?raw=true" alt="Register" width="700"></p>

<br>

### All Posts
The homepage displays every post on the platform in reverse chronological order. Each post shows the author, with a link to their profile, the post content, the date and time it was made, and its current number of likes and dislikes, giving users a quick overview of activity across the whole platform.

<p align="center"><img src="docs/screenshots/all_posts.png?raw=true" alt="All Posts" width="700"></p>

<br>

### Pagination
Every page that lists posts, including the homepage, profile pages, and the following feed, is paginated to a maximum of ten posts per page. Users can move between pages using the previous and next buttons or by selecting a page number directly.

<p align="center"><img src="docs/screenshots/pagination.png?raw=true" alt="Pagination" width="700"></p>

<br>

### Profile
Each user has a profile page showing their username, their follower and following counts, and all of their posts in reverse chronological order. A user's own profile is accessible from the navigation bar, and any other user's profile can be reached by clicking their username on a post.

<p align="center"><img src="docs/screenshots/profile.png?raw=true" alt="Profile" width="700"></p>

<br>

### Create Post
Logged in users can create a new post by entering its content. The post is saved with the current user as the author along with the date and time it was made, and appears immediately at the top of the homepage.

<p align="center"><img src="docs/screenshots/create.png?raw=true" alt="Create Post" width="700"></p>

<br>

### Edit Post
Users can edit the content of their own posts, but not posts made by other users. Clicking "Edit" on a post opens a pop up form prefilled with its current content, and clicking "Save Changes" sends the update straight to the backend, so the post refreshes in place without reloading the page.

<p align="center"><b>Edit Button</b></p>
<p align="center"><img src="docs/screenshots/edit_button.png?raw=true" alt="Edit Button" width="700"></p>

<p align="center"><b>Edit Form</b></p>
<p align="center"><img src="docs/screenshots/edit.png?raw=true" alt="Edit Post" width="700"></p>

<br>

### Follow and Unfollow
Users can follow or unfollow other users directly from their profile page by clicking "Follow" or "Unfollow," though this option does not appear on a user's own profile. Following a user adds their posts to the follower's personalized feed, and the button updates immediately to reflect the change without reloading the page.

<p align="center"><b>Follow</b></p>
<p align="center"><img src="docs/screenshots/follow.png?raw=true" alt="Follow" width="700"></p>

<p align="center"><b>Unfollow</b></p>
<p align="center"><img src="docs/screenshots/unfollow.png?raw=true" alt="Unfollow" width="700"></p>

<br>

### Like and Dislike
Users can like or dislike any post independently, and remove either reaction at any time. Clicking "Like" or "Dislike" registers the reaction and the button switches to "Remove Like" or "Remove Dislike," and each post's like and dislike counts update instantly whenever a reaction is added or removed.

<p align="center"><b>Like</b></p>
<p align="center"><img src="docs/screenshots/like.png?raw=true" alt="Like" width="700"></p>

<p align="center"><b>Remove Like</b></p>
<p align="center"><img src="docs/screenshots/remove_like.png?raw=true" alt="Remove Like" width="700"></p>

<p align="center"><b>Dislike</b></p>
<p align="center"><img src="docs/screenshots/dislike.png?raw=true" alt="Dislike" width="700"></p>

<p align="center"><b>Remove Dislike</b></p>
<p align="center"><img src="docs/screenshots/remove_dislike.png?raw=true" alt="Remove Dislike" width="700"></p>

<br>

### Following Feed
Logged in users can view a feed containing posts only from the users they follow, sorted in reverse chronological order, giving them a personalized alternative to the main homepage.

<p align="center"><img src="docs/screenshots/following.png?raw=true" alt="Following Posts" width="700"></p>

<br>

## Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | JavaScript, HTML, CSS, Bootstrap |
| Backend | Django, Python |
| Database | SQLite |

<br>

## How It Works

The interface is built around a single persistent Bootstrap layout, so the navigation bar and overall page structure stay in place while only the content area changes as users move between the homepage, profiles, and their feed. Actions that need to feel instant, such as liking, disliking, and editing a post, are handled by JavaScript, which sends an asynchronous request to a dedicated Django endpoint for that action and updates only the relevant part of the page, such as a like count or the post content, without a full reload. Most other navigation, including viewing posts, profiles, and the following feed, is handled through standard Django views and templates that render on the server. Posts, follower relationships, likes, and dislikes are all stored as related records in a SQLite database through Django's models.

<br>

## Future Improvements
Several enhancements are planned to extend the functionality of the application:
- Comments on posts
- Direct messaging between users
- Notifications for new followers and post reactions
- A live hosted demo to allow users to try the application without a local setup

<br>

## Getting Started

Follow the steps below to set up and run the application on your own machine. 

<br>

**Prerequisites**

Make sure Python 3 is installed before you begin. You can check by running the command below, which should print a version number.
> **Note:** This project requires Python 3.10+, per Django 5.2's supported versions.
```bash
python3 --version  # On Windows use: python --version
```

<br>

**1. Clone the Repository**

This downloads a copy of the project to your computer and moves you into the project folder.
```bash
git clone https://github.com/steph-xue/network.git
cd network
```

**2. Create and Activate a Python Virtual Environment**

This keeps the project's dependencies separate from other Python projects on your machine.
```bash
python3 -m venv venv      # On Windows use: python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install the Dependencies**

This installs all dependencies the project needs to run.
```bash
pip install -r requirements.txt
```

**4. Set Up the Database**

This creates a local SQLite database for the application.
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Populate the Database with Demo Data**

This populates the SQLite database with sample demo data.
```bash
python manage.py seed_data
```

**6. Start the Development Server**

This runs the application locally.
```bash
python manage.py runserver
```

Once the server is running, open the local URL shown in the terminal to start using the application.
