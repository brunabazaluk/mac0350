from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('query1', views.query1, name='query1'),
    path('query2', views.query2, name='query2'),
    path('query3', views.query3, name='query3'),
    path('query4', views.query4, name='query4')

]
