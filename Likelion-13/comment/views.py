from django.shortcuts import render
from django.http import JsonResponse # ??? 
from django.shortcuts import get_object_or_404 # ???
from django.views.decorators.http import require_http_methods # ???
from .models import * # ???
import json
from posts.models import Post 

# Create your views here.
@require_http_methods("GET")
def comment_list(request, post_id): # 댓글 목록 조회 
    if request.method == "GET":
        comment = get_object_or_404(Post, id=post_id)
        # post_id에 해당하는 Post 객체를 가져옴
        comment_all = Comment.objects.filter(post=comment) 
        #Comment 모델에서 외래키인 post와 연결된 Post 객체를 가져옴

        comment_json_all = []
        # 각 데이터를 Json 형식으로 변환하여 리스트에 저장
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