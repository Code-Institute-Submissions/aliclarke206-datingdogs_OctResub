
# MileStone Project Four
## Dog Dating Website

### About
Welcome to Dating Dogs, a webapp to help dogs find love! This is a Python app using Django, and Email JS to produce a social media style application.

Dating Dogs currently brings users together and allows them to get in contact with the pups they love! The application lets the users create a profile that allows them to add their dogs’ details, add photos, let other users know when the next walk with their dog is happening through blog posts, and access the contact information of fellow pooches. The site offers the additional functionality; reset paasswords,reporting other users, contact us, editing and deleting blogs as well as their profiles,and backend validation. Please look at the features section for a more detailed description. The application has a lot of room for growth and a list of future features to implement.

This project is a simple and responsive design to allow users to easily search, navigate to find new dates for their dogs. Like a playdate but for dogs. It allows users to search through different categories, locations, ages etc and to leave blog posts so other potential dog owners can arrange pooch playdates. 

## Ux

The overall goal of the website is to provide visitors with the ability to view other users pet profiles and gain access to their contact details or to blog posts to view any upcoming puppy playdates. 

Visitors can can view a brief picture of the dogs on the dite but need to subscribe and login to have access to their full profile with contact info and to the blog posts. 


### Strategy

The basic strategy behind this application was to create a simple and easy to navigate app where users could search for other dog dates in their area or selected county. The objective was to create a community for dog lovers to set their pets up with a social life. I have created a playmate finding service dedicated to human’s best friend.

**User Stories**

As a new user of this application: 

* I would like to find out what the site is about and how it works
* I would like to see if the site is for me without registering
* I would like to easily register

As a new user of this application: 

* I would like to search for dogs with different criteria.
* I would like to be able to sign in and out easily.
* See the location of the dogs.
* See the breed of the dogs
* See the age.
* Find information about them from their description.  
* Be able to contact someone about any issues with any of the content or the dogs. 
* Easy to use on desktop and mobile.
* Add dog details, edit and delete details.
* View posts about potential playdates. Also add, edit and delete my own posts.
* Be able to search for other dogs based on location, breed or key words in description

**Site owner Stories**
* A self sufficent site where users pay a one off subscription to enable them to upload their profile, search through other profiles and view other dog lovers playdaye posts.
* Low maintainance as automatic emails, updates and messages are enabled to support the user.
* Potential to incorporate adds in the future for extra revenue. 

### Scope
The specifications and requirements for the site to adhere to the user stories include:
* A search bar to easily find the dog you're looking for or in nearby locations.
* A form to easily add new dogs and edit or delete if you are the user.
* Links to social media accounts for more content.
* A single detail page with more infromation including contact information about the dog.
* A log in and out function so users have their own page.
* Stripe functionality to allow for easy sign up to a one of subscription fee.
* A blog post page to allow users to post about dog meet ups and view other users posts.


### Structure
The site used the SQlite3 database in development and PostgreSQL in production to allow the user to easily obtain new information correlating with the selected dog. The user can filter through using the search bar and then click each individual dog for more detailed information. 

## Information Architecture
During the development phase of the project, I used sqlite3 database which was installed with Django. For deployment/production, a PostgreSQL is provided by Heroku. 

The following apps were created for this website - Dogs, Blog, Subscribe, Home, Profiles.
The User model is provided by Django as a part of defaults django.contrib.auth.models.

* The Dogs App contains the following Models - Dog and Breed.
* The Subscribe App contains the following Model - Subscription
* The Blog App contains the following Model - Post
* The Profile App contains the following Model - Profile

The following is the websites ERD (Entity Relationship Diagram) -

![ERD Image](/media/ERD.png)

### Security
* Username - The username can only exist once in the database and at registration the username is checked against the current usernames

* Passwords - The password must contact a mixture of uppercase and lowercase letters, digits, and a special character. It must be at least 8 characters long. The password is salted and hashed using from werkzeug.security when it is collected from the user.

