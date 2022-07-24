## Deployment

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