from django.urls import path
from . import views


urlpatterns = [
	path('', views.mycard),
	path('home/', views.home)

]
