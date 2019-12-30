"""
import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("----request----")
        return

    def process_view(self, request, func, *args, **kwargs):
        print("----view----")
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        co = time.time() - start
        print('{:.2f}s'.format(co))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        print("----response----")
        return response
"""



#第一次修改
import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("----request----")
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        print("----view----")
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        co = time.time() - start
        print('{:.2f}s'.format(co))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        print("----response----")
        co = time.time() - self.start_time
        print( 'request to response cose:{:.2f}s'.format(co) )
        return response



"""
#第二次修改   修改不成功，屏蔽以后再看,注意有对应settings.py中的修改
class MiddlewareMixin( object ):
    def __init__( self , get_response = None ):
        self.get_response = get_response
        super( MiddlewareMixin , self ).__init__( )

    def __call__(self, requst ):
        response = None
        if hasattr( self , 'process_request' ):
            response = self.process_request(request)
        if not response:
            response = self.get_response( request )
        if hasattr( self , 'process_response' ):
            response = self.process_response( request , response )
        return response
"""