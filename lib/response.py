class Response:
    def __init__(self) -> None:
        self.status = 200
        self.content: str = ""
        self.content_type: str = "plain/text"
    
    def get_status_message(self):
        match self.status:
            case 200: return "OK"
            case 404: return "Not Found"
            case _: return ""
    
    def to_http_response(self):
        head = f"HTTP/1.1 {self.status} {self.get_status_message()}\r\n"
        headers = f"Content-Type: {self.content_type}\r\n"
        headers += f"Content-Length: {len(self.content)}\r\n"
        headers += "\r\n"
        content = self.content
        return head + headers + content