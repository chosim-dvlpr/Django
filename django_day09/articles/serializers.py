from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep

'''
class ArticleListSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 특정 게시글에 작성된 댓글 목록 출력하기
    comment_set = CommentSerializer(many=True, read_only=True)  # 특정 게시글에 작성된 댓글 목록 출력하기 => class 순서 바꿔주어야 함
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 특정 게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
            'comment_set',
            'comment_count',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep
'''

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

class ArticleDetailSerializer(ArticleListSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)  # 특정 게시글에 작성된 댓글 목록 출력하기 => class 순서 바꿔주어야 함
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 특정 게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력

    class Meta(ArticleListSerializer.Meta):
        fields = ArticleListSerializer.Meta.fields + (
            'comment_set',
            'comment_count',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep