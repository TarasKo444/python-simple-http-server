from lib.app import App
from lib.context import Context
from lib.middleware import Middleware

HOST = "127.0.0.1"
PORT = 8888

class TestMiddleware(Middleware):
    def run(self, context: Context):
        context.response.status = 400
        print("Middleware Working", context.request.content[0])

if __name__ == "__main__":
    app = App(HOST, PORT)
    print(f"Server started on {HOST}:{PORT}")

    app.add_middleware(TestMiddleware)
    
    app.start()