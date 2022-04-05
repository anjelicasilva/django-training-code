from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.generic import View


import logging
logger = logging.getLogger(__name__)

# Create your views here.

# Basic Class based view example
class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

# User Authentication example
class UserAuthView(View):
    user = authenticate(username="anjelica", password="password")
    def get(self, request):
        if self.user:
            # logger.info('**** User is authentic ****')
            return HttpResponse('User is Authentic !!')
        else:
            # logger.info('**** Invalid User/ Password ****')
            return HttpResponse('Invalid User / Password')