* Login - At login, the user must match their username/email to the correct password. It will check to make sure that the password the user enters meets the check_password_hash. If successful, the user will be assigned a session cookie. If the user is unsuccessful then they will be notified that one of the fields is incorrect. I have chosen not to notify the user which field is incorrect so that their details remain private and are harder to guess.

* Session Cookie - The user is assigned a session cookie on successful login. This allows the user to navigate their own profile, add edit and delete information. The user is not able to make any changes to pages that their session cookie does not match the username.

* Reset Password - If the user tries to reset their password, they are sent an email to the email address we have on file. They are sent a random string temporary password and a link to the reset password page. Once they have clicked the link, they will need to enter the username attached to the email address as an extra measure.


### Skeleton
The skeleton of the site was designed to be clean and simple and easy to navigate. The information was largely displayed in bullet point form so the user wasn’t overloaded with information in the "about us" and "how it works" links. The user can navigate to a single detail page for the dog for further descriptions and contact info given by their owner.  The drop down menu provides the user with links to their profile, login and logout functions, add dog and the dog blog. The user is either directed to log in or subscribe. Once the user has paid the subscription they are then lead to verify and register their email. Once that's complete they can then add a dog to the site. The navigation bar is also responsive to all screens weather on mobile, tablet or desktop. The card panels are displayed on the main page or users can also filter through using the search function. The skeleton mock ups were roughly done on [Balsamiq WireFrames](https://balsamiq.com/) . 

[Home Page](media/index_page.png)

[Add/Edit Page](media/add-delete-page.png)

[Dog detail](media/dog_detail_page.png)

[All dogs](media/all_dogs_page.png)




### Surface
The surface of the site should be clean and simple. All the content is well spaced out and not overloaded with graphics and animations. Easy to follow and one main background image with dog imagery.
![ColourScheme Image](/media/colorscheme.png)


## Features
### Existing Features
* Easy, simple design to allow for seamless navigation.
* dog detail section to see key features of dog in bullet points.
* Ability to customize dog details and add any extra relevant information. 
* Users have their own profile which they can register and create their own password.
* dogs created by the user can be deleted using the delete dog button and added new dog using the “add new dog".
* Social links in footer available for more content
* verification email when signing in
* stripe to pay for subscription
* contact us page so users can email any issues or queries with the site.
* Blog psot for users to be able to display messages to other users about puppy playdates or just general dog owner reccomendations and discussions.


### Features Left to Implement


