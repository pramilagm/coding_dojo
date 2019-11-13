from django.shortcuts import render, HttpResponse,redirect

def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request,"first_app/index.html",context)
    
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