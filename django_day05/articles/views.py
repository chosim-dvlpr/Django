from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')


# DB에 저장하기 순서
# 1. 사용자가 입력한 값 가져오기
# 2. DB 저장하기
def create(request):
    # 데이터 가져오기
    title = request.GET.get('title')    # name부분 (title)
    content = request.GET.get('content')
    
    # 방법 1
    # DB에 새로운 Article 저장
    # Article.objects.create(
    #     title=title,
    #     content=content
    # )

    # 방법2 - 가장 많이 사용
    article = Article(title=title, content=content)
    # 이 사이에 로직 추가 가능
    article.save()

    # 방법3
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    return redirect('articles:index')   # index로 보내기

'''
# create, new 합치기
def create(request):
    if request.method == 'POST':    # POST 일 때
        # 데이터 가져오기
        title = request.POST.get('title')    # name부분 (title)
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:index')   # index로 보내기
    else:
        # GET일 때
        return render(request, 'articles/new.html')
'''