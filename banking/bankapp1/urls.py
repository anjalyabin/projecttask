
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='bankapp1'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('register1', views.register1, name='register1'),
    path('registerform', views.registerform, name='registerform'),
    path('logout', views.logout, name='logout'),

]

urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.conf.urls.static import static
