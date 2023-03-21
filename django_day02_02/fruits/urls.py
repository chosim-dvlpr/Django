from django.urls import path
from . import views

app_name = 'fruits' # 앱 이름
urlpatterns = [
    path('fruit/', views.fruit),
]
