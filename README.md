# VeggieNosh
![VeggieNosh](veggienosh/static/images/readme/am_i_responsive.png)
Find the final project here: [VeggieNosh]()

## Table of Contents
- [Introduction](#introduction)
- [UX](#ux)
   * [User Stories](#user-stories)
- [Design](#design)
  * [Technical Framework](#technical-framework)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Features](#features)
    * [The Home Page](#the-home-page)
    * [The Navigation Bar Functionality](#the-navigation-bar-functionality)
    * [The All Recipe Page](#the-all-recipe-page)
    * [The Single Recipe Page](#the-single-recipe-page)
    * [The Registration Page](#the-registration-page)
    * [The Login Page](#the-login-page)
    * [The Logout Page](#the-logout-page)
    * [The Account Settings Page](#the-account-settings-page)
    * [The Change Username Page](#the-change-username-page)
    * [The Change Password Page](#the-change-password-page)
    * [The Delete Account Page](#the-single-recipe-page)
    * [The User Recipe Page(My Recipe Page](#the-user-recipe-page)
    * [The Add Recipe Page](#the-add-recipe-page)
    * [The Edit Recipe Page](#the-edit-recipe-page)
    * [The Delete Recipe Page](#the-delete-recipe-page)
    * [The 404 Error Page](#the-404-error-page)
    * [The 500 Error Page](#the-500-error-page)
    * [Features to Implement in the Future](#features-to-implement-in-the-future)
  * [Accessibility](#accessibility)  
- [Issues and Bugs](#issues-and-bugs)
- [Technologies Used](#technologies-used)
  * [Main Languages Used](#main-languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Testing](#testing)
  * [TESTING.md](#TESTING.md)
- [Deployment](#deployment)
  * [Deploying on GitHub Pages](#deploying-on-github-pages)
  * [Cloning the repository](#cloning-the-repository)
  * [Forking the repository](#forking-the-repository)
- [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
- [Acknowledgements](#acknowledgements)

## Introduction

### VeggieNosh: A Vegan Recipe-Sharing Platform

**Dedicated to the vibrant world of vegan cuisine**, VeggieNosh is a modern recipe-sharing platform inspired by esteemed websites such as [Vegan Recipe Club](https://veganrecipeclub.org.uk) and [Rainbow Plant Life](https://www.rainbowplantlife.com). The platform offers a **user-friendly interface** for crafting, sharing, and archiving beloved vegan recipes.

> _This project is a key part of the [Code Institute's Milestone Project 3](https://codeinstitute.net), contributing to the Diploma in Full Stack Software Development. It showcases a proficient implementation of **HTML, CSS, JavaScript, Python+Flask, MongoDB**, and other technologies. VeggieNosh fulfills the essential criteria for **CRUD operations**, allowing users to create, read, update, and delete recipes with ease._

## User Experience
### User Stories

#### New/Unregistered User
- Search for recipes easily.
- Explore all site recipes.
- View complete recipes of interest.
- Intuitive navigation with clear Sign-Up.
- Understand the site's purpose and functionality.

#### Returning/Registered User:
- Quick access to Log In.
- View latest recipes.
- Access account settings, personal cookbook, and other user-specific pages.
- Manage profile and recipes (create, edit, delete).
- Share recipes on social media.
- Print recipes.
- Access a contact page for queries.

#### Administrative User:
- All functionalities of a registered user.
- Manage recipe categories.
- Edit or delete any site recipes.

<details>
  <summary>Click to see Persona Forms!</summary>
  
  ![Persona forms]()
  ![Persona forms]()
</details>

# Design
VeggieNosh is designed to harmoniously blend user convenience with modern design principles. This online vegan cookbook exemplifies a commitment to creating an interface that is both visually appealing and easy to navigate. It's a platform where recipes are elegantly and clearly showcased.
The following design elements were used in the website:

- ## Technical Framework
The [Materialize](https://materializecss.com/) front-end framework, inspired by Material Design, was the choice for VeggieNosh, bringing a fresh, responsive feel to the table. Together with [JQuery](https://jquery.com/), it lays down the interactive groundwork that makes the navigation and presentation of recipes intuitive and fluid.

- ## Colour Scheme
VeggieNosh embraces a color scheme that draws eyes to the vibrant dishes. A backdrop of white space ensures that the rich colors of the food images pop, complemented by touches of green that echo the essence of fresh, vegan ingredients. The addition of coral energizes and directs users through calls to action, creating an inviting, dynamic experience without overwhelming the visual senses.

Core colors:
- coral (#ff4242): Selected for its lively and inviting quality, encouraging user interaction.
- lightblack (#2e2e2e): Ensures text is readable against the light background.
- mediumwhite (#fffafa) and white (#ffffff): Provide a clean and contemporary canvas for the content.
For account settings, a trio of colors was selected to intuitively guide users through their options:

- Red: For actions that require caution or are irreversible.
- Yellow: For moments where caution is advised or to signal a change.
- Green: For positive actions, confirming correct selections or completion.


## Colour Palette
Using the [Adobe Color](https://color.adobe.com/create/color-wheel) colour wheel

![Colour Palette](veggienosh/static/images/readme/colour-palette.png)

- ## Typography

• The choice of Open Sans as the primary font is deliberate, offering readability and a contemporary ambience, while Ubuntu lends a distinct personality to headings and buttons, enhancing the overall design language.

![Typography](veggienosh/static/images/readme/typography1.png)
![Typography](veggienosh/static/images/readme/typography2.png)

- ## Imagery
VeggieNosh website primarily relies on a text-based interface to create a distraction-free quiz environment. However, some key images and icons are used:
  * Logo: The VeggieNosh logo originated from [Hatchful](https://www.shopify.com/tools/logo-maker) and was later refined to enhance contrast, ensuring clear visibility across various platforms and display sizes. The final design showcases a stylized carrot set against a teal backdrop, with playful typography that echoes the vegan essence of the cookbook. This emblem is tailored to stand out and embody the freshness of the plant-based recipes featured on the site.

![Logo](veggienosh/static/images/readme/logo_design.png)

  * Icons: To enhance user engagement and facilitate content discovery, icons have been integrated extensively throughout VeggieNosh. Their use not only captures attention but also aids in content navigation and scanning. Icons serve as intuitive visual cues that transcend linguistic limitations, offering a more inclusive experience for non-native English speakers.

[Font Awesome](https://fontawesome.com/) is the primary source for the icons within the project, providing consistent and recognizable visuals for navigation bars, footers, forms, and recipe detail pages. In certain instances, [Materialize icons](https://materializecss.com/icons.html) have also been employed to complement the design.


  * [Favicon](https://www.favicon.cc/): A unique favicon is provided that is representative of the brand identity. It's visible in the browser tab for easy site identification.

## Wireframes
Wireframes were created for mobile, tablet and desktop using [Balsamiq](https://balsamiq.com/). Please note some improvements were made during the development of the website.

[Wireframes](documentation/wireframes)


# Features
## Existing Features

The website features a structured layout that includes a Home page, an All Recipes page, an Account Settings page, a Registration page, a Change Password page, a Change Username page, a Login page, a User Recipe page, a Single Recipe page, an Add Recipe page, a Search Recipe page, as well as dedicated 404 and 500 Error pages for navigational and server errors.

All Pages on the website are responsive and have:
- A [favicon](https://www.favicon.cc/) in the browser tab.

![Favicon](veggienosh/static/images/readme/browser-favicon.png)

- The Logo: The VeggieNosh logo is strategically positioned at the top of every page for consistent brand visibility. On desktop displays, the logo is placed at the top right, ensuring it's easily noticeable. For smaller screens, the logo is centered to maintain prominence. Clicking the logo from any page redirects users back to the home page, providing a convenient way to return to the start at any time.
![Logo](veggienosh/static/images/readme/logo_design.png)

- Social Media Icons:
Appearing on every page, the icons are appropriate representations of the Social Media platforms, linking users to the various platforms. The icons appear in the centre of the footer.The footer also carries the copyright notice.

![Social media links](veggienosh/static/images/readme/socials_icons.png)

### The Home Page

At the forefront of VeggieNosh, the home page welcomes visitors with a bright, cheerful banner highlighting an assortment of fresh vegetables, framing the site’s purpose in vibrant color. The logo, clear and central, pairs with an engaging tagline that beckons visitors to explore further. Below, the 'Star Veggie Picks' section artfully displays featured recipes, tempting the eye with their vivid imagery. The layout is crisp and user-centric, providing effortless navigation that complements the site’s professional and inviting atmosphere.


![Home Page](veggienosh/static/images/readme/home_page.png)

### The Navigation Bar Functionality

The navigation bar is designed for constant presence at the top of the page, ensuring users can effortlessly access different sections of VeggieNosh at any time. 
Adapting to various screen sizes, the navigation collapses into a hamburger icon on tablets and mobile devices, revealing a slide-out menu upon interaction for a clean, uncluttered experience.

Guest users will find the navigation bar includes essential links for seamless browsing:

![Home Page Navbar for New Users](veggienosh/static/images/readme/home_page_nav1.png)

Logged-in users benefit from an expanded set of options, improving their experience with personalized navigation:

![Home Page Navbar for Current Users](veggienosh/static/images/readme/home_page_nav2.png)

### The All Recipes Page
The 'All Recipes' page of VeggieNosh elegantly presents a collection of recipe cards, organized chronologically from the oldest to the newest additions. Accompanying the page heading is a count of the total recipes available, enclosed within parentheses for easy reference. Each recipe card is interactive and serves as a gateway to a dedicated page, offering detailed information about the recipe. For a streamlined browsing experience, the page is paginated, displaying eight recipes per page for user convenience.

![All Recipes Page](veggienosh/static/images/readme/all_recipes.png)

### The Single Recipe Page
Upon selecting a recipe card, the user is directed to the detailed Single Recipe page. This page comprehensively presents all pertinent details of the chosen recipe, including its title, a full description, the category and dish type, dietary categorization, serving size, total cooking time, the author's name, a list of ingredients, step-by-step directions, and a visual representation through a recipe image. In the absence of a user-provided image, a default placeholder image is displayed.

For recipe authors, the page offers additional functionality with 'Edit' and 'Delete' options, allowing for straightforward navigation to the respective editing and deletion functions for their recipes.

![Single Recipe Page](veggienosh/static/images/readme/single_recipe.png)

### The Registration Page
The registration page on VeggieNosh is meticulously crafted to ensure user accounts are created with robust security measures. Users are required to provide a "username," "password," and a subsequent "confirm password" entry. To safeguard accounts, usernames must be distinct and are verified for uniqueness against existing ones within a character range of 3-15. Passwords follow the same character length requirements and, for security reasons, cannot be identical to the username.

Additionally, the system is sensitive to accidental white spaces within entries — an error message will alert the user if any are detected to prevent login complications. Passwords are securely hashed to protect user information.

If the registration criteria are not met, users are promptly notified through clear error messages to adjust their input accordingly. Following a successful registration, the user is directed to the home page with a confirmation notice, and a link for existing users to log in is conveniently placed at the bottom of the form for easy access.

![Regiatration Page](veggienosh/static/images/readme/register_form.png)

### The Login Page
The login page of VeggieNosh presents a streamlined form with fields for the "username" and "password," facilitating a smooth sign-in process for returning users. Authentication occurs through a verification check where the entered credentials are matched against secured records in the database. Upon successful login, users are seamlessly redirected to the home page with a confirmation message of successful access. Should there be any discrepancies in the input, users are promptly alerted with clear notifications to rectify their login details.

For enhanced security and to prevent login errors, the form is designed to disallow any accidental white spaces in the username and password fields. This measure ensures that user credentials are entered correctly and maintains the integrity of the login process.

Additionally, those new to VeggieNosh will find a convenient link to the registration page below the form, offering an easy transition for users looking to create an account.

![Login Page](veggienosh/static/images/readme/login_form.png)

### The Logout Page
For logged-in users, selecting the "Exit Kitchen" button effectively ends their current session. This action will redirect them to the homepage, where they are greeted with a friendly "See you soon, Veggie Chef!" message.

![Logout Page](veggienosh/static/images/readme/logout_page.png)

### The Account Settings Page
Within the Account Settings page, users are greeted by their personalized avatar, cleverly generated based on their initials, adding a touch of customization. This is accompanied by a welcoming message and easy access to key account management features. The page provides three intuitive buttons for essential account updates:

- "Spice Up Username" to modify their display name,
- "Refresh Password" to ensure ongoing account security,
- "Shut Kitchen Down" for the option to conclusively deactivate their presence on the site.

These controls are intuitively laid out, guiding users smoothly to the corresponding actions with ease and professionalism.

![Account Settings Page](veggienosh/static/images/readme/account_settings.png)

### The Change Username Page
## Change Username Functionality

The 'Spice Up Username' feature is designed to empower registered users with the ability to update their username while maintaining a high standard of security. The system performs a thorough check to ensure the new username is not already taken, including variations with different capitalizations to prevent impersonation or confusion. Your current username is conveniently displayed above the entry field for easy reference.

Adjacent to the new username field, an informative question mark icon can be found. Hovering over this icon displays the username requirements, assisting users in choosing an acceptable new identifier. Following a successful username change, for enhanced security, users are redirected to the login page to sign in with their new username. Should a user decide against modifying their username, a 'Retreat' button is provided, offering a straightforward return to the Account Settings page without making any changes.

![Change Username Page](veggienosh/static/images/readme/change_username.png)




### The 404 Error Page
The 404 error page displays the sites name as a title. This also acts as a link back to the home page. Within the page there is a sorry message explaining to the user that there has been an error directing them to the page they were looking for. The user can click on Home button or title to redirect themselves to the home page.
![404 Page](documentation/features/404-page.png)


### The 500 Error Page
The 500 error page displays the sites names as a title, which also acts as a link back to the home page. Within the page is an error message that tells the user sorry there seems to be an internal server error. The user can click on Home button or title to redirect themselves to the home page.
![500 Page](documentation/features/500-page.png)


## Features to Implement in the future
- Additional features that could be added to the website in the future include:
   * 
## Accessibility
Throughout coding this site I kept accessibility in mind, to ensure that the website is user friendly for any user. I did this by:

  * Using semantic HTML.
  * Using descriptive aria labels for all links.
  * Providing information for screen readers when using icons - such as footer icons.


[Back to top](#)


## Issues and Bugs


## Technologies Used

The following technologies were used in the development of the website:

### Main Languages Used
- HTML5
- CSS3
- JS 

### Frameworks, Libraries & Programs Used
- [Bootstrap 5.3.0](https://getbootstrap.com/) 
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design phase of the project.
- [GitHub](https://github.com/) was used to store the project after pushing.
- [Google Fonts](https://fonts.google.com/) was used to import the font "Roboto" into the style.css file. This font was used throughout the project.
- [Font Awesome 6.3.0](https://fontawesome.com/) was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [jQuery](https://jquery.com/) A JavaScript library.

- [Am I Responsive?](https://ui.dev/amiresponsive) was used in order to see responsive design throughout the process and to generate mockup imagery to be used.
- [Favicon](https://www.favicon.cc/) was used to create a favicon to help users quickly identify a website when multiple tabs are open or when searching through bookmarks.
- [Visual Studio Code](https://code.visualstudio.com/download) was used to create files pages and produce the code for the project.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) was used during the testing phase to test the responsiveness of the site and to check for any bugs.
- [TinyPNG](https://tinypng.com/) was used to compress images.
- [JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) a google chrome extension to enable you to view JSON as raw data or parsed.


# Testing
The website was tested thoroughly to ensure it is fully functional and user-friendly. The testing phase involved manual testing on different devices and browsers.

Testing information can be found in a separate testing [file](TESTING.md).


## Deployment
The website was deployed on GitHub pages.

### Deploying on GitHub Pages
To deploy the website on GitHub Pages, the following steps were followed:
1. Create a new repository on GitHub
2. Add the necessary files to the repository
3. Go to the settings page of the repository and scroll down to the GitHub Pages section
4. Select the main branch and the root folder, then click save
5. The website will now be live at the URL provided in the GitHub Pages section

### Cloning the repository
You can clone the repository by following these steps:
1. Go to the repository on GitHub.
2. Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
3. Open a GitBash terminal and navigate to the directory where you want to locate the clone.
4. On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process.

### Forking the repository
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:
1. Go to the  repository on GitHub.
2. Click on the 'Fork' option towards the top left of the page.
3. Click the dropdown button and click 'create a new fork'.
4. This will bring up a page with details of the repository, fill in boxes as required.
Click 'create fork'.

## Credits
The website was built by the developer. The webpages use images from [Freepik](https://www.freepik.com/), icons from [Font Awesome](https://fontawesome.com/) and [Favicon](https://www.favicon.cc/).

### Content

- Some of the text used in the the various pages were borrowed and adapted from various sites, listed below.

  * 

### Media

- Background imange was sourced by [Freepik](https://www.freepik.com/) free library.
- 

### Code

The developer consulted multiple sites in order to better understand the code they were trying to implement. For code that was copied and edited, the developer made sure to reference this with the code. The following sites were used on a more regular basis:

- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [Medium](https://medium.com/) 


[Back to top](#top)

## Acknowledgements

I want to express my deepest appreciation to my mentor, Seun, for her steadfast support and invaluable insights throughout this journey. I also thank the CI Slack community for their useful advice and suggestions, and to Peter for his tutoring.

[Back to top](#top)

