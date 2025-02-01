from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1 style="color:green">Wellcome to the Home page!</h1>')

def coder(request):
    return HttpResponse('<marquee style="font-weight:bold; font-size:60px;">I am a passioneted programmer from bangladesh and now i am able to work world wide</marquee>')

def show_specific_task(request, id):
    print("id: ", id)
    print("id type: ", type(id))
    return HttpResponse(f"This is specific task page! task id is {id}")


def user_dashboard(request):
    return render(request, 'user-dashboard.html')