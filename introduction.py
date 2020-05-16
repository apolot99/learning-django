# this is the introduction chapter

# brevity means exact use of words in writing

# django is a python-based free and open source web framework. (Just like how there is streamlit, so there is also python)

#      CHAPTER 1

#  The command line is found in a programme called terminal.

# When the book refers to command line, it means open a new console on your computer using terminal.

#  Most frequently commands used in django development; 
#  cd (change down a directory)
#  cd..(change up a directory)
#  ls (list files in your current directory)
#  pwd (print working directory)
#  mkdir (make directory)
#  touch (create a new file)

# The $ sign is our command line prompt. All commands are to be typed after $ prompt.

# Virtual environments are an isolated container containing all the software dependencies of a given project.

# Use a dedicated virtual environment for each new python project. i.e Pipenv

# Pipenv creates a Pipfile containing software dependencies and a Pipfile.loc for ensuring deterministic builds.

# Determinism means that each time and everytime you download the software in a new virtual environment, you will have exactly the same configuration.

# Virtual Environment
# =========================
# venv is a Python package for creating virtual environments
# First install venv as follows: 
# apt-get install python3-venv

# Then create a virtual environment (for example myvenv) as follows:
# python3 -m venv myvenv
# Then activate your virtual env as follows
# source myvenv/bin/activate
# Run the above command every time you start working on your project

# Parenthesis around the name of your current directory on your command line indicates the virtual environment is activated.

# To exit our virtual environment type CONTROL-C (not necessary because when you open a project, it's venv automatically opens)

#                    This is my typical process for every new project
# Create a new repository on github.com
# Then I clone it on my desktop github
# Then open up the folder I have clones using visual studio code
# Then I open my terminal and create a virtual environment for my project i.e python3 -m venv name
# The activate that environment i.e source name/bin/activate
# Then install django i.e pip install django
# Then start my project using django admin i.e django-admin startproject name

# The settings.py file controls our project's settings
# urls.py tells django which pages to build in response to a browser or URL request
# wsgi.py helps dajngo serve our eventual web pages
# manage.py is used to execute various django commands such as running the local web server or creating a new app

# admin.py is a configuration file for the built in django admin app
# apps.py is a configuration file for the app itself.
# migrations keep track of any changes to our model.py so our data base and models.py file stay intact
# models.py is where we define our databse models which django automatically translates into data base models
# apps.py is for our app specific tests
# views.py is where we handle our requests/response logic for our web app

# local apps are apps running on your computer
# local apps should always be at the bottom of INSTALLED_APPS in the settings.py file because django executes the INSTALLED_APPS settings from top to bottom
# The internatl admin app is loaded first

# In django, 4 separate files are used to power one single page i.e;
# - urls.py file
# - views.py file
# - models.py file
# - index.html

#       What happens when you type in a URL 
# a URLpattern is found that matches the home page
# the URLpattern specifies a view 
# the view determines the contents for the page usually from a database model and template for styling and basic logic
# the end result is sent back to the suer as an HTTP response

# URLconfs determines where the content is going
# the model contains content from the database
# the template provides styling for it

# when it comes to errors, look at the last line and it will tell you exactly where the error is

# Git is a version control sysytem 

# Initial set up of our pages app involves the following steps;
# -create a directory for our code
# -install django in a new virtual environment
# -create a new django project
# -create a new pages app
# -update settings.py

# To ignore a folder, create a new file called gitignore using this command in the terminal, touch .gitignore
# Open up the gitignore file and add the name of the folder you want to ignore inside of gitignore

# Templates are individual HTML files that can be linked together

# Every web framework needs a convenient way to generate HTML files and django uses templates to do so.

# HTML is a HyperText Markup Language file format used as the basis of a web page.

# press CONTROL+Z to underdo something

# Classes unlike functions should always be capitalized

# When using class based views, always add as_view() at the end of the view name

# In the words of Django co-creator Jacob Kaplan-Moss, “Code without tests is broken as designed.”

# Writing tests is important because it automates the process of confirming that the code works as expected.

# The status code for each page is 200 which is the standard response for a successful HTTP request.

# Putting our code into production means making our site available on the internet where veryone can see it by deploying our code to an external server that anyone can use to see our site.

# Local code lives only on our computer while production code lives on an external server available to everyone.

# Pip is a package manager for python

# Gunicorn is a web server suitable for production

# A database model is used to store is used to store and display posts from our users.

# The design/schema of databases is the blue print of how all information is stored, updated and accessed. i.e relational and non relational

# Relational databases consist of tables that are structured in clumns and rows like excel spreadsheets.

# MySQL, PostgreSQL, Microsoft Access, Microsoft SQL and oracle are relational databases. 

# They use Structured Query Language (SQL) which is a programming language just for managing data in a relational database.

# Non relational data bases do not have a strict a strict row and column schema

# Every row in a relational table has a primary key

# the 'id' column is the primary key

# A key tenant of good database design is that each data item like username should be stored once in one location

# A second tenant of good database design is to use input constraints to increase the reliability of your data

# Foreign keys let us link multiple database tables together.

# Types of foreign key relationships i.e one to many, one to one, many to many

# Normalization is the process of eliminating redundant data from database tables





