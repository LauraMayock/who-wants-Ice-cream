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
    * [Manual Testing](<#manual-testing>)
    * [Known bug](<#known-bug>)
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



## order receipt
* At the end of the ordering process an order slip is printed to allow for the making up of the order and the taking of payment.
<img src="https://i.ibb.co/qkQJn5Z/order.png" alt="order receipt"></a>


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

* [PEP8 online validation tool](http://pep8online.com) was used to validate code. Although quite a few errors showed up all were easily fixed.

<img src="https://i.ibb.co/K9z8KF7/validation.png" alt="validation" ></a>


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
|             | wrong input |                  |
| :---------: | :----------:| :--------------:
| free        | yes         | ✔               |
| sprinkles   | No          | ✔               |
|             | wrong input | ✔               |
| :---------: | :----------:| :--------------:
|             | yes          | ✔               |
| 1 scoop     | wrong amount|  X                |
|             | wrong input | ✔                |
| :---------: | :----------:| :--------------:
|             | yes          | ✔               |
| 2 scoop     | wrong amount|  X               |
|             | wrong input |  ✔               |
| :---------: | :----------:| :--------------:
| :---------: | :----------:| :--------------:
|             | yes          | ✔               |
| 2 scoop     | wrong amount|  X               |
|             | wrong input |  ✔               |
| :---------: | :----------:| :--------------:

## Known bug 

* At present the user is able to imput a number higher than 6.
Obviously this is not ideal and with more time I would like to have amended this error.

<img src="https://i.ibb.co/MpndQ0Y/Error-when-chooseing-over-7.png" alt="know bugs"></a>

## Bugs Fixed

## Printing flavours by name 

* I had trouble at first trying to find a way to convert the flavour numbers chosen by the customer back to the flavour names.
  I tried to achieve this in a few different ways. Originally I tried to use the number the user inputted to select the flavour name on gspread but as I had the flavour list already linked to the keyword flavour using the below code it seemed cumbersome way.

<img src="https://i.ibb.co/2gxjP3g/gspread-1.png" alt="gspread-1 information"></a>

* Using the flav-list keyword I used a for loop that would append the flavour name to the customer_order global variable but this would only print one favour to the order receipt. 
* In the below example you can see that although there were two scoops chosen, flavours 4,5 only one flavour name is shown. 
<img src="https://i.ibb.co/Qry3TF7/not-listing-flavours.png" alt="know error with flavours">

* In creating a fuction that would take the users number choices and use a for loop to run them through the for loop and append them to new_choice = [] allowed me to print all of the users ice choices by name in the order- receipt. 

<img src="https://i.ibb.co/ZNftCb7/flav-choice.png" alt="flav-choice"></a>

## Sprinkles in a loop

* The below is a snipping tool showing a loop where the user would place their order and choose if they wanted sprinkles, the order slip would be printed but the terminal would then request if they would like sprinkles again. This was caused by me calling the function sprinkles at the end of the code. Once remove this amended the bug.

<img src="https://i.ibb.co/znN4qjY/sprinkles-loop.png" alt="sprinkles-loop"></a>

## Price updating

* Originally I was using the keyword append to save the price to be called in the order-receipt function. But I the customer chose sprinkles the price would not be added to the price of the ice cream, instead it was shown in conjunction with it. In the end I found that updating the price variable when needed using the = sign was the most straightforward and effective way.

<img src="https://i.ibb.co/02zK1HQ/price-update.png" alt="price-update"></a>

## Updating requiremnets file

* After adding new liberys to my github I found that the Hekuro terminal was not supporting the amendments. After much research I came to the conclusing that this was because i did not update the requirments file in my github workspace using 

pip freeze > requirements.txt

[Requirements file update](https://learnpython.com/blog/python-requirements-file/#:~:text=It%20is%20also%20possible%20to%20upgrade%20everything%20with,%3E%20requirements.txt%20to%20update%20the%20Python%20requirements%20file.)

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
* [Inspiraation](https://github.com/shahid129/my-sub-my-way)
* [W3school for Date and time print ](https://www.w3schools.com/python/python_datetime.asp)
* [python typing effect and clear screen](https://www.101computing.net/python-typing-text-effect/)
* [patorijk.com banner creator](https://patorjk.com/software/taag/#p=display&c=bash&f=ANSI%20Shadow&t=The%20Inside%20Scoop)
* [Stack Overflow](https://stackoverflow.com/)
* [w3school](https://www.w3schools.com/)
* [Basis of READ.ME](https://github.com/LauraMayock/motherandbaby/blob/main/README.md)


* [Acknowledgements](<#acknowledgements>)
This site, was designed and developed in conjunction with the Full Stack Software Developer Diploma course (eccommerce) at the Code Institute. I would like to thank my class facilitator, the members of our class, the Slack community and Code Institute for all their support.







