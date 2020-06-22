#  always use a custom user model for all new Django projects

#  This is cz if you want to make any changes to the Usermodel down the road–-for example adding an age field-–using a custom user model from the beginning makes this quite easy.

# Creating our custom user model requires four steps:
#  -update settings.py file
#  -create a new custom User model
#  -create new forms for UserCreationForm and UserChangeForm
#  -update users/admin.py

#  null is database-related.When a field has null=True it can store a database entry as NULL, meaning no value

#  blank is validation-related, if blank=True then a form will allow an empty value, whereas if blank=False then a value is required.

# We should always create a dedicated pages app for all our static pages.

#  run the startapp command then update INSTALLED_APPS.

# There are two ideal times to add tests:
# -before you write any code (test-drivendevelopment)
# -immediately after you've added new functionality and it's clear in your mind 

#  you do not need to add tests for core Django functionality.

# while doing tests, we  test three things:
# -the page exists and returns a HTTP 200 request code
# -the page uses the correct url name in the view
# -the proper template is being used

# Bootstrap comes with the four basic file that we need i.e
# -Bootstrap.css
# -jQuery.js
# -Popper.js
# -Bootstrap.js

# The fastest method I’ve found to figure out what’s happening under-the-hood in Django is to simply go to the Django source code on Github, use the search bar and try to find the specific piece of text.

# SendGrid is a popular service for sending transactional emails.

# A general rule of thumb is to use the plural of an app name–posts,payments,users,etc.– 

# unless doing so is obviously wrong as in the common case of blog where the singular makes more sense.

# I have the same django admin for all the projects, we just pick the author we want to use for the specific project

# Bootstrap has a built-in component called Cards that we can customize for our individual articles

# mixin is a special kind of multiple inheritance that Django uses to avoid duplicate code and still allows customization

# After making a new model it’s good to play around with it in the admin app before displaying it on our actual website

#  This is called a “query” as we’re asking the database for a specific bit of information. 
