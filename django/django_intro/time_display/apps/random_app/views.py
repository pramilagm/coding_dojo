
from django.shortcuts import render, HttpResponse,redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['random'] = ""

    return render(request,'random_app/index.html' )

def random(request):
    random_string = get_random_string(length =12)
    request.session['random'] = random_string
    request.session['counter'] += 1
    

    return redirect('/random')


def reset(request):
 
    del request.session['counter']
    return redirect('/random')