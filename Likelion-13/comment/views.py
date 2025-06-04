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

class Comment_list(APIView):
    permission_classes = [IsValidTime]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many = True)
        if serializer.is_valid:
            return Response(serializer.data)
        
