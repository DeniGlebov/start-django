from time import time

from students.views import logging


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)  # view func call

        end = time()
        with open('middlewares.log', 'a') as file:
            diff = end - start
            file.write(f'{request.path} {request.method} {diff}\n')

        return response


class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()

        path = request.path
        execution_time = str(end - start)
        method = request.method

        if '/admin/' in path:
            # print(f'{path} {execution_time} {method}')
            logging(method=method, path=path, execution_time=execution_time)

        return response
