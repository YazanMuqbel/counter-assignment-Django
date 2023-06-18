from django.urls import path    
from . import views

urlpatterns = [
    path('', views.session),
    path('destroy/', views.destroy, name='destroy'),

]
