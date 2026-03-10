from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.


# this was the first view i created, this is how httpResponse works, commnething this in so tat we can make other views and return different responses when we go to different url patterns defined in urls.py file of the app.
# def index(request):  # here, we have written request because every view receives a request, and his request is the input like parameters
#     return HttpResponse("<h1>Hello, welcome to my website!</h1>")  # this will return a simple response when we go to the root page of the website. we can also return a template instead of a simple response by using render function and passing the request and the template name as arguments.


  #this was thw second thing i did
def index(request):
   
    
    return render(request, 'index.html') # here we are rendering the index.html template when we go to the root page of the website. we need to create a templates folder in the base directory of the project and then create an index.html file inside that folder and write some html code in that file to see the response when we go to the root page of the website.

def counters(request):
    text = request.GET['text'] 
    amount_words = len(text.split()) # this will split the text into a list of words
     # Get the text from the query parameters
    return render(request , "counter.html" , {"amount": amount_words})  # here we are rendering the counter.html template when we go to the root page of the website. we need to create a templates folder in the base directory of the project and then create a counter.html file inside that folder and write some html code in that file to see the response when we go to the root page of the website. we are also passing a context dictionary