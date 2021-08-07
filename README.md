Media content
[Index Image](https://news.sky.com/story/puppy-love-dating-site-for-pedigree-dogs-10487944)

superuser credentials: username:alisonclarke, password:6themayne

# MileStone Project Four
## Dog Dating Website

This project is a simple and responsive design to allow users to easily search, navigate to find new hikes and also to share reviews of hikes that the user may have already completed. The key features of each hike are broken down for quick and easy comparison. Users can also search hikes, locations are available and an email contact service is provided for any concerns or questions.  

## Ux
### Strategy

The basic strategy behind this application was to create a simple and easy to navigate where users could search for hikes in their area or selected county, explore the hikes themselves and then leave a review and recommendations for future hikers. The objective was to create a community for hike lovers to share and recommend the best places or even to avoid. 

**User Stories**

As a user of this application: 

* I would like to search for local hikes.
* Read reviews and recommendations from other users.
* See the location of the hikes.
* See the difficulty of the hikes
* Find information about the distance and amenities such as parking. 
* I would like to be able to leave reviews and add my own recommendations. 
* Be able to contact someone about any issues with any of the content or the hikes. 
* Easy to use on desktop and mobile.
* Simple design with no complicated format. 


### Scope
The specifications and requirements for the site to adhere to the user stories include:
* A search bar to easily find the hike you're looking for
* A form to easily add new hikes
* A contact page for the user to reach out to the site creator.
* Links to social media accounts for more content.
* A link to google maps with the location of the hike 
* A single page with the break down of the key features of the hike such as difficulty and duration. 
* A log in and out function so users have their own page of reviews that they have left.


### Structure
The site is linked with the MongoDB database to allow the user to easily obtain new information correlating with the selected hike. The user can filter through using the search bar and then click each individual hike for more detailed information. The EmailJS functionality makes it easier for the user to make contact.  And the location of the hikes is easily found with the google maps link associated with the hike

### Skeleton
The skeleton of the site was designed to be clean and simple and easy to navigate. The information was largely displayed in bullet point form so the user wasn’t overloaded with information. The user can navigate to a single detail page for the hike for added description and location. The users profile link, login and logout functions, add hike functionality are all displayed in the navigation bar. The navigation bar is also responsive to all screens weather on mobile, tablet or desktop. The card panels are displayed on the main page or users can also filter through using the search function. The skeleton mock ups were roughly done on [Balsamiq WireFrames](https://balsamiq.com/) . 

[Home Page](wireframes/home_page.png)

[Add/Edit Page](wireframes/add_edit_page.png)

[Contact Us Page](wireframes/contact_us.png)

[Hike Detail Page](wireframes/detail_page.png)

[Login/register Page](wireframes/Login_register.png)

[User profile](wireframes/users_profile.png)


### Surface
The surface of the site should be clean and simple. All the content is well spaced out and not overloaded with graphics and animations. Easy to follow and one main background image with hiking imagery.


## Features
### Existing Features
* Easy, simple design to allow for seamless navigation.
* Hike detail section to see key features of hike in bullet points.
* Ability to customize hike details and add any extra relevant information. 
* Users have their own profile which they can register and create their own password.
* Hikes created by the user can be deleted using the delete hike button and added new hike using the “add new hike".
* The user can contact the site creator directly by email. EmailJS sends the designated email address to let them know about the query. A screenshot of the recieved image is here [Email correspondence]()
* Location is available through google maps API to compliment the key features of hike om details page.


### Features Left to Implement

* Adding in the messaging functionality to enable users to direct message each other. (I started to write the code but unfortunately ran out of time)
* Use the email functionality in order to send emails from the account. 

## Technologies Used

1. CSS programming language
2. HTML programming language
3. Javascript Programming language.
4. [Bootstrap](https://getbootstrap.com/)
* To create a responsive structure for the website. 
5. [Balsamiq wireframes](https://balsamiq.com/wireframes/)
* used to create mock ups of what the site will look like
6. [Google Font](https://fonts.google.com/)
* Was used to style the fonts used in the website
7. [Gitpod](https://gitpod.io/workspaces/)
* To build and develop code
8. [w3schools](w3schools.com)
* To help with formatting and styles.
9. [Stackoverflow](https://stackoverflow.com/)
* The forums were useful for styling and functionality issues.
10. [HTML Formater](https://www.freeformatter.com/html-formatter.html#ad-output)
* To beatify HTML code
11. [W3C validator Service](https://validator.w3.org/#validate_by_input)
* To validate HTML code
12. [W3C CSS validator service](https://jigsaw.w3.org/css-validator/validator)
* To validate CSS code
13. [Python code validator](http://pep8online.com/))
* To validate Python code
14. [JQuery](https://jquery.com/)
* To add Javascript functionality
15. [Javascript Validator](https://jshint.com/)
* To validate Javascript code
16. [Jinga templating language](https://jinja.palletsprojects.com/en/3.0.x/)
* To help extend templates and iterate through objects. 
18. [Stripe](https://stripe.com/ie)
* To make the subscription payment possible
19. [Django](https://djangopackages.org/)
* Python framework for building the project.
20. [Gunicorn](https://gunicorn.org/)
* A Python WSGI HTTP Server to enable deployment to Heroku.
21. [Psycopg2](https://pypi.org/project/psycopg2/)
* Enable the PostgreSQL database to function with Django.
22. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
*  To style Django forms.
23. [Pillow](https://pillow.readthedocs.io/en/stable/)
* Saving image file formats
24. [Heroku](https://www.heroku.com)
* Host the project.
25. [AWS S3 Bucket](https://aws.amazon.com/s3/)
* Store static and media files in prodcution.
26. [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* Compatibility with AWS.
27. [SQlite3](https://www.sqlite.org/index.html)
* Development database.
28. [PostgreSQL](https://www.postgresql.org/)
* Production database.
## Testing

The HTML was checked using the [W3C validator Service](https://validator.w3.org/#validate_by_input).
The CSS was checked using the [W3C CSS validator service](https://jigsaw.w3.org/css-validator/validator).
The Javascript was checked using the [Javascript Validator](https://jshint.com/).
The Python was checked using the [Python code validator](http://pep8online.com/).


Manual testing was carried out to ensure the site carries out the intentions of the user stories.

##### Nav bar
* Displays navigation elements according to user. If session isn’t a user it won’t display profile, add hike or logout element. The appropriate login or register elements appear. 
* Responsive to drop down menu on smaller screens. 

##### Footer
* Social links animation works on hover.
* Socail links open to seperate tab. 

##### Search bar
* Filters counties, and hike names correctly.
* Flash message appears if no results are found
* Reset button brings user back to home page if clicked. 

##### Feature Wall 
* Displays hike reviews created by all users. 
* Delete and edit buttons appear for those hikes which were created by the user.
* Clicking on specific hike brings the user to indiviual detail page. 

##### Hike Detail Page
* The correct hike details populate the key features field.
* The Google maps iframe loads to the correct location of the hike using the hike name and county as parameters for search. 
* The description correctly populates underneath the Google image. 
* If the user is the creator of the review the edit and delete buttons appear at the bottom to link to the edit delete functionality. 

##### Delete function
* When delete function is called a warning message appears to confirm deletion.
* If cancelled the user is brought back to page they were on.
* If deleted, a flash message appears and user is returned to page they were on. 
* Object Id is successfullly removed from the database

##### Edit function
* The form pre populates with the information from the hike id it was on. 
* The drop down menu populates with the counties from the counties collection from the database. 
* If edited, a flash message appears and user is returned to their profile page. 
* Object ID is succesfullly updated in the database.

##### Add hike function
* The drop down menu populates with the counties from the counties collection from the database. 
* If added, a flash message appears and user is returned to their profile page.
* Object ID is succesfullly added in the database.

##### Login/Logout and Register functionality
* Flash messages appear to update the user that they have been either logged in, logged out, newly registered or if the username or password is incorrect. 
* If logged in the user is directed to their profile page
* When logged out the session user is removed and is redirected back to login page. 

##### Contact Page
* Social links animation move on hover
* Once form is filled in and send message is clicked, there is a message displayed directly after to acknowledge that the email has been sent. An email was recieved by the creator and the correspondence is [linked here](emailJS/image/emailJS_screenshot.jpg).

The project was also tested on multiple browsers (Chrome, Microsoft edge, Internet Explorer, and Firefox) and I used the Google Chrome's developer tools to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness. 



#### Bugs 

## Deployment

The source code for this website was deployed and stored in a GitHub repository while the website application is hosted by Heroku. The two are linked so any new commits or pushes to GitHub's master branch are also updated on the Heroku hosting service. AWS was also used to store media and static files. 
Link to Heroku live site is [here](https://dating-dogs.herokuapp.com/).

### Heroku Cloud
Heroku service allows for the deployment of our app as a live website, below are the steps required to host a project:

##### Create a new app linked to Github and connecting to SW3 bucket:
* On Heroku website create a user account as required.
* Once registered, click "New" in the top right and "Create App" from the dropdown.
* Choose a name and region and then create app button.
* In the Resources, within Add-ons searched Heroku Postgres, chose Hobby Dev - Free version. 
* In Settings click on Reveal Config Vars button, and copy the value of DATABASE_URL.
* Then back in Gitpod, install psycopg2 and dj_database_url. And pip3 freeze > requirements.txt to store the new requirements. 
* In settings.py and add import dj_database_url and update DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))} 
* Run makemigrations, followed by migrate to update migrations to progres DB
* Create a new superuser
* Returned to terminal window and ran sudo pip3 install gunicorn and added to requirements.txt
* Created a Procfile using the following command: echo web: gunicorn ms4.wsgi:application
* Go back to Heroku and select the "Deploy" option. Under "Deployment method", select the "Github: Connect to Github" option.
* Type in the repository which you want to host and search. 
* Once connected, select "Choose branch to deploy" and choose master. Then, click the "Enable Automatic Deploys" button which will enable automatic updates to heroku app.
* Click "Deploy branch".
* The app should now be successfully deployed and any github pushes should also be updated to the heroku app. 
* Log into Amazon AWS, go to S3 and create a new S3 bucket.
* In Gitpod, install django-storages and install boto3. Went to settings.py and added storages to INSTALLED_APPS.
* Updated enviroment variables in settings.py fie for the AWS bucket and access keys.
* Create custom_storage.py
* Update allowed hosts in settings.py to allow for heroku url to run





##### How to clone the repository:

* From the GitHub dashboard, chose the repository you wish to clone.
* Click the green “Code” button.
* Choose the “Clone with HTTPS” clipboard icon.
* Open Git Bash and change the working directory to the location you would like the clone to be.
* Type git clone, and pass the URL you have copied. (Should be in the format $ git clone https://github.com/username/repository.) and click "Enter".

##### Running the application locally:
* Clone the repository as shown above.
* Install the necessary libraries specified in the requirements.txt.
* Create a new file named env.py and add your variables to it.
* Create a gitignore file and include env.py so the information is not passed to the master branch.
* In your manage.py file, 'Import' your env.py file.
* Using 'python3 manage.py' in the command line you can run the project.

#### GitHub

A repository was created on GitHub and Gitpod was used to write the code. The code was commited and pushed to Github regularly to ensure it was saved. The GitHub repository was then deployed to GitHub pages by:

1. Logging into GitHub
2. Selecting repositories and then Dating_dogs.
3. Then select settings from the top menu bar.
4. Under GitHub pages
5. Under source, select master branch.
6. The website is now deployed and a link appears for the deployed site.
7. This [link](https://github.com/aliclarke206/datingdogs.git) can now be cloned and run locally.

## Credit
* The project's code was developed by following the Code Institute tutorials for the Boutique Ado Django Mini-Project, and customised to meet the requirements of my project.

### Content
 

### Media
#### Image
The source for the background images were from the following stories
* Media content
[Index Image](https://news.sky.com/story/puppy-love-dating-site-for-pedigree-dogs-10487944)


### Acknowledgements
Also my mentor, Brian Macharia for helping me along the way!

The tutor support for always being on hand when needed. 