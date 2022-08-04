from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'registerApp/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        myUser = User.objects.create_user(username=username,password=pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.email = email
        myUser.save()
        messages.success(request,"You have been registerd successfully")
        return redirect('registerApp:login')
    return render(request,'registerApp/userRegister.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        myUsr = authenticate(request,username=username,password=pass1)
        if myUsr is not None:
            login(request, myUsr)
            #return redirect('registerApp:index')
            return render(request,'registerApp/index.html',{'username':myUsr.username})
        else:
            messages.error(request,"Login Failed!!")
            return redirect('registerApp:login')
    return render(request,'registerApp/userLogin.html')

def userLogout(request):
    logout(request)
    return redirect('registerApp:index')
