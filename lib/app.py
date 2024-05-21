import asyncio
import socket
import threading

from lib.context import Context
from lib.middleware import Middleware
from lib.request import Request
from lib.response import Response

class App:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.routes = dict()
        self.middlewares: list[Middleware] = []
        
    def start(self):
        server_socket = socket.create_server((self.host, self.port), reuse_port=False)
        while True:
            conn, _ = server_socket.accept()
            threading.Thread(target=lambda: asyncio.run(self.__handle_connection(conn))).start()
    
    def add_middleware(self, middleware):
        self.middlewares.append(middleware())
    
    def map_endpoint(self, path: str, route):
        a = path.split("/")
        while "" in a:
            a.remove("")

        path = "/".join(a)
        self.routes[path] = route

    async def __handle_connection(self, conn: socket.socket):
        data = conn.recv(1024).decode()
        lines = data.split("\r\n")
        
        req = Request(lines)        
        context = Context(req)
        self.__handle_context(context)
        
        conn.send(context.response.to_http_response().encode())
        conn.close()
        
    def __handle_context(self, context: Context) -> Response:
        # one-way middlewares
        for middleware in self.middlewares:
            middleware.run(context)            