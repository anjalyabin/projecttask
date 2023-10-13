from django.shortcuts import render

# Create your views here

from django.shortcuts import render

def fun(request):



    return render(request,"index.html")

def fun1(request):

    return render(request, "register1.html")