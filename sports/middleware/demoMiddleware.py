import logging
logger = logging.getLogger(__name__)

class demoMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        logger.warning("middleware called new in call")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        logger.info("middleware called new")
        pass

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response
