from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def contactUs(request):
    return render(request,"contactUs.html")

def ourAchievements(request):
    return render(request,"ourAchievements.html")