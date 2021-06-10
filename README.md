# BizNet
A social network for job opportunities.  
  
  ![BizNet devices](https://user-images.githubusercontent.com/70586630/121528548-dd32cb80-c9fb-11eb-9daf-5b57e1da1650.png)


Webpage: https://.com/  
  
*Full Stack Frameworks project with Django stored in GitHub and deployed to Heroku.*  
  
# Table of contents
  
[The UX Framework (Strategy Plane)](#strategyplane)  
  * [Introduction](#introduction)  
  * [Goal](#goal) 

[User Stories (Scope Plane)](#ux) 

[Structure plane](#structureplane)  
  * [Typography](#typography)  
  * [Color](#color)  
  * [Interactive Design & Informative Architecture](#idandia)  


[Skeleton Plane](#skeletonplane)  
  * [The structure of the website](#skeleton)  
  * [The database structure](#database)  
  * [Recipe categories](#recipecat)  
  * [Recipe information](#recipeinfo) 
  
[Surface Plane](#surfaceplane)  
  * [Wireframes](#wireframes)  
  
[Features](#features)  
  * [Existing Features](#existingfeat)  
  * [Features Left to Implement](#featimpl)  
  
[Technologies Used](#usertech)  

[Testing](#testing)  

[Deployment](#deployment)  

[Credits](#credit)  
  * [Content](#content)  
  * [Media](#media)  
  * [Acknowledgements](#acknowled)  
  * [Links](#link)    
    

## The UX Framework (Strategy Plane)<a name="strategyplane"></a>


### Introduction<a name="introduction"></a>  
This project is a full-stack site based around business logic used
to control a centrally-owned dataset. It will include an authentication
mechanism and provide paid access to the site's data and/or other activities
based on the dataset, such as the purchase of a product/service.  

Main Technologies:  
* HTML, CSS, JavaScript, Python+Django
* Relational database (recommending MySQL or Postgres)
* Stripe payments
* Additional libraries and API’s  
  
Value provided:  
  
* By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.  
* The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.  
 
  
### Goal<a name="goal"></a>   
To build a social network subscription application.  
  
External user’s goal:  
  
To join a social network community and purchase, ad contacts and purchase monthly subscriptions.  
  
Site owner's goal:  
  
* Build an active community around the social network based on subscription and individual payments models.
* Add new contacts and build a relationship database
* Sell Monthly subscriptions from free version to paid
  


## User Stories (Scope Plane)<a name="ux"></a>

The type of users for the BizNet are non-subscribers, subsribers, admin user. 
  
**Non-subscribers**  
As a non-ubsriber I want:  
*	the signup process to be eazy and be understandable, so I won’t lose interest.
*	easily sign up for subscription, so I can get access to all features on the platform.
*	to see many users using it, so I can see how it will benefit me.
*	easy access to information to how the page work, to understand the purpose it serves.

**Subsribers**  
As a ubsriber user I want:  
*	navigation to be easy on the website, so I won’t be discouraged to use the website.

  
**Admin and Goals**  
As an admin I want:  
* to be able to create new categories, if it's needed.  
* to be able to edit or delete profiles, if it's needed. 
* users to be able to contact me if something is wrong with the website.


## Structure plane<a name="structureplane"></a>


### Typography<a name="typography"></a>

Font style used for the website is Ubuntu and Oswald. Ubuntu for headers and logo and Oswald for all other text.  


### Color<a name="color"></a>

The color used through the website are:  
  
•	Light gray    
•	Blue  
•	White  


### Interactive Design & Informative Architecture<a name="idandia"></a>

  
#### Recipes
  
In the top navbar there is a dropdown button with all recipe categories open for public. Once I select one of them rows with recipes are shown in the body. To view the you click on the name or pic.

#### Create a profile
  
For the first time user, the option to “Register” or “Sign In” on the first page. When choosing “Register” user have to fill in a username and a password. Then click “Create account” and the page automatically takes the user to their profile page. If user already has an account they just click on the “Sign In” button and fill in the username and password.

#### Categories
  
When you’re a logged in user you will see a button in the top navbar called “Categories”. When clicked a dropdown list shows of all category options shows. Once I select one of them a list with all of those recipes should show in the main window.
  
For Admin, the categories link in top navbar gives access to add/edit/delete the categories.


#### Create Recipe Posts
  
As a registered user you should see a button called “Create Recipes” in your profile. Once clicked it should clear how to fill in the fields. 

#### Edit Profile  
By clicking on the "Edit" button on your recipe you should be able to open up the edit form and save the changes. 

#### Delete Profile  
If you want to delete a post, it should be easily done by clicking on “Delete Recipe” button on the page of your recipe. You will get a confirmation message that the post has been deleted.

#### Sign In  
In the top navbar the “Sign In” button should be displayed if your an unregistered user or if you not logged in yet.

#### Sign Out
The “Sign Out” button in the top navbar should be clickable and log you out of your account. You will get a confirmation popup message that you've been logged out.
  


## Skeleton Plane<a name="skeletonplane"></a>

### The structure of the website:<a name="skeleton"></a>   

![Skeleton](https://.png)


### The database structure:<a name="database"></a>   
  
Django default databases SQLite in gitpod environment and PostgreSQL database with Heroku as production enviroment. Contains 4 collections:

*	user  
*	contacts  
*	message  
*	subscription 
* ...   
 
  
![Database](https://.png)

 ### Profile categories:<a name="recipecat"></a>   
     
*	Carpenter  
*	Electrician  
*	Accountant  
*	IT Consultant  
*	Graphic designer  
*	Markerter
*	Hair dresser
*	....  


### Profile information:<a name="recipeinfo"></a>   
    
*	First Name  
*	Last Name  
*	Title  
*	Area  
* .......


## Surface Plane:<a name="surfaceplane"></a>   
 

### Wireframes:<a name="wireframes"></a>   
 

**First Page** 
  
![First Page](https://.png)

  
**Login**
    
![Login](https://.png)  
  
**Forgot/Reset Password**  
    
![Forgot/Reset Password](https://.png)  

  
**Register Profile**  
    
![Register Profile](https://.png)  
  
**Register Profile - Matching Preferences**  
    
![Register Profile - Matching Preferences](https://.png)  
  
  
**Profile**  
    
![Profile](https://.png)  

**New Matches**  
    
![New Matches](https://.png)  
  
**My Contacts**  
  
![My Contacts](https://.png)  

  
**Network Search**  
    
![Network Search](https://.png)


**Non-subscription User**  
    
![Subscription user](https://.png)
  
**Non-subscription User**  
    
![Subscription user](https://.png)

  
  **Subscription Form**  
  
![Subscription Form](https://.png)



## Features:<a name="features"></a>   
 

### Existing Features:<a name="existingfeat"></a>   
  
**Popup Info Links:** [From Source](https://)  
  
Popup with link to subscription.  

**Static Top Navbar:** [From Source](https://) 

Navbar with dropdown links aligned to the right for message, settings, , login, register and search.  
  
**Static Bottom Navbar:** [From Source](https://) 

With search options.  
  
**Register Form:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) 

User create a username and password that get stored in the database under user.
  
**Login Form:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) 

Login with username and password.   
  
**Logout Function:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization)  
  
  When user logout it brings them back to the login site.

  
**Profile Page setup:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) 

Personalized profile page for logged in user. If you have created any recipes then they will show here.
  
   
    
  
**Links:** 
Responsive links to view other profiles.  
  
**Profile Form:**  

Includes input fields for name,... A dropdown menu for cooking time, difficulty options, categories, portions. The information saved in  database.  
  
**Edit/delete Profile:**  

If user wants to edit or delete their profile ..... If user choose to delete profile it will bring them back to first page.  
  
**Images:** 

All images are taken from internet and box sized to fit the recipes pages, except for the logo and category pictures. They are save in the project with reference under media.  
  

**Add Image to Profile** Code from [Gazza J MS3](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/templates/add_recipe.html)  

Used the function of adding url picture for the profile picture.
  
**Flash messages:** 

Verification to users when creating, editing or deleting post or deleting account. 
  
**Buttons:** 

When register an account or login there is a confirmation button at the end.  
  
**Boxes:** 

Confirmation...  
  
**Footer** [From Materialized](https://) 

Repetition links at the bottom from the navbars, copyright information, and a back to top button.
  
**Bring to Top Button:**  
  
  [Icon](https://fontawesome.com/icons/chevron-up) used. Code from [w3s](https://www.w3schools.com/icons/tryit.asp?filename=tryicons_fa-chevron-up).



### Features Left to Implement:<a name="featimpl"></a>   
 


## Technologies Used:<a name="usertech"></a>   
 
**Text Editor:**
  * [GitPod](https://gitpod.com/) – the editor to build, commit, and push data to GitHub.  
  
**Control System:**
  * [GitHub](https://github.com/) – used to host the project.  
  
**Database:**
  * [MongoDB](https://mongodb.com/) – cloud based service used for managing the database. 
   
**Platform Host:**
  * [Heroku](https://heroku.com/) – Cloud based platform for deployment of app.  
  
**Key Generator:**
 *	[MiniWebTool](https://miniwebtool.com/django-secret-key-generator/) - For generating Django secretkey.  
  
**Languages:**
  * [HTML](https://sv.wikipedia.org/wiki/HTML) – for the basic structure of the project.
  * [CSS](https://sv.wikipedia.org/wiki/Cascading_Style_Sheets) –for the overall style of website.
  * [JavaScript](https://developer.mozilla.org/sv-SE/docs/Web/JavaScript) - used to activate functions
  *	[jQuery](https://jquery.com/) – used as the main JavaScript function.
  *	[Python](https://www.python.org/) – for the backend of project.  
  
**Frameworks:**
  * [Django](https://www.djangoproject.com/) – Framework used for project.  
  
  
**Style:**
  *	[Google Fonts](https://fonts.google.com/) – For using and Oswald and Ubuntu fonts on website.
  *	[Balsamiq Wireframes](https://balsamiq.com/wireframes/) – used for the websites wireframes. 
   
**Validations:**
  *	[W3C CSS Validator]() - Validate CSS
  *	[W3C HTML Validator]() - Validate HTML
  *	[Chrome DevTools]() - Errors in console
  *	Jshint](https://jshint.com/) - Validate JavaScript
  *	[PEP8](http://pep8online.com/) – for validate the Python code.  
  

## Testing<a name="testing"></a>  
  
[Testing.md](Testing.md)  
  
    

## Deployment<a name="deployment"></a>
Deployment for this GitHub repository project is done through Heroku through the following steps;

**1. Heroku**
  * Create an account on Heroku and Login
  *	We have to register the MongoDB database information for the project. Under “Settings” scroll down to “Config Vars”. We need to add following variables for our env.py to secure the webpage;

    *	IP : (Add ip address)
    *	PORT : (0.0.0.0)
    *	SECRET_KEY : (Add secret key)
    *	MONGO_URI : (Add string from MongoDB cluster connection button)
    *	MONGO_DBNAME : (Add your MongoDB project name)

*	To create new application, click on “New” on the dashboard and then choose “Create new app”.
* Choose an app name without spaces.
*	Click on Deployment and choose the deployment method of your choice (in this case it GitHub).
*	Click on your GitHub Name that appears in the window as a dropdown list and select your project.
*	Click on the “Connect” button for sync app and project.
  
**2.	GitPod**  
  
In terminal (CLI):

** - pip3 install dj_database_url

** - pip3 install psycopg2-binary

** - pip3 freeze --local > requirements.txt  
  
Add Database in settings.py file in project app (get url from HEROKU -> Settings -> Config Vars -> DATABASE_URL)  
  
DATABASES = { 'default': dj_database_url.parse('DATABASE_URL') }  
  
In terminal (CLI):  
  
* - python3 manage.py showmigrations  
  
Migrate:  
** - python3 manage.py migrate  
  
Load database:  

** - python3 manage.py loaddata db.json  
  
Add super user:  
** python3 manage.py createsuperuser
** Add gunicorn to Gitpot
  
** - pip3 install gunicorn
  
** - pip3 freeze --local > requirements.txt
  
Add Procfile and add web dyno:  
  
** web: gunicorn shop.wsgi:application
  
In terminal (CLI):  
  
** - heroku login or heroku login -i
  
open in a browser and click Log In button or add credentials in terminal, then:  
  
** - heroku config:set DISABLE_COLLECTSTATIC=1 --app appname  
  
in settings.py file
ALLOWED_HOSTS = ['.herokuapp.com']  
  
In terminal (CLI):  
  
initialize heroku git remote:  

** - heroku git:remote -a appname  
and:

** - git push heroku master
 
  
**3.	Heroku**  
  
Deploy tab

* click connect to GitHub search for a repository and Connect

* click Enable Automatic Deploys
  
Add in settings tab -> Conf Vars  
  
SECRET_KEY  
  
in settings.py SECRET_KEY = os.environ.get('SECRET_KEY', '')  
  
and  
  
DEBUG = 'Development' in os.environ  

#### Run the project locally

Clone the project:  
  
*	Log in to GitHub and locate the repository you like to clone.
*	Click on the  “Code” button on the left side of the GitPod.
*	In the dropdown menu click on the HTTP option in the left top corner.
*	Click on the copy icon for the repository url.
*	In your local IDE choose the location where you want your clone directory.
*	Type “git clone” in Terminal and paste the url. Enter.  
  
Clone to GitHub Desktop:  
  
*	Log in to GitHub and locate the repository you like to clone.
*	Click on the  “Code” button on the left side of the GitPod.
*	In the dropdown menu click on the HTTP option in the left top corner.
*	Click on the “Open with GitHub Desktop.  
*	Then follow the prompts GitHub Desktop instructions to complete the clone.  


## Credits:<a name="credit"></a>

### Content:<a name="content"></a>


### Media:<a name="media"></a>


Link to [Media.md](Media.md) information.
  
  
  
### Acknowledgements<a name=”acknowled”></a>
•	I received inspiration for this project from X


### LINKS<a name=”link”></a>
