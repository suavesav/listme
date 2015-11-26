from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import json

def lists_handler(request):
    if request.is_ajax() and request.POST:
        operation = request.POST.get('operation', None)
        if operation=='test':
            test_text = request.POST.get('txt')
            return HttpResponse(json.dumps({'msg':test_text}), content_type='application/json')
    return render_to_response('listhome.html', context_instance=RequestContext(request))
