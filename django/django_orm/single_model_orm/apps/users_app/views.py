from django.shortcuts import render, HttpResponse
from .models import Users


def index(request):
    context =  {

        "user_info":Users.objects.all()
    }
    return render(request, "users_app/index.html",context)
