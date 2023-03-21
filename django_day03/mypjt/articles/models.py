from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)  # 타이틀은 문자열 형태임을 알려줌
    content = models.TextField()