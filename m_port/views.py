from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'index.html')

# class HomePageView(TemplateView):
#     template_name = "index.html"

# class AboutPageView(TemplateView):
#     template_name = "about_me.html"