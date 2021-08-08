from .views import *
from django.urls import path
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'covma'
urlpatterns = [
    path("patient_list",patient_list,name= 'detail'),
    path("patient_<int:pk>",patient_detail,name= 'delete'),
    path("virus_list",virus_list,name= 'detail'),
    path("virus_<int:pk>",virus_detail,name= 'delete'),
    path("virus_var_list",virus_var_list,name= 'detail'),
    path("virus_var_<int:pk>",virus_var_detail,name= 'delete'),
    path("ace_list",ace_list,name= 'detail'),
    path("ace_<int:pk>",ace_detail,name= 'delete'),
    path("ace_var_list",ace_var_list,name= 'detail'),
    path("ace_var_<int:pk>",ace_var_detail,name= 'delete'),
]
