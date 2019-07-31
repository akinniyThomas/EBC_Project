from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    mesages = Message.objects.order_by('pk')
    return render(request, "ebc_app/index.html", 
           {
               'title' : 'EBC YOUTH!!',
               'mesages' : mesages,
           })