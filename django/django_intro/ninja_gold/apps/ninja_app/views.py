from django.shortcuts import render,HttpResponse,redirect
import random,time

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    context ={
        'gold' : request.session['gold'],
        'activities' : request.session['activities']
    }
    return  render(request,'ninja_app/index.html', context )

def process(request):
    str_format = ('%Y/%m/%d %H:%M %p')

    if request.POST['building']=="farm":
        val = random.randint(10,20)
        request.session['gold'] += val
        log = "<div style ='color:Blue'>Earned "+ str(val) +" gold from the farm !  " +time.strftime(str_format)+"</div>"
        request.session['activities'].append(log)

    elif request.POST['building']=="cave":
        val = random.randint(5,10)
        request.session['gold'] += val
        log = "<div style ='color:Blue'>Earned "+ str(val) +" gold from the farm !  " +time.strftime(str_format)+"</div>"
        
        request.session['activities'].append(log)

    elif request.POST['building']=="house":
        val = random.randint(2,5)
        request.session['gold'] += val
        log = "<div style ='color:Blue'>Earned "+ str(val) +" gold from the farm !  " +time.strftime(str_format)+"</div>"
        request.session['activities'].append(log)

    elif request.POST['building']=="casino":
        val = random.randint(0,50)
        request.session['gold'] -= val
        log = "<div style ='color:red'>Enter a casino and lost  "+ str(val) +" gold ...ouch!!" +time.strftime(str_format)+"</div>"
        request.session['activities'].append(log)

    return redirect('/')

def reset_activity(request):
    del request.session['gold']
    del request.session['activities']
    request.session.modified = True
    return redirect("/")