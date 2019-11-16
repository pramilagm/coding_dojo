from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt

from .models import User, Book

def index(request):
    return render(request,'favorite_books_app/index.html')
def register(request):
    email_check = User.objects.filter(email =request.POST['email'])
    if email_check:
        messages.error(request, "THAT EMAIL ALREADY EXISTS")
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cnpassword = request.POST['cnpassword']
        User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
        return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/books')
        else:
            messages.error(request, 'The password is invalid!')
            return redirect("/")
def books(request):
    if 'userid' not  in request.session:
       return render(request,'favorite_books_app/info.html')
    else:
        context= {
            'user':User.objects.get(id=request.session['userid']),
            'books':Book.objects.all()
            }
        return render(request,'favorite_books_app/books.html',context)

def books_add(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        user = User.objects.get(id = request.session['userid'])
        new_book = Book.objects.create(uploaded_by = user,title = request.POST['title'],desc = request.POST['desc'])
        new_book.users_who_like.add(user)
        return redirect('/books')

def display(request):
    context ={
        'user':User.objects.get(id=request.session['userid']),
        'books':Book.objects.all()
        
    }
    return render(request,'favorite_books_app/fav_books.html',context)

def add_favorite(request, book_id):
    user = User.objects.get(id = request.session['userid'])
    this_book = Book.objects.get(id = book_id)
    this_book.users_who_like.add(user)
    return redirect ('/books')

def show_book_info(request,book_id):
    if 'userid' not  in request.session:
        return render(request,'favorite_books_app/info.html')
    else:
        context ={
            'user':User.objects.get(id=request.session['userid']),
            'books':Book.objects.get(id=book_id)
            # 'user': User.objects.id(id)
        }
    return render(request,'favorite_books_app/book_info.html', context)

def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    book.desc = request.POST['desc']
    book.save()
    messages.success(request, "Description successfully updated")
    return redirect('/books/show/'+str(book_id))

def book_delete(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')

def unfavorite(request,book_id):
    book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=request.session['userid'])
    book.users_who_like.remove(this_user)
    return redirect('/books/show/'+str(book_id))
    
def add_favorite_book(request, book_id):
    user = User.objects.get(id = request.session['userid'])
    this_book = Book.objects.get(id = book_id)
    this_book.users_who_like.add(user)
    return redirect('/books/show/'+str(book_id))

def logout(request):
    if 'userid'  in request.session:
        request.session.clear()
    return redirect('/')
