
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mytb
def index(request):
	msg="";
	if request.method == 'POST':
		alldata=request.POST
		username = alldata.get("name",0)
		request.session['username'] = username
		obj = Mytb(username = username)
		obj.save()
		if obj.id > 0 :
			msg="Data Saved Successfully"	
		
	all_entries = Mytb.objects.all()
	return render(request, "web/insertdb.html", {'msg':msg,"all_entries":all_entries})