from django.urls import path
from django.urls import re_path as url
from knox import views as knox_views
from AsgariUcret import views
from .api import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    url(r'^asgariucret', views.asgariucret_api),
    url(r'^asgariucret/(\d+)', views.asgariucret_api),
    url(r'^asgariucret/savefile', views.SaveFile),
    path('', views.asgariucret_api),
    path('user/', UserAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('api/auth /logout', knox_views.LogoutView.as_view(), name="knox-logout")
]
