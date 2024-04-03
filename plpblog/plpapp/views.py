# myapp/views.py

# Create your views here.


from django.http import HttpResponse

def plpapp(request):
    return HttpResponse("Hello, World this is my first django project!")
def contact(request):
    return HttpResponse("Contact page")
