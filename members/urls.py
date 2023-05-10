from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('members/',views.members,name="members"),
    path('mens_shirt/<int:men_shirt_id>',views.men_shirt,name="men_shirt"),
    path('mens_shirt/upload',views.upload,name='upload'),
    path('mens_jacket/<int:men_jacket_id>',views.men_jacket,name="men_jacket"),
    path('mens_jacket/upload',views.upload,name='upload'),
    path('mens_pants/<int:men_pants_id>',views.men_pants,name="men_pants"),
    path('mens_pants/upload',views.upload,name='upload')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)