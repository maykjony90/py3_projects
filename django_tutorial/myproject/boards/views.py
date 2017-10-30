from django.shortcuts import render

# Create your views here.

# DEGISIKLIK
from django.http import HttpResponse


# DEGISIKLIK
def home(request):
    return HttpResponse('Hello, World!')



sik = '<h1 style="text-align:center;font-size:100px">sik kafali!</h1>'
# TEST DEGISIKLIGI
def about(request):
	return HttpResponse(sik)
