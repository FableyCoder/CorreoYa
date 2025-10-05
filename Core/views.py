from django.shortcuts import render

def home(request):
    return render(request,"core/home.html")

def quien(request):
    return render(request,"core/quien.html")

def pregunta(request):
    return render(request,"core/pregunta.html")
