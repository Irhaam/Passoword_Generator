from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''
   
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('012345689'))
    if request.GET.get('special'):
        characters.extend(list('!@#%^&*()'))
    
    length=int(request.GET.get('length',12))
    for x in range(length):
        thepassword +=random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})

def info(request):
    return render(request,"generator/About.html")


