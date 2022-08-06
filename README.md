<img src="https://i.ibb.co/FxY2gH5/welcome-screen.png alt=welcome-screen">

# **_Who wants Ice-cream - Portfolio Project 3 - Python_**
Who want Ice-cream is a command-line user interface providing the customer with the ability to order an ice cream cone or cup of choice. This project was built using Python.

You can view the live site here - <a href=" https://github.com/LauraMayock/who-wants-Ice-cream" target="_blank"> Who wants ice-cream? 
----
# Content

* [Objectives](<#objective>)
* [User Experience](<#user-experience-ux>)
    * [User](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Owner of site](<#Owner-of-site>)
    * [Flow Chart](<#flow-chart>)
* [Features](<#features>)
    * [Header](<#header>)
    * [Error message](<#error-message>)
    * [Tying effect](<#typing-effect>)
    * [Gspread](<#gspread>)
    * [prettytable](<#prettytable>)
    * [Receipt](<#receipt>)
* [Future Features](<#future-features>)
* [Technologies Used](<#technologies-used>)
* [Testing](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Accessibility Testing](<#accessibility-testing>)
    * [Manual Testing](<#manual-testing>)
    * [Bugs Fixed](<#bugs-fixed>)
* [Deployment](<#deployment>)
    * [To Fork the repository on GitHub](#To-Fork-the-repository-on-GitHub)
    * [To Clone the repository on GitHub](#To-Clone-the-repository-on-GitHub)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)



# Objective

The goal is to create an interactive site using a command line interface. It provides an automated ordering process for the user, allowing them to order their favourtie ice-cream.

[Back to top](#content)

# User Experience (UX)

## User
* As a user, I want a clear understanding of the purpose of the page and the ability to use it intuitively with its clear and thought-out design. 
* To have a clear layout and a clear understanding of what information is expected of me.
* To be prompted if my input is invalid. 

## User Stories
* I want a simple and interactive way to order my favourite ice-cream.
* I want clear guidance throughout.
* I want a receipt with my purchase. Giving a clear outline of my purchase and the cost.

## Owner of site
* This system automates the order process for simple orders freeing up staff to concentrate on taking payments and services for both the business and user.
* This allows for quicker delivery of service and allows staff to concentrate on orders with a higher monetary value.

## Flow Chart
Using the website [lucidchart](https://www.lucidchart.com/) The flow chart below gives a simplified layout of what I was hoping to achieve. The shapes highlighted by the yellow colour show the stages where the user will be asked for simple input. the red boxes symbolise the negative input or an invalid input. While the green shows a positive response from the user.

<img src="https://i.ibb.co/zhXVhNm/Blank-diagram-1.jpg" alt="Flow Chart">Flow Chart</a>

[Back to top](<#content>)

# Features

## Header
* Using [Patorjk](https://patorjk.com/) i created a simple logo for the shop.

<img src="https://i.ibb.co/y6wJZQH/logo.png" alt="logo"></a>

## Error messages

* By installing [Colarama](https://pypi.org/project/colorama/) i have added a red colour to any error messages to provide a visual warning to the user.

<img src="https://i.ibb.co/Gncdk03/Error-message.png" alt="Heading"></a>


## Typing effect

* I have addig a typerwriter effect by using libraries time,sys. Code sourced from [www.101computing.net](https://www.101computing.net/python-typing-text-effect/)
* This effect makes it a lot more reader friendly. 
* It gives the impressing of a more thoughtful automation process giving the system a more welcoming and customer focused feel.
* Os libary was also use to clear clutter from the screen to allow the user to focus on the question/desision at hand.

## Gspread

* The ice cream flavours have been saved on a google spread to allow the owner to amend the flavours easily. 


<img src="https://i.ibb.co/y0dpc9p/gspread.png" alt="gspread"></a>


## Prettytable

* I have used the library prettytable to create a user friendly viewing. 
* Ice cream flavours are outlined in a simple table form with a relating number that the user can use for quick decision making.

<img src="https://i.ibb.co/P94j8QT/ice-cream-flavours.png" alt="Prettytable"></a>

## Free sprinkles

* With every 3 scoops of ice cream the customer can choose to have free sprinkles.



## Reciept

* 

<img src=""></a>



[Back to top](<#content>)


# Future Features

* Expanding the menu available, adding ice lollies.
* To be able to order more than one ice-cream at a time.
* To utilise gspread by holding a stocklist of available products. That would update the system when there are out of stocks.

# Technologies used

* Python
* gitpod - Used to develop website.
* GitBash - Used to push repository to Github.
* HeroKu - Used host and deploy website.

## Framework/Packages Used

* os 
Used to clear the ordering screen.
* time and sys
Used to create a typewriter effect.
* gspread
Used to hold the icecream flavours
* google.oauth2.service_account and Credentials
Accessing the gspread.
* time date
To post on receipts.
* Prettytable
Used to display iceCream flavours.
* Colorama
Adding a red colour to the warning text.



[Back to top](<#content>)

# Testing

## Code Validation

* Both the CSS and HTML code was tested using W3 validation services. Each test came back with no issues highlighted.

<img src="https://i.ibb.co/nkPm19j/v3-CSS-valatation-test.png" alt="v3-CSS-valatation-test"></a>


## Manual Testing

* Testing user input

| Test        |     Input   | Desired outcome |
| :---------: | :----------:| :-------------: |
| Welcome     | yes         | ✔               |
|             | no          | ✔               |
|             | wrong input | ✔               |
| :---------: | :----------:| :--------------:
| cup/cone    | cup         | ✔               |
|             | cone        | ✔               |
|             | wrong input | ✔               |
| :---------: | :----------:| :--------------:
| How many    | 1           | ✔               |
| scoops      | 2           | ✔               |
|             | 3           | ✔               |
|             | wrong input |                  |
| :---------: | :----------:| :--------------:
| flavours    | 1 scoop     | ✔               |
|             | 2 scoops    | ✔               |
|             | 3 scoops    | ✔               |
|             | wrong input |               |
| :---------: | :----------:| :--------------:
| free        | yes         | ✔               |
| sprinkles   | No          | ✔               |
|             | wrong input | ✔               |
| :---------: | :----------:| :--------------:
| Sprinkles   | yes          | ✔               |
| 1 scoop     | no          | ✔                |
|             | wrong input |                  |
| :---------: | :----------:| :--------------:
| Sprinkles   | yes          | ✔               |
| 2 scoop     | no          | ✔                |
|             | wrong input |                  |
| :---------: | :----------:| :--------------:


* I have tested that this page works in the following browsers: Chrome, Edge, Safari and FireFox.
* I tested responsiveness in portrait form using the inspect function on google chrome, and it is recommended to play in this position. 
* I tested that the text is readable in all website areas and that each round decider shows as required in the right circumstances.

## Bugs Fixed

* Below are screen shots of some of the issues highlighted by devtools. 

<img src="https://i.ibb.co/bKGG1Hx/devtools-bug-javascript-link.png" alt="devtools-bug-javascript-link"></a>

* One of the above issues was a simple error with the link between the JavaScript page and HTML and was rectified easily.

* The second was highlighting an issue finding a Favicon. This was due to pre-saved software by Code Institue. When I installed a Favicon onto the site, it created another error because I had followed the steps on the Favicon website on how to install it, not knowing that this step was already preloaded.

* Issue with Modal

<a href="https://ibb.co/TTBMtH0"><img src="https://i.ibb.co/cvchQN8/devtools-bugs-modal-issue.png" alt="devtools-bugs-modal-issue" border="0"></a>

* This was due to the fact that i did not create a getElement between the modal button and Javascript. I did with the Modal itself but didnt recognise that it was needed for both.

* Show icon not defined

<img src="https://i.ibb.co/bsN96H8/devtools-bugs.png" alt="devtools-bugs"></a>

* The above error was caused by me not defining the element before using it in a function.

* The Favicon shown in the above image is the same issue discussed above.

* I used a seprate gitpod work space to work through and test code before implimenting it. This help grately to ensure that I didnt break any of the functions that I proviously implimended. 

* I aimed to add an option to play a round of 5 or 10 and then for the game to end showing an overall winner, but this caused a lot of issues, and due to time constraints, it had to be left for a future feature.

# Deployment

Before you deploy to Heroku, make sure to update any dependencies needed to run your app. A list of dependencies can be saved in the requirements.txt file. This is done automatically after adding the below code into the terminal and then do a git push. 

pip3 freeze --local > requirements.txt

1. Navigate to Heroku website and either sign in or click sign up to create a new account.

2. In your account dashboard click the Create new APP button.

3. Add a name for APP in the APP-Name field.

4. Select your region from the drop-down menu and click on Create APP button.

5. On the next page click on the Settings tab to adjust the settings.

6. Click on the "config vars" button and hide any sensitive files from being deployed.

7. In the field for key add the sensitive file name and in the value field copy the entire file from your workspace into this field and click add.

7. in the supply key field below this add PORT and 8000 into the value field. Then click on the "add" button.

8. Click on the ADD Buildpack button.

9. Select python buildpack and click save changes. Then click Add Buldpack button again but this time add node.js and save changes. Please ensure that you are adding them in this order as it may cause issues otherwise.

10. Navigate to the deploy section by using the deploy tab a the top of the screen, select Github and connect to your Github profile.

11. Search for your Github repo name by adding the name to the repo-name tab and click the search button.

12. When the search is complete, click on the connect button to the right of your repo name.

11. Now you can deploy the app automatically or manually. Automatically deploy will update the app automatically every time you push any changes to Github.

12. Once the build is successful, you can open the app by clicking Open App button in the top right corner. 

## To Fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the origional repository.

1. Log in to GitHub and locate the repository in question.
2. Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
3. Click this button to create a copy of the origional repository in your GitHub Account.

## To Clone the repository on GitHub

1. Click on the code button which is underneath the main tab and repository name to the right.
2. In the "Clone with HTTPS' section, click on the clipboard icon to copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to where you wan the cloned directory to be made.
5. Type git clone, and then paste the URL copied form GitHub.
6. Press enter and the clone of your repository will be created.




* [Credits](<#credits>)
* [Css background](https://codepen.io/P1N2O/pen/pyBNzX)
* [Javascript Jutorial source](https://javascript.tutorialink.com/rock-paper-scissors-game-using-javascript/)
* [Javascript Jutorial source 2](https://betterprogramming.pub/7-ways-to-code-rock-paper-scissors-in-javascript-4189a5e7e535)
* [Javascript Jutorial source 3](https://wierdlygoodcoder.github.io/rock-paper-scissors/)
* [modal tutorial](https://www.w3schools.com/w3css/w3css_modal.asp)
* [Css grid](https://www.youtube.com/watch?v=9zBsdzdE4sM&t=5s&ab_channel=WebDevSimplified)
* [Basis of READ.ME](https://github.com/LauraMayock/motherandbaby/blob/main/README.md)


* [Acknowledgements](<#acknowledgements>)
This site, was designed and developed in conjunction with the Full Stack Software Developer Diploma course (eccommerce) at the Code Institute. I would like to thank my class facilitator, the members of our class, the Slack community and Code Institute for all their support.







