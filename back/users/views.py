from django.shortcuts import render

# Create your views here.
def home():
    return render('<h1>Hello</h1>')