from django.urls import path  # this means thta we are importing the path , this is needed as we will send request to views ans we are wrtting that path here
from . import views  # here . means thiscurent folder.  so this line means import views.py from the current folder which is myappicreated folder. we need to import views.py because we will be using the functions defined in views.py to handle the requests and return responses when we go to a specific url pattern defined in urlpatterns list below.
urlpatterns = [
    path('' , views.index , name = 'index') , 

    # here name = index is the name of thje url, later we dont need to writ uirl we can use the name we have used.
    # path is empty strings, ehich means this will open the root page of the website when we go to localhost:8000/ 
    # views.index means that when we go to the root page of the website, it will call the index function defined in views.py and execute the code inside that function and return the response to the user.
    path('counters' , views.counters , name = 'counter'),
]