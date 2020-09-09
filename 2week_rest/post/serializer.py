from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # 다 보여주려면 all
        # fields = ['id', 'title', 'body']
        read_only_fields = ('title',)
        # title의 변경을 허용하지 않을 때.(나말고는 title 변경 ㄴㄴ)
        # read 말고 write로 써도 무방.
        
