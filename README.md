# VeggieNosh: Vegan Recipe-Sharing Web Application

Dedicated to the vibrant world of vegan cuisine, VeggieNosh is a contemporary recipe-sharing platform drawing inspiration from esteemed sites like [The Vegan Society](https://www.vegansociety.com/) and [Rainbow Plant Life](https://rainbowplantlife.com/). It provides users with a user-friendly interface to craft, share, and archive their cherished vegan recipes.

> **Note**: This endeavor is an integral component of the Code Institute’s Milestone Project 3, as part of their Diploma in Full Stack Software Development. It proficiently demonstrates the implementation of HTML, CSS, JavaScript, Python+Flask, MongoDB, and other technologies, meeting the essential criteria for CRUD (Create, Read, Update, and Delete) operations.

**[View Live Website Here](#)** _(Replace `#` with your live website URL)_

---

## Table of Contents
- [UX Development Planes](#ux-development-planes)
  * [Strategy Plane](#strategy-plane)
  * [Scope Plane](#scope-plane)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
  * [Surface Plane](#surface-plane)
- [Features](#features)
- [Issues and Bugs](#issues-and-bugs)
- [Testing](#testing)
- [Technology Used](#technology-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## UX Development Planes

### A. Strategy Plane
#### User Stories

**New/Unregistered User:**
- Search for recipes easily.
- Explore all site recipes.
- View complete recipes of interest.
- Intuitive navigation with clear Sign-Up.
- Understand the site's purpose and functionality.

**Returning/Registered User:**
- Quick access to Log In.
- View latest recipes.
- Access account settings, personal cookbook, and other user-specific pages.
- Manage profile and recipes (create, edit, delete).
- Share recipes on social media.
- Print recipes.
- Access a contact page for queries.

**Administrative User:**
- All functionalities of a registered user.
- Manage recipe categories.
- Edit or delete any site recipes.

#### Online Research
For UI and UX inspiration, research included platforms like:
- [The Vegan Society](https://www.vegansociety.com/) 
- [Rainbow Plant Life](https://rainbowplantlife.com/)
- various projects on [Dribbble](https://dribbble.com/)
- Projects by Code Institute peers (from `peer-code-review` on Slack).

#### Project Goals
VeggieNosh aims to provide a visually appealing and user-friendly platform for sharing recipes. Users can:
- Create, edit, delete, and save recipes.
- Search recipes.
- Print, and share recipes on social media.

#### User Goals
Users seek a:
- Simple and modern recipe-sharing platform.
- Community to share and discover recipes.
- Personal online cookbook for favorite recipes.

**Target Audience:**
- All age groups.
- Vegan community.
- Foodies and food-enthusiasts.
- Cooking and baking enthusiasts.
- Tech-savvy users who share recipes online.

#### Site Owner Goals
The site owner aims to:
- Offer a comprehensive online recipe-sharing platform.
- Engage with the community as a regular user.
- Curate the platform's content and categories.
- Maintain platform quality and adherence to rules.

#### Strategy Table
A thorough brainstorming session was conducted based on the user stories and goals. Opportunities were evaluated based on importance (driven by goals and user needs) and viability (considering time and resources).

_(Continue with other sections like Scope Plane, Structure Plane, etc. following a similar structure.)_

### B. Scope Plane

Based on the mapping in the Strategy Plane, a scope was defined for the site with room for future improvements.

## Functional Requirements

**Users** will be able to:

- Sign up and log in to the site by providing username and password.
- View and Edit their profile (option to change username and password).
- Delete their account.
- Upload a recipe.
- Edit their recipe.
- Delete their recipe.
- View all recipes on the site.
- Search for recipes.
- View the cookbook that is filled with their recipes.
- Print a recipe page.
- Share a recipe page.

**Admin/ Site Owners** will be able to:

- Have all functionalities as a user does.
- Add a category of recipes.
- Edit a category.
- Delete a category.
- Delete any recipes listed on the site (if needed).

## Non-Functional Requirements

- The users will be able to send a message to the Admin/ site owners via contact form.
- The users will be able to navigate easily and intuitively throughout the site, able to log in and log out at every page the users currently at.

## Content Requirements

- **Single Recipe Page:** Includes recipe name, description, serving size, time, category, ingredients, and direction. 

- **Home Page:** Features:
  - A button that redirects a user to the "All Recipes" page.
  - Displays 4 random images from the database using the $sample function of MongoDB.

- **Online Cookbook:** Features all recipes that had been saved to the cookbook by users, and users' uploaded recipes as well.

### C. Structure Plane

### D. Skeleton Plane

Wireframes/ mock-ups were created using Figma to design the navigation and interface of the website. For a better and clearer visualization before coding, and also to check if the color scheme and images match and work great together, the wireframes were created with such details, in three different device sizes: desktop, tablet, and mobile.

### E. Surface Plane

## Color Scheme

The overall theme of the site was orange and green[...] Using [Coolors](https://coolors.co/)[...]



