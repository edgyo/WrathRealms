from django.urls import path

from . import views

urlpatterns = [
    path('america', views.america, name='america'),
    path('europe', views.europe, name='europe'),
    path('russia', views.russia, name='russia'),
    path('info', views.info, name='info'),
    path('', views.index, name='index'),
]