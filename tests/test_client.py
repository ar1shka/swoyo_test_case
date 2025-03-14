import pytest

from http_client import Request, send_sms


@pytest.mark.parametrize(
    ("method", "endpoint", "headers", "body", "expected"),
    [
        ("post", "/", {}, {}, "response_404"),
        (
            "post",
            "/send_sms",
            {},
            {
                "sender": "test_sender",
                "recipient": "test_recipient",
                "message": "test_message",
            },
            "response_401",
        ),
        (
            "Post",
            "/send_sms",
            {"Authorization": "Basic dXNlcjpwYXNz"},
            {},
            "response_400",
        ),
        (
            "Post",
            "/send_sms",
            {"Authorization": "Basic dXNlcjpwYXNz"},
            {
                "sender": "test_sender",
                "recipient": "test_recipient",
                "message": "test_message",
            },
            "response_200",
        ),
    ],
)
def test_client(
    request: pytest.FixtureRequest,
    address: tuple[str, int],
    method: str,
    endpoint: str,
    headers: dict[str, str],
    body: dict[str, str],
    expected: str,
) -> None:
    host, port = address
    response = send_sms(Request(method, host, port, endpoint, headers, body))
    response.headers.pop("Date", None)
    assert str(response) == request.getfixturevalue(expected)
