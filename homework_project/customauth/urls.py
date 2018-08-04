from django.urls import re_path

from django.contrib.auth.models import User

### see => https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
from django.contrib.auth import views as auth_views


###
### uninstalled django 2.1 
### and than installed 2.0.7, so auth_views works!
###


from . import views as custom_auth_views

app_name = 'custom_auth'

urlpatterns = [

    re_path(r'^signup/$', custom_auth_views.signup, name='signup'),
    re_path(r'^login/$', auth_views.login, name='login'), 
    re_path(r'^logout/$', auth_views.logout, {'next_page': 'learning:courses_list'} , name='logout'),

]