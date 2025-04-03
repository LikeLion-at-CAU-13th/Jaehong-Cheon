from django.shortcuts import render
from django.http import JsonResponse # ??? 
from django.shortcuts import get_object_or_404 # ???
from django.views.decorators.http import require_http_methods # ???
from .models import * # ???
import json
from posts.models import Post 

# Create your views here.
@require_http_methods(["GET"])
def post_list(request, category_id):
    if request.method == "GET":
        category = get_object_or_404(Category, id=category_id)
        # 카테고리 id에 해당하는 포스트를 가져옴
        post_all = Post.objects.filter(post_category__category=category).order_by('created')
    
		# 각 데이터를 Json 형식으로 변환하여 리스트에 저장
        post_json_all = []
        
        for post in post_all:
            post_json = {
                "title" : post.title,
                "content": post.content,
                'username': post.user.username,
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status': 200,
            'message': 'success',
            'data': post_json_all
        })