* A lot more could be done to this project. More testing needed to be done and better naviagtion for the user and better UX. 
* Adding a direct messaging functionality to enable users to direct message each other instead of leaving contact details on the dog profile page or communicating via the blog. 
* Could add some affiliated products to the site for your dog as an added revenue stream. 
* Ablitiy to send likes to other dogs and make it a bit more interactive.
* I would also like to render the Users dog detail page and blog posts to their User Profile page.
* Add a loactaions tag if the user is posting a blog post about a playdate. 

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
13. [Python code validator](http://pep8online.com/)
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
29. [EmailJS](https://www.emailjs.com/)
* To enable email service for the contact page. 


## Testing

The HTML was checked using the [W3C validator Service](https://validator.w3.org/#validate_by_input).
The CSS was checked using the [W3C CSS validator service](https://jigsaw.w3.org/css-validator/validator).
The Javascript was checked using the [Javascript Validator](https://jshint.com/).
The Python was checked using the [Python code validator](http://pep8online.com/).


Manual testing was carried out to ensure the site carries out the intentions of the user stories.

##### Nav bar
* Displays navigation elements according to user. If session isn’t a user it won’t display profile, add dog, logout element, or dog blog. The appropriate login or register elements appear. 
* Responsive to drop down menu on smaller screens. 
* Use can sort by breed type age, breed or location.
* Search bar filtrs through locations names and key words that might be in the descriptions.

##### Footer
* Social links animation works on hover.
* Social links open to seperate tab. 
* Quick links section naviagtes users to how it works page, contact page and if the user is logged in, to the Dog Blog.

##### Search bar
* Filters through description, breed and location.
* Reset button brings user back to home page if clicked. 

##### All Dogs Wall 
* Displays image of dog and snippet of relevant information. 
* Delete and edit buttons appear for those dogs which were created by the user.
* Clicking on specific dog brings the user to indiviual detail page. 
* The sorting bar correctly orders the dogs by age, location, breed and name.
* also when using the sorting the correct number of dogs appears at the top. 

##### dog Detail Page
* The correct dog details populate the key features field.
* The description correctly populates underneath the image. 
* If the user is the creator of the dog, the edit and delete buttons appear at the bottom to link to the edit delete functionality. 

##### Delete function
* When delete function is called a warning message appears to confirm deletion.
* If cancelled the user is brought back to page they were on.
* If deleted, a flash message appears and user is returned to page they were on. 
* Object Id is successfullly removed from the database

##### Edit function
* The drop down menu populates with the breed from the breed collection from the database. 
* If edited, a flash message appears and user is returned to their profile page. 
* Object ID is succesfullly updated in the database.

##### Add dog function
* Ability to add image and url. 
* If added, a flash message appears and user is returned to their profile page.
* Object ID is succesfullly added in the database.

##### Login/Logout and Register functionality
* Flash messages appear to update the user that they have been either logged in, logged out, newly registered or if the username or password is incorrect. 
* If logged in the user is directed to their profile page
* When logged out the session user is removed and is redirected back to login page. 

##### Subscribe
* The subscribe page brings the user to a page to add details and credit card to allow the user to access the rest of the site.
* When tester card is used it successfully logs in the stripe account and webhook handler is successful.
* Error warnings  appear if the details entered don't meet the criteria. For example if the @ symbol wasnt used in the email section or if the form wasn't complete.

#### Webhook and Emails

Initially my webhook handelers were getting a error 401 message when I tried to test them but this was due to my local host not being public. Once the site was linked to the public heroku app the webhooks were successful and the charge is successful. 
Also when a user creates an account a verification email is successfully sent to the user to allow them to verify their account. 
![Confirmation email](/media/confirm_email_ss.png)


#### Blog
* View all blog posts' (visible to all users once logged in) renders the blog post templates and displays all available blog posts.
* Create Blog Post' (only available to logged in users) renders the create a blog post template with a form so the user can publish a blog post.
* Only authenticated users are allowed to publish and view blog posts. The Blog link in the dropdown menu and in the quicklinks footer only becomes available once a user is logged in. For non-authenticated users, the link does not appear. 
* Slice method on blog posts ensures that only 200 characters display on blog page with all the posts.
* Post displays correct date of users post and is ordering according to date.
* Superusers and 

### Contact Us
* Social media account links for user to each social media page.
* Able to send email to site using form and email successfully recieved from the back end. 
* Query selection successfully populates when clicked and displays relevant options. 
![EmailJS Image](/media/emailJS.png)

## About us Page
* All links bring user to relevant pages
* Media files display in order. During deployment there was some issues getting the media files from the new database but the issue was solved using the {{MEDIA_URL}} functionality.


The project was also tested on multiple browsers (Chrome, Microsoft edge, Internet Explorer, and Firefox) and I used the Google Chrome's developer tools to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness. 
Ran python3 -m flake8 for all problems to be displayed to fix a number of indentation errors and line lenght errors.



#### Bugs 
When submitting a blog post the user is able to pick any user name. Ideally the only user name available would be their own. 

## Challenges
Had trouble making migrations once the app was connected to Heroku. There was an error connecting to the DATABASE_URL. This is a known bug in Gitpod which was remedied by unsetting the DATABASE_URL in the command line. When I did this and pushed to github, it stopped deploying to Heroku. 


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
[About Us Background](https://www.freepik.com/vectors/logo)
[How it works images](https://members.tagalongdates.com/)


### Acknowledgements
Also my mentor, Brian Macharia for helping me along the way!

The tutor support for always being on hand when needed. 