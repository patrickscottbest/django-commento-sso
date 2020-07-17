from django.shortcuts import render, redirect
from django_commento_sso.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
#import hashlib
import hmac
import json
import logging
logger = logging.getLogger(__name__)

def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = auth.get_user(request)
    return request._cached_user


def sso(request) :

	if settings.SECRET_KEY == None:
		logger.error("django_commento_sso - COMMENTO_SECRET_KEY not found in settings.py")
		return HttpResponse(status=204)


	if request.GET['token']:
		logger.debug("token as received %s" % request.GET['token'])
	else:
		return HttpResponse(status=204)


	if request.GET['hmac']:
		logger.debug("hmac as recevied %s" % request.GET['hmac'])
	else:
		return HttpResponse(status=204)


	receivedHmacBytes = bytes.fromhex(request.GET['hmac'])
	tokenBytes = bytes.fromhex(request.GET['token'])

	secretKeyBytes = bytes.fromhex(settings.COMMENTO_SECRET_KEY)
	expectedHmacBytes = hmac.digest(secretKeyBytes, tokenBytes, 'sha256')
	print ("expected hmac was %s" % expectedHmacBytes.hex() )

	if expectedHmacBytes==receivedHmacBytes:

		logger.debug("HMAC comparison of token - match")

		if not request.user.is_authenticated:
            return redirect('%s?next=https://%s?hmac=%s&token=%s' % (settings.LOGIN_URL, request.get_full_path(),request.GET['hmac'],request.GET['token']))
		else:
			logger.info("django_commento_sso SSO Success for User %s" % request.user.username )
			payload = {
			    "token": request.GET['token'],
			}
			if not request.user.email:
				logger.error('django_commento_sso User must have email for Commento SSO')
				return False
			else:
				payload['email']=request.user.email


			payload['name']=settings.COMMENTO_USER_NAME_FUNCTION(get_user(request))

			if settings.COMMENTO_USER_LINK_FUNCTION:
				payload['link']=settings.COMMENTO_USER_LINK_FUNCTION(get_user(request))
			if settings.COMMENTO_USER_PHOTO_FUNCTION:
				payload['photo']=settings.COMMENTO_USER_PHOTO_FUNCTION(get_user(request))

			payloadHMACHex=(hmac.digest( secretKeyBytes, bytes(json.dumps(payload),'utf8'),'sha256')).hex()
			payloadHex=bytes(json.dumps(payload),'utf8').hex()

			return redirect("https://commento.io/api/oauth/sso/callback?payload={0}&hmac={1}".format(payloadHex, payloadHMACHex))

	else:
		#spoofed token attempt or error
		logger.warning("django_commento_sso SSO HMAC comparison - No match")
		return HttpResponse(status=404)
