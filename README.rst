=====
django-commento-sso
=====

django-commento-sso is a Django app to interact with commento.io sso.
It receives commento's redirect, verifies, and sends the user back to commento.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django-commento-sso" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-commento-sso',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('commento/', include('django_commento_sso.urls')),


