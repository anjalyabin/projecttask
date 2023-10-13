from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages,auth
from django.contrib import messages
from . models import  MyModel
def login(request):
     if request.method=='POST':
          username2=request.POST['username']
          password2=request.POST['password']
          user=auth.authenticate(username=username2,password=password2)
          if user is not None:
               auth.login(request,user)
               return redirect('bankapp:fun')
          else:
               print("user login")
               messages.info(request,"user login")
               return redirect('bankapp:fun')
     else:

          return render(request,"login.html")
def register(request):
   if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        cpassword1= request.POST['cpassword']
        if password1 == cpassword1 :
             if User.objects.filter(username=username1).exists():

                  messages.info(request, 'username already exist')
                  return redirect('bankapp1:register')
             else:
                  #if User.objects.filter(email=email1).exists():
                      # messages.info(request, 'Registration Failed - Try different email address')
                      # return redirect('bankapp1:register')
                 # else:


                       user = User.objects.create_user(password=password1,username=username1)
                       user.save();

                       print("user created")
                       return redirect('bankapp1:login')
        else:
             messages.info(request, 'password dose not match')
             return redirect('bankapp1:register')


   else:

        return render(request, "register.html")



def logout(request):
     auth.logout(request)
     return redirect('bankapp:fun')
def register1(request):

     return render(request,"register1.html")
def registerform(request):



     if request.method == 'POST':
          name1 = request.POST.get('MyModel', '')
          date1= request.POST.get('date', '')
          age1 = request.POST.get('age', '')
          mobile1 = request.POST.get('mobile', '')
          address1 = request.POST.get('address', '')
          task1 = MyModel(name=name1, date=date1,age=age1,mobile=mobile1,address=address1)
          task1.save()
     return render(request, 'registerform.html')
