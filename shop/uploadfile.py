
from django.http import HttpResponse
from django.shortcuts import render

from .forms import Profile_Form
from .models import Myupload
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def index(request):
	msg="";
	form = Profile_Form()
	if request.method == 'POST':
		form = Profile_Form(request.POST, request.FILES)
		if form.is_valid():
			 user_pr = form.save(commit=False)
			 user_pr.picture = request.FILES['picture']
			 file_type = user_pr.picture.url.split('.')[-1]
			 file_type = file_type.lower()
			 user_pr.save()
			 msg="Upload success"
	all_entries = Myupload.objects.all()	
	return render(request, "web/uploadfile.html", {'msg':msg,'all_entries':all_entries})