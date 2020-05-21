# BLOG APP

# We perfrom a migration to set up a database

# For the author field in blog/models.py, we’re using a ForeignKey which allows for a many-to-one relationship. This means that a given user can be the author of many different blog posts but not the other way around

#  For all many-to-one relationships such as a ForeignKey we must also specify an on_delete option.

# we create database models by updating our models.py file in our app

# After creating our database, we configure it.

# After entering information on our django admin, we need to create the necessary views, URLs, and templates so we can display the information on our web application.

# After, we’ll first configure our blog_project/urls.py file and then our app-level blog/urls.py file to achieve this.

# Then, In our views file, add the code to display the contents of our Post model using ListView.

# After creating templates file, update settings.py so django knows to look there for our templates

#  CSS is referred to as a static file because, unlike our dynamic database content, it doesn’t change. 

# Fortunately it’s straightforward to add static files like CSS, JavaScript, and images to our Django project.

#  We need to add the static files to our templates by adding {% load static %} to the top of base.html.

# Because our other templates inherit from base.html we only have to add this once.

# All blog post entries will start with post/

