from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json

def lists_handler(request):
    return render_to_response('listhome.html', context_instance=RequestContext(request))
