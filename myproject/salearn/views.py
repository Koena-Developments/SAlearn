from django.shortcuts import render
from django.http import HttpResponse



def hello_world(request):
    
    context = {'name':'Thabang Motswenyane'}
    return render(request, 'index.html', context)

def navigation(request):
    context = {'name':'Thabang Motswenyane'}
    return render(request, 'navigation_bar.html', context)