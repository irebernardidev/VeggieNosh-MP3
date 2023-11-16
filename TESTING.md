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
- [script.js](documentation/testing/validation/jshint.png)

------
#### Python Validator

To ensure that my code adheres to PEP8 guidelines, I am utilizing the [pycodestyle package](https://pypi.org/project/pycodestyle/) within my (IDE).

- [run.py](documentation/testing/validation/run_pep8_validator.png) - No errors or warnings.
- [init.py](documentation/testing/validation/init_pep8_validator.png) - No errors or warnings.
- [forms.py](documentation/testing/validation/forms_pep8_validator) - No errors or warnings.
- [routes.py](documentation/testing/validation/routes_pep8_validator) - No errors or warnings.

------
#### Lighthouse

I employed the Lighthouse feature in Chrome Developer Tools to evaluate the website's performance, accessibility, adherence to best practices, and SEO. While the resulting scores were good for most pages, some were not quite at the level I had hoped for. Enhancing these aspects will be a key focus in my upcoming implementation efforts, as I aim to elevate the overall quality and user experience of the website.

**Home Page**
- [Home Page Desktop](documentation/testing/validation/home_lh.png)
- [Home Page Mobile](documentation/testing/validation/home_mob_lh.png)

**All Recipe Page**
- [All Recipe Page Desktop](documentation/testing/validation/all_rec_lh.png) 
- [All Recipe Page Mobile](documentation/testing/validation/all_rec_mob_lh.png)

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
