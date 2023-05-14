#  Recipe App

 This ia a  recipe app that utilizes a full-stack framework including Django, Python, HTML, and CSS. The app is designed to enable users to easily create, add, edit, and comment on recipes, and the website is fully responsive and functional.

**Developer: Antony Maina**

[Visit live website](https://recipe2023.herokuapp.com/)

## Table of Contents
1. [About](#about)
  
2. [UX](#ux)
    - [User Stories](#user-stories)

3. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)

# About
My recipe app in Django is a great way to organize and share recipes online.The app typically includes features such as the ability to create, read, update and delete (CRUD) recipes
The recipe app is usually designed with a user-friendly interface that allows users to easily navigate through the app and find the recipes they are interested in. It can also include additional features such as creating profiles and leaving comments.

# UX
* The recipe app has a user friendly interface i.e it is easy to use and navigate through easily.
* I used a simple and visually appealing design.
* I personalizes the app by creating user profiles and ability to update pictures.
* There i also user feedback by leaving comments of the cuisine.
* There are also instructions on which type of ingredients and description of the cuisines.

## User Stories 

**Admin**
- As a Site admin I can view contact comments so that i can make my cusine site more appealing to user
- As a site Admin I can create, edit and delete recipes and comments so that I can manage the site content
- As a Site admin I can log in admin dashboard so that i can edit cuisines/comments/profiles
- As a site Admin I can log out of the admin panel so that I can disconnect from the website

**Site User**
- As a Site user  I can see if i'm logged in or out  so that i can see what my status is
- As a Site user I can write comments on recipes so that I can leave my feedback
- As a Registered user I can edit my profile so that i can update my personal information
- As a Registered user I can view my profile so that i can manage my personal information
- As a Site user I can delete my comment so that i can correct a mistake made
- As a Site user I can see the ingredients so that i can see what i should buy to make a recipe
- As a Site user I can create a recipe so that i can contribute and get feedback from my skills
- As a Site User I can register an account so that i can view recipes
- As a Site user I can comment on the cuisine so that i can share my thoughts with others
- As a Site user I can easily navigate through the site so that i can view the desired content

#
# Scope 

## **Features**
### **Home Page**
*Navigation bar:* 
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'About', 'Add cuisines', 'Contact', 'profile', 'login'  and 'Register'
- When the user is logged in the users 'Profile' and 'Logout' link apppear
- When the user registers a placeholder image appears and the user can add a picture at any time.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

<p align="center">
<img src="assets/images/navbar.png" width="50%" height="50%">
</p>


*Hero Carusell:*
- The hero carusell shows the user what the app ias about and the variuos type of cusines on the app.

<p align="center">
<img src="assets/images/carousell.png" width="50%" height="50%">
</p>

*Recipe/Cuisine:*
Just below the carusell are the recipes that have be created by the user or by the admin.
- At the top we have the 'author'
- Description about the recipe comes at the second position
- Ingredients about the recipe comes at the third position
- Created on date of the recipe is also visualized in this section.
- The view cuisine button is at the bottom of the card ab when clicked directs us to the comment section

<p align="center">
<img src="assets/images/recipe-cuisine.png" width="50%" height="50%">
</p>

*Comments section*
- Only logged in users can comment on a recipe
- logged in users can only delete their own comments.
- Admin can also delete comments.

<p align="center">
<img src="assets/images/add-delete-comment.png" width="50%" height="50%">
</p>


### **About Page**
- The page highlights the team's goal to inspire and encourage people to get creative in the kitchen by providing a recipe menu that is accessible to everyone, regardless of their skill level. 
- The team emphasizes the importance of making cooking fun and enjoyable for everyone and hopes that their website will inspire people to try new and exciting dishes.
- Overall, the "about us" page is intended to provide a brief introduction to the team's philosophy and approach to cooking, and to encourage visitors to explore the recipe menu and try out some of the team's favorite dishes

<p align="center">
<img src="assets/images/about.png" width="50%" height="50%">
</p> 

### **Add a cuisine**
- This is the main page of the logged in user.
- User can a add a title about the recipe he/she wants to create
- User can add a description abou the recipe
- User can add ingredients about the recipe 
- User can add image of the recipe
- when the user saves the image it it highlighted in the home page

<p align="center">
<img src="assets/images/add-cuisine.png" width="50%" height="50%">
</p> 

### **Contact Us**

- The contact us page in this recipe app is typically a way for users to get in touch with the admin . 
- It is a separate page that contains contact information i.e Name, Email and Subject.
- It has a submit button which directs the message to the admin of the app.

<p align="center">
<img src="assets/images/contact.png" width="50%" height="50%">
</p> 

### **Profile**
- In this section the user can see their logged in status
- in this section the user can edit the placeholder image and update their own

<p align="center">
<img src="assets/images/profile.png" width="50%" height="50%">
</p> 

### **Login/Register**
- The Register button takes users to the login page where they can also find a link to the Register page where they can create an account
- when a user is logged in the logout button dynamically appears to show the status of the user.

<p align="center">
<img src="assets/images/register.png" width="50%" height="50%">
</p> 

### **Footer**
- Appears on every page and contains social media links
- Links are opened in a new tab to avoid dragging users from our site

<p align="center">
<img src="assets/images/footer.png" width="50%" height="45%">
</p> 

# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:
- [Balsamiq wireframes](assets/documents)

# Database schema

<p align="center">
<img src="assets/documents/database-schema.png" width="50%" height="50%">
</p>

## Models
### **Cuisine Model**
<p align="center">
<img src="assets/images/class-cuisine.png" width="50%" height="50%">
</p>

### **Contact Model**
<p align="center">
<img src="assets/images/class-contact.png" width="50%" height="50%">
</p>

### **Profile Model**
<p align="center">
<img src="assets/images/class-profile.png" width="50%" height="50%">
</p>

### **Comment Model**
<p align="center">
<img src="assets/images/class-comment.png" width="50%" height="50%">
</p>


