from django.shortcuts import render,HttpResponse,redirect
from db.models import Signin
from django.contrib.auth import authenticate,login
import random
import smtplib as s

def home(request):
    if request.method=="post":
        print("h1")
        """email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)"""
        return HttpResponse("<h1>Welcome to Home Page2</h1>")
    print("h1")
    add = request.META.get("HTTP_X_FPRWARDED_FOR")
    if add:
        ip = add.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    return render(request,"home.html",{"ip":ip})

def signin(request):
    #if request.method=="get":
    if request.method=="POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        print(Email,Password)
        user = authenticate(request,email=Email,password=Password)
        """if Signin.objects.filter(email=Email).exists and Signin.objects.filter(password=Password).exists:
            return redirect("/")
        else:
            return HttpResponse("<h1>Welcome to Home Page</h1>")"""
        if user is not None:
            return redirect("/")
        else:
            return HttpResponse("<h1>Welcome to Home Page</h1>")
        
        
       
        #return redirect(request,"/")
    print("h1")
    return render(request,"sign_in.html",{})
       
     
        

def signup(request):
    print("Data 1")
    if request.method=="POST":
        print("Data 2")
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        Cpassword = request.POST.get("Cpassword")
        mobNo = request.POST.get("mobNo")
        #return HttpResponse("<h1>Welcome to Home Page1</h1>")
        print(Fname,Lname,email,password,Cpassword,mobNo)
        return HttpResponse("<h1>Welcome to Home Page2</h1>")

    print("Data 3")
    return render(request,"sign_up.html",{})
def validate(request):
    #if request.method=="POST":  
        #return HttpResponse("<h1>Welcome to Home Page</h1>")
    #if request.method=="GET":
        #return HttpResponse("<h1>Welcome to Home Page1</h1>")
    #else:
    #if request.method=="POST":  
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(email,password)
    return redirect(request,)

    #SisExists = Signin.isExists()
    """if Signin.objects.filter(email=Signin.email):
        print("Login Successfull")
        return HttpResponse("<h1>Login Successfull</h1>")"""
    
def otp(request):
    pass
def forgotPass(request):
    if request.method=="POST":
        print("post")
        email = request.POST.get("email")
        print(email)
        otp = random.randint(100000,999999)
        server = s.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("roshan.2002kumr@gmail.com","ntupwfddenyvxhug")
        msg = "Your OTP is {} Please don't share with anyone".format(otp)
        server.sendmail("roshan.2002kumr@gmail.com",email,msg)

        server.quit()
        
    return render(request,"forgotPass.html",{})