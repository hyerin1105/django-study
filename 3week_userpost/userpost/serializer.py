from .models import UserPost
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyfield(source='author_username')

    class Meta:
        model = UserPost
        fields = ['pk', 'author_name', 'title', 'body']