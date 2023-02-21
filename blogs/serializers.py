from rest_framework import serializers
from blogs import models

# class BlogSerializer(serializers.Serializer):
#     id=serializers.ImageField()
#     title=serializers.CharField(max_length=100)
#     blog=serializers.CharField()


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Blog
        fields='__all__'

