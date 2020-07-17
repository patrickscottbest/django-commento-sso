===============================
django-commento-sso
===============================

django-commento-sso is a Django app to interact with commento.io single sign on.
It receives commento's redirect, verifies, and sends the user back to commento.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django-commento-sso" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-commento-sso',
    ]

2. Add COMMENTO_SECRET_KEY in 64-character text to your settings.py 

3. Include the URLconf in your project urls.py like this::

    path("sso/", include('django_commento_sso.urls')),
