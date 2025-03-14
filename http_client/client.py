import socket

from .request import Request
from .response import Response


def send_sms(request: Request) -> Response:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((request.host, request.port))
        s.send(request.to_bytes())
        response = s.recv(4096)

    return Response.from_bytes(response)
