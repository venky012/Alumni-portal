from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('register/', views.accounts_register, name='register'),
    path('updateDP/', views.upload_image, name='upload_photo'),
    path('deleteUser/', views.delete_user, name='delete_user'),
    path('updateprofile/', views.update_profile, name='update_profile'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
    path('delete/<slug:uidb64>/<slug:token>)/', views.delete, name='delete'),
    path('profile_page/userinfo/<str:username>/',views.user_profile,name='profile_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()