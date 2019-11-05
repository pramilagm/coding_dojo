from django.shortcuts import render, HttpResponse,redirect

def index(request):

    return HttpResponse("hello Programmer Have Fun")
def new(request):
    return HttpResponse('This the the new blog ')

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse("this the blog " + number)

def edit(request,number):
    return HttpResponse(" the edited number is " +number )

def destroy(request,number):
    return redirect('/')