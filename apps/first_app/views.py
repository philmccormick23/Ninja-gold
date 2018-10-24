from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
# the index function is called when root is visited

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'money' not in request.session:
        request.session['money']=0
    return render(request, 'pages.html')

def process_money(request):
    if request.POST['type']=='farm':
        request.session['money'] += random.randrange(10, 20)
        request.session['gold'] += request.session['money']

    elif request.POST['type']=='cave':
        request.session['money'] += random.randrange(5, 10)
        request.session['gold'] += request.session['money']
    elif request.POST['type']=='house':
        request.session['money'] += random.randrange(2, 5)
        request.session['gold'] += request.session['money']
    elif request.POST['type']=='casino':
        request.session['money'] += random.randrange(-50, 50)
        request.session['gold'] += request.session['money']
    elif request.POST['type']=='zero':
        request.session.clear()
    
    


    return redirect('/')
    