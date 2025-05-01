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

class Comment_list(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many = True)
        if serializer.is_valid:
            return Response(serializer.data)
        
# Create your views here.
@require_http_methods("GET")
def comment_list(request, post_id): # ��� ��� ��ȸ 
    if request.method == "GET":
        comment = get_object_or_404(Post, id=post_id)
        
        comment_all = Comment.objects.filter(post=comment) 
        

        comment_json_all = []
        
        for comment in comment_all:
            comment_json = {
                "author_name" : comment.author_name,
                "content": comment.content,
            }
            comment_json_all.append(comment_json)

        return JsonResponse({
            'status': 200,
            'message': 'success',
            'data': comment_json_all
        })