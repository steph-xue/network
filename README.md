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
     - Post contents
     - Date and time post was made
     - 
   
   
   - a list of all active auction listings (sorted alphabetically by title)
     - This can be accessed via the 'Active Listings' tab 
     - Each auction listing card on the homepage displays the following:
       - Title
        - Image
        - Description
        - The starting price
        - The highest bidding price (and the user who made the bid)
        - A 'more details' button to view more detailed information in the the auction listing page

**2. Viewing a specific user's profile**  
   - The user can view a list of all active auction listings (sorted alphabetically by title)
     - This can be accessed via the 'Active Listings' tab 
     - Each auction listing card on the homepage displays the following:
       - Title
        - Image
        - Description
        - The starting price
        - The highest bidding price (and the user who made the bid)
        - A 'more details' button to view more detailed information in the the auction listing page
&nbsp;

![Active Listings](/auctions/static/auctions/images/active_listings.png?raw=true "Active Listings")
<br></br>

**2. Viewing more detailed information in the the auction listing page**
   - The user can view more details about the selected auction listing item, add or delete items to their watchlist, add a bid greater than the starting price and last highest bid price, and leave or delete comments listed in reverse chronological order.
    - This can be accessed by clicking into viewing 'More Details' about a particular listing item
    - Information on the auction listing pages includes the following:
      - Title
        - Image
        - Description
        - Category
        - Listing Owner
        - The starting price
        - The highest bidding price (and the user who made the bid)
        - Comments made with regards to the listing item
&nbsp;
       
![Listing Page](/auctions/static/auctions/images/listing_page.png?raw=true "Listing Page")
<br></br>

**2. Searching auction listings by category**
   - The user can search the list of active listings by category based on the listed categories available
    - This can be accessed via the 'Categories' tab 
    - Listings in each category are sorted alphabetically by title
&nbsp;

![View by Category](/auctions/static/auctions/images/view_category.png?raw=true "View by Category")
<br></br>

## Features where login authentication is needed:
**1. Creating new auction listings**
   - Can be accessed via the 'Create Listing' tab 
   - Users can create a new auction listing by providing the following information:
      - Title
        - Description
        - Image URL (optional)
        - Starting price
        - Category
      - The new auction listing will specify the user as the owner of the listing
&nbsp;

![Create a New Listing](/auctions/static/auctions/images/create_listing.png?raw=true "Create a New Listing")
<br></br>

**2. Using the watchlist**
   - The watchlist can be used to help users keep track of listing items they are interested in
   - Users can add/remove listing items to/from their own watchlist
   - The function to add and remove watchlist items can be found on the auction's listing pages as a button:
      - 'Add to Watchlist'
         - 'Remove from Watchlist'


## Specifications and How to Run
- The email project was created using Django, a Python-based web framework, for the backend and JavaScript for the front end to create a mix of possible user interactions
- The web application can be run in the terminal using 'python3 manage.py runserver'
