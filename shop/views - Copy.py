
from django.http import HttpResponse
from django.shortcuts import render
from django import forms


def index(request):
	message = "Not logged in, Please Login Here"
	username=""
    # return HttpResponse("<h1>MY First Web</h1><br><br>Hello, world. You're at the polls index.")
	if request.method == 'POST':
		alldata=request.POST
		username = alldata.get("name",0)
		message = "Login by user name :"+username
	return render(request, "web/index.html", {"username":username,"message":message})