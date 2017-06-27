from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def send_sms(request):
    return HttpResponse('hi')