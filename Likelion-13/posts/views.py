from django.shortcuts import render
from django.http import JsonResponse # �߰� 
from django.shortcuts import get_object_or_404 # �߰�
from django.views.decorators.http import require_http_methods # �߰�
from .models import * # �߰�
import json
from comment.models import Comment
from .serializers import PostSerializer
# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsAuthor, IsValidTime

class PostList(APIView):
    permission_classes = [IsAuthor, IsValidTime]

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(slef, request, format=None):
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor, IsValidTime]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)