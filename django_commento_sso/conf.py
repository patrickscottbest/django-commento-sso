from django.conf import settings
from appconf import AppConf


class DjangoCommentoSSOConf(AppConf):
    SECRET_KEY = None

    from django_commento_sso.utils import commento_user_name_function
    USER_NAME_FUNCTION = commento_user_name_function

    USER_LINK_FUNCTION = None
    USER_PHOTO_FUNCTION = None
    # COMMENTO_USER_EMAIL = None
    # COMMENTO_USER_NAME = 'user.name'
    # COMMENTO_USER_LINK = None
    # COMMENTO_USER_PHOTO = None

    class Meta:
        prefix = 'commento'
