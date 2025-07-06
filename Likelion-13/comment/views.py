from django.shortcuts import render
from django.http import JsonResponse # ??? 
from django.shortcuts import get_object_or_404 # ???
from django.views.decorators.http import require_http_methods # ???
from .models import * # ???
import json
from posts.models import Post 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import CommentSerializer
from config.permissions import IsAuthor, IsValidTime
from config.custom_exception_handler import BaseCustomException

class Comment_list(APIView):
    permission_classes = [IsValidTime]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many = True)
        if serializer.is_valid:
            return Response(serializer.data)
    
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        content = request.data.get("content", "")
        if len(content) < 15:
            raise BaseCustomException(
                detail="댓글을 15자 이상 써주세요 ㅎㅎ",
                code="COMMENT_TOO_SHORT"
            )
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post) # post에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
