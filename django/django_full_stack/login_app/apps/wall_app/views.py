from django.shortcuts import render,redirect
from django.contrib import messages
from apps.users_login_app.models import Form
from apps.wall_app.models import Messages,Comments
def index(request):

    if 'id' not  in request.session:
        return render(request,'users_login_app/message.html')
           
    else:
        context ={
        'all_msg':Messages.objects.all(),
        'user':Form.objects.get(id =request.session['id'])
        }
        return render(request,'wall_app/index.html',context)
        



def post_message(request):
    print("INSIDE POST MESSAGE")
    user = Form.objects.get(id=request.session['id'])
    Messages.objects.create(user=user, message = request.POST['message'])
    return redirect('/wall')
def post_comment(request):
    user = Form.objects.get(id=request.session['id'])
    msg_obj = Messages.objects.get(id =request.POST['post_id'])
    Comments.objects.create(user=user, message = msg_obj, comments=request.POST['comment'])
    return redirect('/wall')


def delete_post(request):    
    message_delete = Messages.objects.get(id=request.POST['msg_id'])
    if message_delete.user.id != request.session['id']:
        messages.error(request, 'U are not authorized to delete this message')
        return redirect('/wall')
    else:
        message_delete.delete()
        return redirect('/wall')



def logout(request):
    if 'id' in request.session:
        del request.session['id']
    return redirect('/')


