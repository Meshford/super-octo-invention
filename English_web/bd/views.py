from django.shortcuts import render

def bd_home(request):
    return render(request, 'main/index.html')