<h1 align=center> </h1>

<p align=center>

</p>
<p align="center">
<img src="">
</p>

Live app link [here](https://theregionaltaste.herokuapp.com/)


## User Experience

### User Stories

1. As a user, I would like to be able to …

    1.1 ... register using name, email, username and password;
    
    1.2. ... login on website using my email/username and password;
    
    1.3 ... logout easily;
    
    1.4 ... have all information about website services on landing page;

    1.5 ... see details about each available box;
    
    1.6 ... add boxes on my bag;

    1.7 ... check all available boxes and products;

    1.8 ... pay for my product using a Credit Card;

    1.9 ... add my shipping and billing address;

    1.10 ... get a confirmation email with my order and shipping details;

    1.11 ... create my profile

    1.12 ... check my previous order details on profile page;

    1.13 ... subscribe the newsletter;

    1.14 ... unsubscribe the newsletter;

    1.14 ... select 5 products to add on my box;

    1.15 ... check user's review's on boxes;

    1.16 ... add a review on boxes;
    
    1.17 ... edit or delete my reviews on boxes. 

2. As a site admin, I would like to be able to …

    2.1  ... have admin privileges and check the product management page;

    2.2 ... be present to a list of products to edit or delete;

    2.3 ... create products or add them to the boxes;

    2.4 ... o delete created products or boxes;

    2.5 ... the user to be redirected to a specific page if any error happens.

### 1. Strategy

  + **Project Goal**

Create an e-commerce app that allows people (users) who lives out of their home countries or loves different cuisines to have access to a range of regional products from various part of the world.  

### 2. Scope

 * A simple, straightforward, intuitive UX experience;
 * An explicit content; 
 * An easy navigation for the user through all the features;
 * A site that is visually appealing on most devices.

## Functional Scope 

**Flowchart**

<img height= "" src="">

**DER - Diagram Entity Relationship**

<img width= "" src="">

**Agile Methodology**

All functionality and development of this project were managed using [Jira](https://bestbeer.atlassian.net)

* Credentials to this management tool will be provided during submission.

<details>
<summary>All sprints are described here.</summary>

Test cases were linked with every User story presented above, and can be found in [TESTING.md](TESTING.md)- Automated testing section. 

* Sprint 1 - 04/01/2022 - 11/01/2022 (Finished at 09/01/2022)

  + Initial setup
    - As a developer, I want to setup django templates
  + Create Database and Deployment on Heroku
    - As a developer, I want to set up a Database to store all data 
    - As a developer, I want to deploy website on Heroku
  + Create user registration and login/logout features
    - As a user I want to register on website
    - As a user I want to login on website
    - As a user I want to logout on website
    - As a site admin I want to have admin privileges 

* Sprint 2 - 09/11/2022 - 16/01/2022 (1 week)

  + Create products page
    - As a shopper I want to to see details about each available box
    - As a shopper I want to add product on my bag 
    - As a shopper I want to check all available products 
    - As a shopper I want to sort a list of products by region (Not done on this sprint. Will be add in future sprints)


* Sprint 3 and 4 - 17/01/2022 - 24/01/2022 (2 weeks)

  + Create order and payment pages
    - As a user I want to pay for my product 
    - As a user I want to add my shipping and billing address
    - As a user, I want to get a confirmation email with my order and shipping details 

* Sprint 5 - 30/01/2022 - 06/02/2022

  + Create Profile
    - As a user, I want to create my profile
    - As a user I want to check my previous order details

* Sprint 6 - 07/02/2022 - 14/02/2022

  + Add products on Box
    - As a user, I want to select 5 products to add on my box

  + Product Management
    - As a site admin, I want to create products or add it to the box
    - As a site admin, I want to delete created products
    - As a site admin, I want to be present to a list of products to edit or delete

* Sprint 7 - 13/02/2022 - 20/02/2022

  + User acceptance
    - As a user I want to use all features on platform without major issues

  + Validation
    - As a site owner I want to make sure that all files are validateds


</details>


### 3. Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have a leisurely experience.
* Navbar is fixed on top to facilitate users to navigate through pages easily. Small navigation is the same on all pages to ensure easy navigation.
* Footer is fixed on the bottom with links to social media and newsletter subscription.

### 4. Skeleton

Wireframes created with Balsamiq. The project was developed from initial wireframes, and some modifications were made during the development process in respose to user feedbacks and to assure the best usability. 

* UI was changed during the project to ensure better user experience.

Click to see wireframes (before UI changes):

[HomePage](media/readme/wireframes/homepage.png) <br>
[Register Page](media/readme/wireframes/register_page.png) <br>
[Login Page](media/readme/wireframes/login.png) <br>
[Reginal items Page](media/readme/wireframes/region_items_available.png) <br>
[Bag Page](media/readme/wireframes/bag.png) <br>
[Payment Page](media/readme/wireframes/payment_page.png) <br>
[Order Placed Page](media/readme/wireframes/order_placed_page.png) <br>
[Site Map Page](media/readme/wireframes/site_map.png) <br>

### 5. Surface

* Colours

The Colour scheme was generated using the eyedropper plugin to get one colour from the logo image and [colours](https://coolors.co/) to create the colour palette.

<img width="300" src="media/readme/regionaltastepallete.jpg">

* Font Selection
 
Two complimentary fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the website.

The chosen fonts were Roboto for headings and navbar and Lato for links, buttons and paragraphs.

<img width="200" src="media/readme/googlefonts_roboto.jpg">
<img width="200" src="media/readme/googlefonts_lato.jpg">

## Existing Features

<details>

<summary> Here you can find a description of all features availabe on the platform. </summary>

### **Navbar** 

+ Fixed Navbar allow the user easy access to all pages. 

1. On the left site, How it works and Boxes links leads user to this pages;

2. On the right side Account and Cart buttons are available to user;

<img width="800" src="media/readme/features_ss/navbar.jpg">

  2.1 Not logged user:

  + Register and Login options are available

<img width="200" src="media/readme/features_ss/notlogged_account_navbar.jpg">

  2.2 Admin logged user:

  + Product Management, Login and Logout options available

<img width="200" src="media/readme/features_ss/admin_account_navbar.jpg">

  2.2 Customer logged user:

  + Login and Logout options available

<img width="200" src="media/readme/features_ss/customer_account_navbar.jpg">

  2.3 Cart Button are available to all users and leads to respective page

3. Collapsed navbar on smaller devices to wrap in all options and assure better navbar design.

<img width="300" src="media/readme/features_ss/collapsed navbar.jpg">

### **Footer** 

+ Sticky footer present in all pages with link to susbcribe to newsletter and social media links. 

<img width="800" src="media/readme/features_ss/footer.png">

### **Homepage** 

1. Homepage jumbotron 

  + A brief explanation about the store with a button link to products page

<img width="400" src="media/readme/features_ss/home_jumbotron.jpg">

### **How it works** 

1. 3 steps images 

  + A brief explanation about how the store works

<img width="400" src="">

### **Boxes Page** 

1. Cards with all available boxes are present on this page with image, description and price. 

<img width="400" src="">

2. Buttons are available in each card to lead user to add the box directly to the cart or customize it

<img width="400" src="">

### **Boxes Details Page** 

1. A card with all box information are available to the user (box name, description, image, standart products, selectable products and price)

<img width="700" src="media/readme/features_ss/box_details.jpg">

2. The user can customize the box choosing 5 items from checkbox list before add the box to cart. In case the user dont customize the box, 5 surprise items will be added to their box in the cart page. 

3. User's reviews are availabe on the bottom of the box card and can be viewed by all customers (logged or not)

<img width="500" src="media/readme/features_ss/users_review_box.jpg">

4. A logged user can add a review about the box clicking on Add Product Review button. 

<img width="400" src="media/readme/features_ss/add_review_button.jpg">

### **Shopping Cart Page** 

1. User can check all data about the boxes in the cart (box name, quantity, selected products, number of items and total price)

2. On the right side, an order summary is available with number of items and total price

<img width="800" src="media/readme/features_ss/shopping_cart.jpg">

3. Optional buttons can lead user back to the boxe page or to checkout 

<img width="200" src="media/readme/features_ss/cart_buttons.jpg">

### **Checkout Page** 

1. Shipping address 

  + User can add a shipping address and save it on profile if didn't do it before. 
  + User can add the same billing address just checking the checkbox 

<img width="700" src="media/readme/features_ss/shipping_address.jpg">

2. Billing address 

  + User can add a billling address and save it on profile if didn't do it before. 

<img width="700" src="media/readme/features_ss/billing_address.jpg">

  + User can auto complete billing address with saved shipping address from profile 

<img width="700" src="media/readme/features_ss/billing_shipping_same.jpg">

### **Confirm Order Page** 

1. All shipping and billing address ae available to be confirm by the user

2. If want to change address user can come back to the last page and change it

<img width="700" src="media/readme/features_ss/confirm_order.jpg">

### **Payment Page** 

1. Credit card only payments are available on this page

<img width="400" src="media/readme/features_ss/payment.png">

### **Management Page** 

1. On his page, admin user can find all options to add, edit or delete products, boxes and products on boxes, and also check all sent newsletters or send a new one. 

<img width="700" src="media/readme/features_ss/management.png">

  1.1 Send newsletter 

  + Admin user can send newsletter to all user or just chose some of them .

<img width="700" src="media/readme/features_ss/send_newsletter.png">

  1.2 Newsletters sent 

  + Display a list of all sent newsletters

<img width="700" src="media/readme/features_ss/sent_newsletter.png">

  1.3 Add box, product and product on box 

  + Admin user can add all products in database from frontend.

<p float="left">
<img width="400" src="media/readme/features_ss/add_box.png">  
<img width="400" src="media/readme/features_ss/add_products.png">
<img width="400" src="media/readme/features_ss/add_products_on_the_box.png">
</p>

  1.4 Box, product and product on box list to edit or delte

 + Admin user can edit or delete or all products in database from frontend.

<p float="left">
<img width="400" src="media/readme/features_ss/boxes_list.png">  
<img width="400" src="media/readme/features_ss/products_list.png">
<img width="400" src="media/readme/features_ss/products_on_box_list.png">
</p>

  1.5 Edit box, product and product on box 

 + Admin user can edit or all products info in database from frontend.

<p float="left">
<img width="400" src="media/readme/features_ss/edit_box.png">  
<img width="400" src="media/readme/features_ss/edit_products.png">
<img width="400" src="media/readme/features_ss/edit_producst_on_boxes.png">
</p>

</details>

## Future Features

1. Paginate Box, Products and Products on boxes list to show the admin user only 20 items per page;
2. Create a seach feature to management page to make easier find boxes, products and products on boxes;
3. Store all orders ins a json file to have all data even if boxes or products were deleted;
4. Create a wishlist in user profile;
5. Display all users comments on profile page;
6. Only alow user to comment on prduct if they already bought it. 


## Languages Used

Python 3.0

## Frameworks, Libraries & Programs Used

+ Balsamiq: Balsamiq was used to create the wireframes during the design process.
+ Favicon Generator: Used to create favicon used on the website.
+ Font Awesome: Font Awesome was used on all pages to add icons for aesthetic and UX purposes.
+ Grammarly: Used to correct any spell mistakes on readme and app text.
+ Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
+ GitHub: GitHub is used to store the project's code after being pushed from Git.
+ Google Fonts: Google fonts are used to add fonts for aesthetic and UX purposes.
+ Django: Framework used to add structure to the platform. 
+ PGAdmin: Used to administer Database and generate DER.
+ Multi Device Website Mockup Generator: Used to generate mockup image.


## Testing and Code validation 

All testing and code validation details are described in a separate file called TESTING.md and can be found [here](TESTING.md).

## Project Bugs and Solutions:

| Bugs              | Solutions |
| ---               | --------- |
| Cart count item just works when user add product to the cart, do to cart, come back to the previous page and refresh | Change functon on context and add cart count on it |
| Get cart total function stotp works when ordered box are deleted | Create a exclude item on this property  |

## Deployment 

This App is deployed using Heroku.

<details>
<summary>Heroku Deployment steps </summary>
 
 1. Ensure all dependencies are listed on requirements.txt. 
 
 Write on python terminal ` pip3 freeze > requirements.txt`, and a list with all requirements will be created to be read by Heroku. 
 
 2. Setting up your Heroku

    2.1 Go to Heroku website (https://www.heroku.com/). 
    2.2 Login to Heroku and go to Create App.
    
    <img src="media/readme/deployment/heroku_login.png">
    
    <img src="media/readme/deployment/heroku_login2.png">
    
    2.3 Click in New and Create a new app
    
    <img src="media/readme/deployment/heroku_newapp.png">
    
    2.4 Choose a name and set your location
    
    <img src="media/readme/deployment/heroku_createnewapp.png">

    2.5. Navigate to the Resources tab 

    <img src="media/readme/deployment/heroku_resoursces_tab.png">

    2.6. Click on Resources and Seach for Heroku Postgres and select it on the list.
    
    <img src="media/readme/deployment/heroku-postgres.png">
    
    2.7. Navigate to the deploy tab
    
    <img src="media/readme/deployment/heroku_dashboard_deploy.png">
    
    2.8. Click in Connect to Github and search for 'nandabritto' GitHub account and 'PP5' repository
    
    <img src="media/readme/deployment/heroku_github_deploy.png">
    
    2.9.  Navigate to the settings tab
    
    <img src="media/readme/deployment/heroku_dashboard_settings.png">
    
    2.10.  Click on Config Vars, and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    
    <img src="media/readme/deployment/heroku_vars_settings.png">
    
 

3. Deployment on Heroku

    3.1.  Navigate to the Deploy tab.
    
    <img src="media/readme/deployment/heroku_dashboard_deploy.png">
    
    3.2.  Choose the main branch to deploy and enable automatic deployment to build Heroku every time any changes are pushed on the repository.
    
    <img src="media/readme/deployment/heroku_automatic_deploys.png">
    
    3.3 Click on manual deploy to build the App.  When complete, click on View to redirect to the live site. 
    
    <img src="media/readme/deployment/heroku_view.png">
</details>

<details>
<summary>Forking the GitHub Repository </summary>

* By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account, allowing you to view and/or make changes without affecting the original repository by using the following steps:

    Log in to GitHub and locate the GitHub Repository
    At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
    You should now have a copy of the original repository in your GitHub account.

* Making a Local Clone

    Log in to GitHub and locate the GitHub Repository
    Under the repository name, click "Clone or download".
    To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    Open Git Bash
    Change the current working directory to the location where you want the cloned directory to be made.
    Type git clone, and then paste the URL you copied in Step 3.

$ git clone https://github.com/nandabritto/PP5

Press Enter. Your local clone will be created.
</details>


# Credits

## Media

+ All pictures and images used in this project are from [Depositphotos](https://depositphotos.com) and [Unsplash](https://unsplash.com/).

## Work based on other code

[**JustDjango Youtube Channel**](https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ) - Used as a base to develop cart and checkout features<br>
[**Dennis Ivy Youtube Channel**](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg)- Used as a base to develop cart, checkout and confirmation email features<br>
[**Master Code Online**](https://www.youtube.com/channel/UCbhm6TbMBTWn_GxrIbPFapA)- Used as a base to develop newsletter app <br>
[**Code With Stein**](https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg)- Used as a base to develop box reviews app <br>
 
# Acknowledgements

+ Stack Overflow is a valuable resource for solving lots of issues.
+ W3schools and Django documentation for general reference.

I would also like to thank:

+ My husband Guilherme for all the support on stressful moments, helping to figure out lots of bugs and for reviewing everything.
+ Code institute tutors and my CI Mentor Daisy Mcgirr for the guidance and help with several issues and bugs.