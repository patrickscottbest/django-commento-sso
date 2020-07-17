# django-commento-sso
A Django Single Sign-On Module for the Popular Commento.io platform

# Usage
Be familiar with the instructions at https://docs.commento.io/configuration/frontend/sso.html
You will need a commento account if you are using the single signon

# Requirements
1. Django set up and ready to receive.  This is tested on 3.0.8 with Python 3.8.2.  YMMV.
2. Commento.io account

# Installation

You have two options to install.  Edit your requirements.txt text with either of the following methods

## PyPi direct

    django-commento-sso

## PyPi via Github

    git+https://github.com/patrickscottbest/django-commento-sso@master

If you're feeling brave, I keep a development branch: 

    git+https://github.com/patrickscottbest/django-commento-sso@development


# OPTIONS
The following options are settable in your settings.py

## Mandatory
      COMMENTO_SECRET_KEY = "abc123-secretkeyfromcommento-64characterslong-321cba"

## Optional

All optional settings.py statements refer to a function.  You can pass any function that returns a text string based on a provided django.contrib.auth.User object.

Only a default user_name function is provided at this time.

     COMMENTO_USER_NAME_FUNCTION =

These functions will return other information to commento.io.  They are considered "optional".  Again, you can pass any function that returns a text string (which will be a URL pointing to a profile or photo) based on a provided django.contrib.auth.User object.

     COMMENTO_USER_LINK_FUNCTION =
     COMMENTO_USER_PHOTO_FUNCTION =


# SECURITY CONSIDERATIONS

Aside from the commento.io security considerations, you may wish to adhere to the following django security considerations:

1.  Do not allow users to change their email addresses on your site.
2.  Use an alternative strategy for issuing "Name:" to commento's SSO payload receiver, rather than the defacto provided "User.username" method here.  The username login can be divined from commento postings this way, and this author considers usernames to be one half of *the* password in it's entirety.


https://docs.commento.io/configuration/frontend/sso.html#security-checklist

Your HMAC secret key is kept securely. If you lose this, anybody can impersonate requests from Commento and you will leak personal data.

You're verifying signatures before processing data.

You're using a well-audited crypto library for HMAC. Never roll out your own crypto.

You're using a timing safe comparison algorithm to compare the hashes and not a simple string comparison. This is done to prevent timing attacks.

You're authenticating your users properly before sending Commento a response payload. This includes email verification, two-factor authentication, access control lists, and so on.

You're redirecting to the HTTPS version of Commento at the end. Personal data is transmitted in this stage and using plain HTTP is grossly insecure.

# TODO

Perhaps users who self-host would like the option to select their own host.  Not my priority.

I have authored this github to be a standalone app, but have not yet deployed on PyPi.  

# HELP ME!
Fix it and issue a pull request.  Thanks!
