import random
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User,auth
from .models import myuser,contact
from django.contrib import messages
global userObject
userObject = 0
# Create your views here.
def index(request):
    context = {
    'variable':"This is sent"
    }
    return render(request,'index.html',context)
    # return HttpResponse("Mayur")

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html' )
def services(request):
    # return HttpResponse("This is services page")
    return render(request, 'Services.html' )

def contactus(request):
    if(request.method =="POST"):
        Account_No = int(request.POST.get('account',''),10)
        firstname = request.POST.get('first_name','')
        lastname = request.POST.get('last_name','')
        Email = request.POST.get('email','')
        phone = request.POST.get('Phone','')
        message = request.POST.get('message','')

        Contact= contact(Account_No = Account_No,firstname = firstname,lastname = lastname,Email = Email,phone = phone,message = message)
        Contact.save()
    return render(request, 'Contact.html' )

def trial(request):
    return render(request, 'trial.html' )
    # return HttpResponse("This is services page")

def Userlogin(request):
    if(request.method =="POST"):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        # print(username,password,balance)
        user = myuser.objects.filter(Username = username,Password=password).values()
        print(len(user),user)

        if len(user) == 1:
            # dep = user[0].get("Balance")
            # dep = dep + x
            # user[0].update({"Balance":dep})
            global userObject
            userObject = username
            bal = user[0].get("Balance")
            print(bal)
            return render(request,'UserFrame.html',{"bal":bal,"val":len(user)})
        else:
            messages.success(request, 'User not found !! Please check username and password !! ')

            print("User not found !! Please register first !! ")
            return render(request, 'User_Login.html')
            
            
    return render(request, 'User_Login.html')

def SignUp(request):
    if(request.method =="POST"):
        # itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        user = myuser.objects.values("Username")
        for i in user:
            print(i["Username"] == username,i,username)
            if i["Username"] == username:
                return HttpResponse("Username is taken")    
        
        if(password == password2):
            order = myuser(Account_No = random.randint(0,999),name=name, Balance = 0 ,Username=username, Password=password,)
            order.save()   
        else:
            return HttpResponse("Incorrect Password")
    return render(request,'SignUp.html')
     

def UserFrame(request):
    print(request,"Hiiii")
    if(request.method == "POST" and userObject):
        x = myuser.objects.all() 
        withdraw = request.POST.get('withdraw', '')
        Deposite = request.POST.get('Deposite', '')
        if(len(withdraw)>0 and len(Deposite)>0):
            return HttpResponse(f"Please do only one action at the time")
        if(not(len(withdraw)>0 or len(Deposite)>0)):
            return HttpResponse(f"Please Enter valid amount")

        if(len(withdraw)>0):
            withdraw = int(withdraw)
        else:
            withdraw = 0
        if(len(Deposite)>0):
            Deposite = int(Deposite)
        else:
            Deposite = 0
        for i in x:

            if(i.Username == userObject):
                if(Deposite):
                    bal = i.Balance
                    i.Balance += Deposite
                else:
                    bal = i.Balance
                    i.Balance -= withdraw
                    if(i.Balance<0):
                        # strr = f'Your account balanace is low {i.Balance}'
                        # messages.success(request, "Your account balanace is low")            
                        # print(strr)
                        # return render(request, 'UserFrame.html')

                        return HttpResponse(f"Your account balanace is low <br> <br> Account Balance: {bal}<br><br>Please withdraw amount with in balance amount only!! ")
                bal = i.Balance
            i.save()
    else:
            messages.success(request, 'Please Login corectly !! Please register first !!')
            print("Please Login corectly !! Please register first !! ")
            return render(request, 'User_Login.html')
                
    # return render(request, 'UserFrame.html')
    print(userObject)
    return HttpResponse(f"Payment Successfull!!<br><br>Your account balanace : {bal}")

def logout(request):
    global userObject
    userObject = 0
    return render(request, 'index.html',{"userObject": userObject})