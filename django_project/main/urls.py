from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index),
    path('about', views.about, name='about'),
    path('upload', views.upload),
    path('homeinfo', views.homeinfo),
    path('login', views.login_html),
    path('profile', views.profile_view, name='profile'),
    path('delete', views.delete_upload_file, name='delete_upload_file'),
    path('task3', views.task3, name='task3'),
    path('get_json_author', views.getJson, name='get_json_author'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register', views.RegisterView.as_view(), name="registerview"),
]
