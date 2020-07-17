from django.contrib.auth.models import User

# django has configurations that would potentially cause a problem with the commento SSO requirements of email and name.
# we are assuming that to commento, name is a mutable object and email is immutable (fixed forever)

def commento_user_name_function(user):

    # if not user.first_name or user.last_name:
    #     return user.username
    # elsif user.first_name and user.last_name:
    #     return ("%s %s" % user.first_name , user.last_name)
    # elsif user.first_name:
    #     return ("%s" % user.first_name)
    # elsif user.last_name:
    #     return ("%s" % user.last_name)

    return ("%s" % user.username)
