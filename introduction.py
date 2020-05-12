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






