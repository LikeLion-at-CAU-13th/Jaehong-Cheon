import logging
from django.utils.deprecation import MiddlewareMixin

# �ΰ� ����
logger = logging.getLogger('request_logger')

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info(f"URL: {request.method} {request.get_full_path()}")
