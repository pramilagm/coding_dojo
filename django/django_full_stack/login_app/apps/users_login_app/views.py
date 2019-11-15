from django.shortcuts import render,redirect
from django.contrib import messages
from apps.users_login_app.models import Form
import bcrypt


# Create your views here.
def index(request):

    return render(request,'users_login_app/index.html', {'form':Form.objects.all()})

def register_form(request):

    check = Form.objects.filter(email = request.POST['email'])
    if check:
        messages.error(request, "THAT EMAIL ALREADY EXISTS")
        return redirect('/')
    errors = Form.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cnpassword = request.POST['cnpassword']
        Form.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash,birthday=birthday)
        return redirect('/')

def login(request):
    email = Form.objects.filter(email = request.POST['email'])
    if email:
        logged_email = email[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_email.password.encode()):
            request.session['id'] = logged_email.id
            return redirect('/success')
        else:
            messages.error(request, 'The password is invalid!')
            return redirect("/")

def success(request):
    if 'id' not in request.session:
        return render(request,'users_login_app/message.html')

    else:
        id = request.session['id']
        context = {
            'user':Form.objects.get(id=id)
        }
        return redirect('/wall')
  

    
def logout(request):
    if 'id' in request.session:
        del request.session['id']
    return redirect('/')
