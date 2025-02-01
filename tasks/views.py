from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def text_view(request):
    return HttpResponse('<h1 style="color:green">Hello coder, i am here to solve your problem.</h1>')

def coder(request):
    return HttpResponse('<marquee style="font-weight:bold; font-size:60px;">I am a passioneted programmer from bangladesh and now i am able to work world wide</marquee>')