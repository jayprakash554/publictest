from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views
from . import vlist
from . import vedit
from . import uploadfile

urlpatterns = [
	url(r'^$', views.home , name = 'home'),
    #path('', views.index, name='index'),
	path('delete', vlist.index, name='index'),
	path('edit', vedit.index, name='index'),
	path('mylist', vlist.index, name='index'),
	path('uploadfile', uploadfile.index, name='index'),

	
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
