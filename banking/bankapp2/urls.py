# In your urls.py file, add the following URL patterns
from django.urls import path
from . import views
app_name='bankapp2'
urlpatterns = [
    # The URL for the navbar view
    path("navbar/", views.navbar, name="navbar"),
    # The URL for the district view, with a dynamic parameter for the district name
    path("district/<str:name>/", views.district, name="district")
]
