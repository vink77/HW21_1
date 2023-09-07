from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'catalog/index.html')

def info(request):
    return render(request,'catalog/info1.html')