from django.shortcuts import render

# Create your views here.
def Cat(request):
    return render(request,'generic.html')