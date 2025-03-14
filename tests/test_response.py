import pytest

from http_client import Response


@pytest.mark.parametrize(
    ("status_code", "info", "headers", "body", "expected"),
    [
        (
            200,
            "OK",
            {},
            {},
            "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 2\r\n\r\n{}",
        ),
        (
            400,
            "NOT OK",
            {"Test-Header": "test header value"},
            {"content": "empty"},
            'HTTP/1.1 400 NOT OK\r\nTest-Header: test header value\r\nContent-Type: application/json\r\nContent-Length: 20\r\n\r\n{"content": "empty"}',
        ),
    ],
)
class TestResponse:
    def test_response(
        self,
        status_code: int,
        info: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        response = Response(status_code, info, headers, body)
        assert response.status_code == status_code
        assert response.info == info
        assert response.headers == headers
        assert response.body == body

    def test_response_to_str(
        self,
        status_code: int,
        info: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        response = Response(status_code, info, headers, body)
        assert str(response) == expected

    def test_response_to_bytes(
        self,
        status_code: int,
        info: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        response = Response(status_code, info, headers, body)
        assert response.to_bytes().decode() == expected

    def test_response_from_bytes(
        self,
        status_code: int,
        info: str,
        headers: dict[str, str],
        body: dict[str, str],
        expected: str,
    ) -> None:
        response = Response.from_bytes(expected.encode())
        assert response.status_code == status_code
        assert response.info == info
        assert response.headers == headers
        assert response.body == body
