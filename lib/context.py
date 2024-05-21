from lib.request import Request
from lib.response import Response

class Context:
    def __init__(self, request) -> None:
        self.request: Request = request
        self.response = Response()