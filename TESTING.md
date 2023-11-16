# VeggieNosh - Testing
![VeggieNosh](documentation/readme/am_i_responsive.png)
 
Find the final project here: [VeggieNosh](#)

## Contents
- [AUTOMATED TESTING](#automated-testing)
  - [W3C Validator](#w3c-validator)
  - [Javascript Validator](#javascript-validator)
  - [Python Validator](#python-validator)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Testing User Stories](#testing-user-stories)
  - [Full Testing](#full-testing)
- [BUGS](#bugs)
  - [Solved Bugs](#solved-bugs)
  - [Known Bugs](#known-bugs)

Throughout the entire development process, I extensively used Chrome Developer Tools for real-time testing and troubleshooting. I leveraged its console feature to ensure JavaScript code functionality and identify any issues.

To verify adaptability, I employed Google Chrome Developer Tools and Firefox's Inspector tool to check the responsiveness of each page across various devices and screen sizes. This rigorous approach ensured a seamless user experience on multiple platforms.

### AUTOMATED TESTING
#### W3C Validator
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

- [Home Page](documentation/testing/validation/home_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Footer Page](documentation/testing/validation/footer_validator.png)- No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Navbar Page](documentation/testing/validation/navbar_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Recipe Cards Page](documentation/testing/validation/cards_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Account Settings Page](documentation/testing/validation/account_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Add Recipe Page](documentation/testing/validation/add_rec_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [All Recipe Page](documentation/testing/validation/all_rec_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Base Page](documentation/testing/validation/base_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Change Password Page](documentation/testing/validation/change_pass_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Change Username Page](documentation/testing/validation/change_user_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Edit Recipe Page](documentation/testing/validation/edit_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Login Page](documentation/testing/validation/login_validator.png)- No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [My Recipe Page](documentation/testing/validation/my_rec_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Register Page](documentation/testing/validation/register_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Search Page](documentation/testing/validation/search_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [Single Recipe Info Page](documentation/testing/validation/single_rec_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [404 Error Page](documentation/testing/validation/404_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [500 Error Page](documentation/testing/validation/500_validator.png) - No errors, since it does not recognize Jinja2 templating language, it showed a couple of warnings.
- [CSS](documentation/testing/validation/css_validator.png) - No errors or warnings.

------
#### Javascript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.
- [script.js](documentation/testing/validation/jshint.png) - No errors or warnings.

------
#### Python Validator

To ensure that my code adheres to PEP8 guidelines, I am utilizing the [pycodestyle package](https://pypi.org/project/pycodestyle/) within my (IDE).

- [run.py](documentation/testing/validation/run_pep8_validator.png) - No errors or warnings.
- [init.py](documentation/testing/validation/init_pep8_validator.png) - No errors or warnings.
- [forms.py](documentation/testing/validation/forms_pep8_validator) - No errors or warnings.
- [routes.py](documentation/testing/validation/routes_pep8_validator) - No errors or warnings.

------
#### Lighthouse

I employed the [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?pli=1) feature in Chrome Developer Tools to evaluate the website's performance, accessibility, adherence to best practices, and SEO. While the resulting scores were good for most pages, some were not quite at the level I had hoped for. Enhancing these aspects will be a key focus in my upcoming implementation efforts, as I aim to elevate the overall quality and user experience of the website.

**Home Page**
- [Home Page Desktop](documentation/testing/validation/home_lh.png)
- [Home Page Mobile](documentation/testing/validation/home_mob_lh.png)

**All Recipes Page**
- [All Recipes Page Desktop](documentation/testing/validation/all_rec_lh.png) 
- [All Recipes Page Mobile](documentation/testing/validation/all_rec_mob_lh.png)

**Single Recipe Info Page**
- [Single Recipe Info Page Desktop](documentation/testing/validation/single_rec_lh.png)
- [Single Recipe Info Page Mobile](documentation/testing/validation/single_rec_mob_lh.png)

**Login Page**
- [Login Page Desktop](documentation/testing/validation/login_lh.png) 
- [Login Page Mobile](documentation/testing/validation/login_mob_lh.png)

**Account Settings Page**
- [Account Settings Page Desktop](documentation/testing/validation/account_lh.png)
- [Account Settings Page Mobile](documentation/testing/validation/account_mob_lh.png)

**Change Username Page**
- [Change Username Page Desktop](documentation/testing/validation/change_user_lh.png) 
- [Change Username Page Mobile](documentation/testing/validation/change_user_mob_lh.png) 

**Change Password Page**
- [Change Password Page Desktop](documentation/testing/validation/change_pass_lh.png)
- [Change Password Page Mobile](documentation/testing/validation/change_pass_mob_lh.png) 

**My Recipe Page**
- [My Recipe Page Desktop](documentation/testing/validation/my_rec_lh.png)
- [My Recipe Page Mobile](documentation/testing/validation/my_rec_mob_lh.png)

**Edit Recipe Page**
- [Edit Recipe Page Desktop](documentation/testing/validation/edit_lh.png)
- [Edit Recipe Page Mobile](documentation/testing/validation/edit_mob_lh.png)

**Add Recipe Page**
- [Add Recipe Page Desktop](documentation/testing/validation/add_rec_lh.png)
- [Add Recipe Page Mobile](documentation/testing/validation/add_rec_mob_lh.png) 

**Register Page**
- [Register Page Desktop](documentation/testing/validation/register_lh.png)
- [Register Page Mobile](documentation/testing/validation/register_mob_lh.png) 

**Search Page**
- [Search Page Desktop](documentation/testing/validation/search_lh.png) 
- [Search Page Mobile](documentation/testing/validation/search_mob_lh.png) 


------

### MANUAL TESTING

#### Testing User Stories


| Goals                 | How are they achieved?                                                                                                       | Image |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------|:-----:|
| **New/Unregistered User**   |                                                                                                                              |       |
| Search for recipes easily. | Upon selecting the "All Recipes" page, I am presented with an array of recipe cards, neatly arranged in rows with 8 recipes per page. Each card showcases the recipe's image, name, and a brief description. When I select a specific recipe card, I am seamlessly taken to a dedicated page for that recipe, which offers comprehensive details about the ingredients, preparation steps, and other relevant information.                                       | [All Recipes](documentation/readme/all_recipes.png)|
| Explore all site recipes. | At the top of the homepage, just above the display of recipe cards, there's a prominent "Explore Veggie Creations" button. A click on this button navigates to the "All Recipes" page, which offers a full view of the available recipes. On this page, there is also a search bar that enables users to enter specific search terms. This search feature is robust, capable of returning results from complete words or even from a mere few letters of a word, ensuring that users can easily find the recipes they're interested in. | [Explore Veggie Creations ](documentation/testing/explore_rec.png)[Search veggie recipes](documentation/testing/explore_rec2.png)|
| View complete recipes of interest.      | Selecting a recipe card allows any user, regardless of registration or login status, to access the complete details of the recipe.                                 | [Recipe Card](documentation/testing/card.png) [Recipe Card Info](documentation/testing/card2.png)|
| Intuitive navigation with clear Sign-Up.      | Navigation for guests who have not registered is facilitated by the availability of several links on the Navbar, specifically: Home, Browse Dishes, Enter The Kitchen, and Join VeggieNosh. Upon arriving at the landing page, new visitors will immediately notice the Join VeggieNosh and Login buttons, conveniently positioned at the upper right corner of the screen for easy access.                                     | [Navbar](documentation/testing/nav.png)|
| Understand the site's purpose and functionality.      | The homepage features a hero image that is thoughtfully complemented by a title and tagline, succinctly introducing the essence of the website to the user at a glance.                                | [Home/ tagline](documentation/testing/tagline.png)|
| **Returning/Registered User**   |                                                                                                                              |       |
| Quick access to Log In.    | If a user is not logged into an account, a login link is provided on the navbar.                                             | [Navbar](documentation/testing/nav.png)||
| View latest recipes.      | Upon selecting the "All Recipes" page, I am presented with an array of recipe cards, neatly arranged in rows with 8 recipes per page. Each card showcases the recipe's image, name, and a brief description. When I select a specific recipe card, I am seamlessly taken to a dedicated page for that recipe, which offers comprehensive details about the ingredients, preparation steps, and other relevant information.                                             | [All Recipes](documentation/readme/all_recipes.png)|
| Access account settings, personal cookbook, and other user-specific pages.         |  Once logged in, the user can navigate to the "Chef's Corner" via the link in the navbar. Here, they are presented with three choices: "My Veggie Recipes," which is a repository of the user's own recipes; "Whip Up a New Recipe," an area designed for the creation of new veggie recipes; and "Account Settings," where users have the ability to modify their username, password, or proceed with account deletion.          | [Chef's Corner](documentation/testing/chef_corner.png) [Chef's Corner Options](documentation/testing/chef_corner2.png)|
| Manage profile and recipes (create, edit, delete).       |       Once logged in, users can click on the "Chef's Corner" link in the navigation bar to explore three options. They can visit "My Veggie Recipes" to view all the recipes they have created, select "Whip Up a New Recipe" to craft a new culinary creation, or choose "Account Settings" to modify their username, password, or to delete their account. Additionally, within the "My Veggie Recipes" section, users have the ability to edit or delete any of their existing recipes, with changes reflecting both on the webpage and in the database.      | [User Account Settings Options](documentation/testing/account.png) [Change Username](documentation/readme/change_username.png)[Change Password](documentation/readme/change_password.png)[Delete Account](documentation/readme/delete_account.png)[Add Recipe](documentation/readme/add_recipe.png) [Edit/Delete Recipe Options](documentation/testing/rec_option.png)|
| Share recipes on social media. | Upon interacting with a recipe card, users are seamlessly transitioned to the individual recipe information page, where they can discover the full set of cooking instructions and ingredient lists. Adjacent to the recipe image on this page, there is a dropdown 'Share' button. A single click on this button unfolds a menu offering sharing options, including the ability to post the recipe page directly to WhatsApp and Facebook.              | [Share on Socials Option](documentation/readme/share.png)|
| Print recipes.   | When a user clicks on a recipe card, they are taken to the individual recipe information page, which contains the full set of instructions and ingredients for the recipe. Adjacent to the recipe image, on this detailed page, there is a print icon situated next to the share button. Clicking the print icon opens a new window, presenting the user with various printing options to conveniently print the recipe.           | [Print Option](documentation/testing/print_opt.png) [Print Window](documentation/testing/print_page.png)|
| Access a contact page for queries.       | Located in the footer of each page, amidst various social platform icons, users will find an email icon. This provides a convenient means for users to contact the website owner with any inquiries they may have. A single click on the icon will open the user's email client in a new tab, ready for them to compose their message.             | [Email Option](documentation/readme/socials_icons.png) [Email Window](documentation/testing/email_window.png)|
| **Administrative User**   |                                                                                                                              |       |
| All functionalities of a registered user. | The admin possesses the capability to perform all the functions that a registered user can execute.                                                              | `:---`|
| Manage my veggie recipes. | The description on the home page encourages new users to register for an account. A register link is displayed on the navbar if a user is not logged in. | `:---`|
| Edit or delete any site recipes.    | After successfully logging in, users have the opportunity to delve into the "Chef's Corner" by clicking on its link in the navigation bar. This section unfolds three choices, including the "My Veggie Recipes" area. Here, users are empowered to modify or remove their personal recipes. Any alterations made will be updated instantaneously on the website and synchronized with the database for consistency.          | `:---`|

------
#### Full Testing
Full testing was performed on the following devices:

- Laptop:
  - Macbook Air 2017 13 inch screen
- Mobile Devices:
  - iPhone 14 Pro.
  - iPhone XR.
  - iPhone 12 Pro.

Each device tested the site using the following browsers:

- Google Chrome
- Opera
- Firefox
- Edge
