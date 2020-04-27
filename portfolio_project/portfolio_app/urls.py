from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('resume', views.resume, name='resume'),
]
