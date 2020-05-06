from django.conf import settings
from django.shortcuts import HttpResponse
from .models import GuestUser 
from datetime import datetime, timedelta
import requests
import uuid

class IpSessionMiddleware:

    now = datetime.now()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # request.session["guest_user"] = None
        # request.session["guest_ip"] = None
        last_activity = request.session.get('last_activity') if request.session.get('last_activity') else self.now.timestamp()
        user_ip = requests.get('https://api.ipify.org').text
        if request.session.get('guest_user') == None or request.session.get('guest_ip') != user_ip:
            if (int(self.now.timestamp() - last_activity)) > 862500 or request.session.get('guest_ip') != user_ip:
                # ('after more than 10 minutes of session')
                if (GuestUser.objects.filter(ipaddress = user_ip, uuid=request.session.get('guest_uuid'))).exists():
                    user = GuestUser.objects.get(ipaddress = user_ip, uuid=request.session.get('guest_uuid'))
                    request.session["guest_user"] = user.id
                    request.session["guest_ip"] = user.ipaddress
                    request.session["guest_uuid"] = user.uuid
                else:
                    id = str(uuid.uuid4())
                    user = GuestUser(ipaddress = user_ip, status="Active", uuid = id)
                    user.save()
                    request.session["guest_user"] = user.id
                    request.session["guest_ip"] = user_ip
                    request.session["guest_uuid"] = user.uuid
        request.session['last_activity'] = self.now.timestamp()
    