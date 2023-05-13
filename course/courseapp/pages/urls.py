from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    # path('',views.index,'index.html'),
    path('',views.home),
    path('anasayfa',views.home),
    path('iletisim',views.iletisim),
    path('hakkimizda',views.hakkimizda),
    
]