from django.shortcuts import render,redirect
from .models import Tv_show
from django.contrib import messages
def index(request):
    context = {
        'all_shows': Tv_show.objects.all()
    }
    return render(request,'tv_show_app/index.html',context)

def new(request):
    
    return render(request,'tv_show_app/show_add.html')

def create(request):
    errors = Tv_show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for tag, error in errors.items():
            messages.error(request,error)
            return redirect('/shows/new')
    elif request.method == "POST":
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        new_show = Tv_show.objects.create(title= title, network= network, release_date=release_date, desc = desc)
        show_id = new_show.id
   
        return redirect('/shows/'+str(show_id))
            
def view (request,show_id):
    context ={
        "show": Tv_show.objects.get(id=show_id)
    }
    return render(request,'tv_show_app/show_view.html',context)

def show_edit(request,show_id):
    context = {

        "show":Tv_show.objects.get(id=show_id)
    }
    return render(request,'tv_show_app/show_edit.html',context)

def show_edit_update(request ,show_id):
    errors = Tv_show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for tag, error in errors.items():
            messages.error(request,error )
            return redirect('/shows/'+show_id)
    else:
        new_show = Tv_show.objects.get(id = show_id)
        new_show.title = request.POST['title']
        new_show.network = request.POST['network']
        new_show.release_date = request.POST['release_date']
        new_show.desc = request.POST['desc']
        new_show.save()

    return redirect('/shows/'+str(show_id))

def show_destroy(request,show_id):
    show = Tv_show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
    



 