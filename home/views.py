from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserLoginForm ,NoteForm
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from django.http import JsonResponse
from .models import Note
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        form = NoteForm()
        notes = Note.objects.filter(user = request.user)
        if request.method =='POST':
            title = request.POST['title']
            description =  request.POST['description']
            print(title  , description)
            note = Note()
            note.title = title
            note.description = description
            note.user = request.user
            note.save()
            notes = Note.objects.values().filter(user = request.user)
            user_notes=list(notes)
            return JsonResponse({"status":"1", 'status_message' : "Note created","notes" : user_notes})

        return render(request, "index.html" , {'form' : form ,"notes":notes})
    else:
        return redirect('Login')
    
def register(request):
    form  = UserRegisterForm(request.POST)
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        print(name,username,email,password,re_password)
        if password != re_password:
            messages.error(request, "Password not match")
        else:
            user = User.objects.create_user(first_name=name,username=username,email=email,password=password)
            user.save()
            if user.is_active:
                print("register")
                messages.success(request,"user created")
            else:
                print('error')          
            
    return render(request,"register.html" ,{'form' : form})

def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(request,username = username , password = password)
        if user is not None:
            login(request,user)
            print(username,password)
            return JsonResponse({'status':"User login succesfully"})
        else:
            return JsonResponse({'status':"credentials wrong"})
    return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('Login')

def edit_note(request):
    edit_id = request.POST['edit_id']
    title = request.POST['title']
    description = request.POST['description']
    Note.objects.filter(id=edit_id).update(title=title , description = description)
    notes = Note.objects.values().filter(user = request.user)
    user_notes=list(notes)
    return JsonResponse({"status":"1",'status_message' : "Note created","notes" : user_notes})


def delete_note(request):
    delete_id = request.GET.get('delete_id')
    Note.objects.filter (id=delete_id).first().delete()
    notes = Note.objects.values().filter(user=request.user)
    user_notes=list(notes)
    return JsonResponse({"status":"1",'status_message' : "Note Deleted","notes" : user_notes})