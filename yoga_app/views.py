from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
	return HttpResponse("Hello! Welocome to my yoga site")
