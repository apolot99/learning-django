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