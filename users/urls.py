from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name ='users/login.html'), name='login'), #korzystamy z budowanego w django widoku do logowania. Nalezy recznie podac link to szablonu z logowaniem
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.register, name='register'),
]