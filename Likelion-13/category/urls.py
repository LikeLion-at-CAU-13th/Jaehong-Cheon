from django.urls import path
from posts.views import *
from category.views import *
urlpatterns = [
    path('<int:category_id>/posts/', post_list, name='post_list') # Post ?? ??
]