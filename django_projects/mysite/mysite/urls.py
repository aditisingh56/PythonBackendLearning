"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # we need to import include function to include the urls of our app in the main urls.py file

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('myappicreated.urls')),  # this means send all requesto to the app urls.py file and check if there is a match with the url pattern defined in that file and if there is a match then execute the code inside that function defined in views.py file and return the response to the user.
]
