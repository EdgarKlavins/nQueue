# nQueue

## Milestone Project 4 - Full Stack Development

<h2 align="center"><img src="docs/README/responsive.png"></h2>

My milestone Project 4 is a fully functional online bookstore dedicated exclusively to self-development books. This fictional e-commerce platform offers a wide selection of titles focused on personal growth, mental wellness, productivity, and motivation. The store provides an intuitive and seamless shopping experience, allowing users to browse, search, and purchase books effortlessly.

## Live Project

[View the live project here.](https://nqueuebookstore-234df69c8477.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/EdgarKlavins/nQueue)


# UX

### Desciption

The main purpose of this project is to create a full stack website with django including stripe payments, designed to browse, search and buy books.

## Project Goals
<ul>
    <li>To design and build a realworld Full Stack MVC application with a Front end</li>
    <li>To implement simple and clean design that is easy to navigate
    and allows the user to find information and resources intuitively.
    </li>
    <li>Where the purpose is immediately evident to a new user</li>
    <li>Which provides a good solution to the user’s demands and expectations</li>
    <li>To create a good looking website that responds correctly on all device sizes.</li>
    <li>A website that has user authentication</li>
    <li>A website that has user uuthorization</li>
    <li>A website is providing CRUD operations where all data (CRUD)
    actions are immediately reflected in the user interface.
    </li>
    <li>A website which is linked to external database</li>
    <li>Configure the project efficiently through wellkept Procfile, requirements.txt file,
    settings files, keeping the data store configuration in a single location where it can be changed easily.
    </li>
    <li> Fully describe the data schema in the project README file.</li>
    <li> Demonstrate solid understanding of Django template syntax, logic and usage</li>
    <li> Use version control software effectively to provide a record of the development process.</li>
</ul>
<br>

## User Stories

### As a Customer:
1. **Account Creation:**
   - As a customer, I want to create an account so that I can manage my orders and personal information.
   
2. **Login and Logout:**
   - As a customer, I want to log in to my account so that I can access my personal dashboard and order history.
   - As a customer, I want to log out of my account so that my personal information remains secure.

3. **Browse Books:**
   - As a customer, I want to browse through the book categories so that I can find books that interest me.
   
4. **Search Books:**
   - As a customer, I want to search for books by title, author, or keyword so that I can quickly find specific books I am looking for.
   
5. **Book Details:**
   - As a customer, I want to view detailed information about a book, including its description, author, and ratings, so that I can make an informed purchase decision.
   
6. **Add to Cart:**
   - As a customer, I want to add books to my shopping cart so that I can purchase multiple items at once.
   
7. **Manage Cart:**
   - As a customer, I want to view, update, and remove items from my shopping cart so that I can manage my intended purchases.
   
8. **Checkout:**
   - As a customer, I want to securely enter my payment information and complete the purchase process so that I can buy the books I want.
   
9. **Order Confirmation:**
   - As a customer, I want to receive an order confirmation email so that I have a record of my purchase.

10. **Order History:**
    - As a customer, I want to view my past orders so that I can keep track of my purchases.

### As a Visitor:
1. **Explore Website:**
   - As a visitor, I want to browse the website without creating an account so that I can explore the available books.
   
2. **Search Books:**
   - As a visitor, I want to search for books by title, author, or keyword so that I can find books that interest me.
   
3. **Book Details:**
   - As a visitor, I want to view detailed information about a book so that I can learn more about it before deciding to purchase.

4. **Create an Account:**
   - As a visitor, I want to create an account so that I can save my favorite books and make future purchases.

### As a Site Owner:
1. **Manage Books:**
   - As a site owner, I want to add, update, and remove books from the catalog so that I can keep the inventory current and accurate.
   
2. **View Orders:**
   - As a site owner, I want to view customer orders so that I can fulfill them efficiently.

3. **Manage Users:**
   - As a site owner, I want to manage user accounts, including registration and permissions, so that I can maintain the security and integrity of the site.

<br>

## Design

   ### Wireframes

   1. **Home page** displays the introduction and purpose of the website.

   [Home page](docs/README/wireframes/homew.png)


   2. **Books** displays list of products.

   [Books page](docs/README/wireframes/Products.png)


   3. **Product desciption** displays details of the products, gives option to add to bag.

   [Details page](docs/README/wireframes/description.png)

   4. **Shopping bag** displays details of the products, gives option to add to bag.

   [Shoping bag](docs/README/wireframes/Shoping_bag.png)

 <br>


 ### Colour Scheme

 - For my project I used a  colour scheme of warm browns, greys and yellows. I chosed colors to match the main bacground theme with books.



 <h2 align="center"><img src="docs/README/colordesign.png"></h2>

 <br>


 ### Typography

 - As Google fonts I have picked two fonts.

 

 1.  <h2 align="center"><img src="docs/README/Font1.png"></h2>


 2. <h2 align="center"><img src="docs/README/Font2.png"></h2>



 <br>


 ### Imagery 


 For my main bacground image, to create smart, classical atmosphere, I used Old Vintage Bookshelf from https://www.freepik.com/

 <h2 align="center"><img src="media/background.jpg"></h2>

 And open book image at my homepage from https://www.shutterstock.com/

 <h4 align="center"><img src="media/book5.jpg" width="1000" height="800"></h4>


 Rest of images for my product list are takken directly from www.amazon.co.uk books as url_images.

 <br>

 ### Icons

 All icons through out the website are imported from Font Awesome

 #### Main Navigation

 * Search Icon: Used in the search bar within the header section.
 * Shopping Bag Icon: Displayed in the navigation bar to represent the shopping bag.
 * Footer section for Facebook profile, LinkedIn profile,  Instagram profile and GitHub profile

 #### Bag

 * Star Icon: Displayed next to product ratings.
 * Minus and Plus Icon: Used in the decrement and increment quantity button.
 * Chevron Left Icon: Used in the "Keep Shopping" button. 
 * Lock Icon: Used in the "Secure Checkout" button. 

 <br>

# Features


 ### Header 

 The header sets the tone and branding of the website containing:

  * Main Title: Displays "nQueue - Personal Development Books", reinforcing the website's focus.
  * Tagline: "Invest in yourself", encouraging users to see the value in personal development books.
  * Search Bar, features an input field and a search button styled to match the site's design and allows users to search for books by entering keywords.

 ### Navigation Bar

 The navigation bar provides a user-friendly, responsive  interface to navigate through the website and contain:
  
  * Home, which links directly to the homepage, allowing users to easily return to the starting point of the website.

  * Books, dropdown menu that offers several options:

     *  All Books: Links to a page displaying all available books.
     *  By Rating: Sorts and displays books by their rating in descending order, helping users find the highest-rated books.
     *  By Price: Sorts and displays books by their price in ascending order, assisting users in finding budget-friendly options.

   * Genre, dropdown menu categorizing books into different genres:
      
     * Motivational & Inspirational: Links to books that inspire and motivate.
     * Self-help: Links to books focusing on personal development and self-improvement.
     * Spirituality: Links to books exploring spiritual topics.
     * Personal Finance: Links to books providing financial advice and strategies.
     * Biography: Links to biographies of influential individuals.

   * Best Sellers, direct link to a page showcasing the best-selling books, helping users quickly find popular and recommended reads.

   * My Account, dropdown menu that changes based on the user's authentication status
     * Authenticated Users:

        * Product Management: Available only for superusers, linking to a page where products can be managed (added, edited, deleted).
        * My Profile: Links to the user’s profile page, allowing them to view and edit their personal information.
        * Logout: Provides a logout option to end the user's session.

     * Unauthenticated Users:
        * Register: Links to the registration page for new users to sign up.
        * Login: Links to the login page for existing users to access their accounts.

   * Shopping Bag, a dynamic link displaying the total cost of items in the user’s shopping bag. Including:

      * Shopping Bag Icon: visual indicator of the shopping bag.
      * Total Amount: shows the current total price of the items in the bag.
      * Links to the shopping bag page where users can view and manage their selected items.
 

 






