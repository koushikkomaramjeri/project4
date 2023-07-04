from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def calculate(request):
    x=int(request.POST['t1'])
    y=int(request.POST["t2"])
    optype=request.POST["op"]
    if optype=="add":
        z=x+y
        res="the sum is: "+str(z)
    elif optype=="sub":
        z = x - y
        res = "the sub is: " + str(z)
    elif optype=="mul":
        z = x * y
        res = "the mul is: " + str(z)
    else:
        z = x/y
        res = "the div is: " + str(z)
    response=HttpResponse(res)
    return response
