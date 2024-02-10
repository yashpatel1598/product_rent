from django.shortcuts import render
from django.http import *

# Create your views here.
def hello(request):
    return  HttpResponse("Hello World")

# def add(request):
#     num1 = request.GET["num1"]
#     num2 = request.GET["num2"]
#     sum_result = float(num1) + float(num2)
#     context = {"sum":sum_result}
#     return render(request,"add/index.html",context=context)
