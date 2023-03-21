from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def subway(request):
    return render(request, 'my_app/subway.html')
