from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
   
   x=1
   y=2
   # return HttpResponse('Hello world')
   #return render(request, 'hello.html')
   return render(request, 'hello.html', {'name':'mosh'})

# Create your views here.
#request -> Response
#Request Handler
#Action






