
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mytb
def index(request):
	msg="";
	usernameses="";
	if request.session.has_key('username'):
		usernameses = request.session['username']
	if request.method == 'GET':
		if request.GET :
			allget=request.GET		
			id=allget.get("id",0)
			obj = Mytb(id = id)
			obj.delete()
			msg="Delete Success of ID : "+id
	all_entries = Mytb.objects.all()
	return render(request, "web/mylist.html", {'msg':msg,"all_entries":all_entries,'usernameses':usernameses})