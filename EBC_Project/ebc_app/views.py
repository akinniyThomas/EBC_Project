from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "ebc_app/index.html", 
           {
               'title' : 'EBC YOUTH!!',
           })