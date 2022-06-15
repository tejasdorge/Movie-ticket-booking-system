import logging
request_logger = logging.getLogger('movie')

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        # log_data = {
        # 'request_method': request.method,
        # 'request_path': request.get_full_path(),
        # 'response_status_code': response.status_code,
        # 'response_data': response.data
        # }
        # request_logger.info(msg=log_data)
        return response
