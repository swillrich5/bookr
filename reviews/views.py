from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get("name") or "world"
    return render(request, 'base.html', {"name": name})

def search(request):
    search = request.GET.get("search") or "No Search Term Entered"
    return render(request, 'search_result.html', {"search": search})
