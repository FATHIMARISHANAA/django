from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
   path("",views.index,name="home"),
   path("about",views.about,name="aboutus"),
   path("department",views.department,name="department"),
]
