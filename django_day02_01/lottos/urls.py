from django.urls import path
from . import views

app_name = 'lottos' # 앱 이름
urlpatterns = [
    path('ss/', views.greeting, name='greeting'),
    path('index/', views.index, name='index'),
    path('lotto/', views.lotto, name='lotto'),
]
