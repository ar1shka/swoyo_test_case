import pytest

from http_client import Request


@pytest.mark.parametrize(
    ("method", "host", "port", "endpoint", "headers", "body", "expected"),
    [
        (
            "GET",
            "localhost",
            8080,
            "/",
            {},
            {},
            "GET / HTTP/1.1\r\nHost: localhost:8080\r\nContent-Type: application/json\r\nContent-Length: 2\r\n\r\n{}",
        ),
        (
            "post",
            "127.0.0.1",
            4010,
            "/test",
            {"Test-Header": "test header value"},
            {"content": "empty"},
            'POST /test HTTP/1.1\r\nHost: 127.0.0.1:4010\r\nTest-Header: test header value\r\nContent-Type: application/json\r\nContent-Length: 20\r\n\r\n{"content": "empty"}',
        ),
    ],
)
class TestRequest:
    def test_request(
        self,
        method: str,
        host: str,
        port: int,
        endpoint: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        request = Request(method, host, port, endpoint, headers, body)
        assert request.method.upper() == method.upper()
        assert request.host == host
        assert request.port == port
        assert request.endpoint == endpoint
        assert request.headers == headers
        assert request.body == body

    def test_request_to_str(
        self,
        method: str,
        host: str,
        port: int,
        endpoint: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        request = Request(method, host, port, endpoint, headers, body)
        assert str(request) == expected

    def test_request_to_bytes(
        self,
        method: str,
        host: str,
        port: int,
        endpoint: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        request = Request(method, host, port, endpoint, headers, body)
        assert request.to_bytes().decode() == expected

    def test_request_from_bytes(
        self,
        method: str,
        host: str,
        port: int,
        endpoint: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        request = Request.from_bytes(expected.encode())
        assert request.method.upper() == method.upper()
        assert request.host == host
        assert request.port == port
        assert request.endpoint == endpoint
        assert request.headers == headers
        assert request.body == body
