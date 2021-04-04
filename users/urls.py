from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'users'

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.loginview, name='loginview'),
    path('login/loginuser', views.loginuser, name='loginuser'),
    path('logout/', views.logoutview, name='logoutview'),
    path('add/adduser', views.adduser, name='adduser'),
    path('add/', views.add, name='add'),
    path('<int:profile_id>/detail/', views.detail, name='detail'),
    path('<int:profile_id>/delete/', views.delete, name='delete'),
    path('<int:profile_id>/edit/', views.edit, name='edit'),
    path('<int:profile_id>/edit/edituser', views.edituser, name='edituser'),
    path('searchuser', views.searchuser, name='searchuser'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
