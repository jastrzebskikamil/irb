from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def blog(request):
    return render(request, 'personal/blog.html' , {'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})
