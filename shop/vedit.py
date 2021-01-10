
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mytb
def index(request):
	msg="";
	id="";
	if request.method == 'POST':
		alldata1=request.POST
		id = alldata1.get('id',0)
		obj=Mytb.objects.get(id=id)
		username = alldata1.get('name',0)
		obj.username = username		
		getid=obj.save()
		msg="Data Update Successfully"	
	if request.method == 'GET':
		alldata=request.GET
		id = alldata.get("id",0)
	all_entries = Mytb.objects.filter(id=id)
	return render(request, "web/editdb.html", {'msg':msg,"all_entries":all_entries})