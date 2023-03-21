from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

def create(request):
    return render(request, 'articles/create.html')

def submit(request):
    print(request.GET)  # <QueryDict: {'content': ['내용']}> 출력
    print(request.GET.get('title'))     # None 출력
    print(request.GET.get('content'))   # 내용 출력
    
    title = request.GET.get('title')
    content = request.GET.get('content')

    # # DB에 저장
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'articles/submit.html', context)