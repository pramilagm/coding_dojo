from django.shortcuts import render, HttpResponse,redirect
from .models import Book, Author


def index(request):
    if request.method == "GET":
        context ={
        'books':Book.objects.all()
        }
        return render(request, 'books_authors_apps/index.html',context)
    if request.method =="POST":
        title = request.POST['title']
        desc = request.POST['desc']
        Book.objects.create(title = title, desc = desc)
        return redirect('/')

def view(request,id):

    if request.method =='GET':
        books_info = {
            'books_infos':Book.objects.get(id = id),
            'author_infos':Author.objects.all(),
        }
        return render(request,'books_authors_apps/Books_info.html', books_info)
    if request.method=="POST":
        
        this_book = Book.objects.get(id=id)
        this_book.author.add(Author.objects.get(id=request.POST['author_id']))
        return redirect('/books/'+str(id))


    
def authors(request):
    if request.method == "GET":
        context ={
            'authors':Author.objects.all()
        }
        return render(request,'books_authors_apps/authors.html' ,context)

    if request.method =="POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        Author.objects.create(first_name=first_name,last_name=last_name)
        return redirect('/authors')

def author_view(request, author_id):
    if request.method == "GET":
        author_infos ={
            'author_in': Author.objects.get(id=author_id),
            'book_infos':Book.objects.all()
        }
        return render(request,"books_authors_apps/authors_info.html",author_infos)
    if request.method =="POST":
        this_author = Author.objects.get(id = author_id)
        this_author.Books.add(Book.objects.get(id= request.POST['book_id']))
        return redirect("/author/" + str(author_id))

def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/')

def author_delete(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('/authors')