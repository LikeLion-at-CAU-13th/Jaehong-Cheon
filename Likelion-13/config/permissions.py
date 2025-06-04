from rest_framework import permissions
from django.utils import timezone
import pytz
from datetime import time

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user #작성자감 맞는지 
    
class IsValidTime(permissions.BasePermission):
    def has_permission(self, request, view):
        kst = pytz.timezone('Asia/Seoul')
        now_kst = timezone.now().astimezone(kst).time()

        start = time(22, 0)
        end = time(7, 0)

        if now_kst >= start or now_kst < end:
            return False
        return True
        