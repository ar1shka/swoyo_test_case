import pytest


@pytest.fixture
def response_200() -> str:
    return "\r\n".join(
        [
            "HTTP/1.1 200 OK",
            "Access-Control-Allow-Origin: *",
            "Access-Control-Allow-Headers: *",
            "Access-Control-Allow-Credentials: true",
            "Access-Control-Expose-Headers: *",
            "Connection: keep-alive",
            "Keep-Alive: timeout=5",
            "Content-Type: application/json",
            "Content-Length: 45",
            "",
            '{"status": "success", "message_id": "123456"}',
        ]
    )


@pytest.fixture
def response_400() -> str:
    return "\r\n".join(
        [
            "HTTP/1.1 400 Bad Request",
            "Access-Control-Allow-Origin: *",
            "Access-Control-Allow-Headers: *",
            "Access-Control-Allow-Credentials: true",
            "Access-Control-Expose-Headers: *",
            'sl-violations: [{"location":["request","body"],"severity":"Error","code":"required","message":"Request body must have required property \'sender\'"},{"location":["request","body"],"severity":"Error","code":"required","message":"Request body must have required property \'recipient\'"},{"location":["request","body"],"severity":"Error","code":"required","message":"Request body must have required property \'message\'"}]',
            "Connection: keep-alive",
            "Keep-Alive: timeout=5",
            "Content-Type: application/json",
            "Content-Length: 31",
            "",
            '{"error": "Invalid parameters"}',
        ]
    )


@pytest.fixture
def response_401() -> str:
    return "\r\n".join(
        [
            "HTTP/1.1 401 Unauthorized",
            "Access-Control-Allow-Origin: *",
            "Access-Control-Allow-Headers: *",
            "Access-Control-Allow-Credentials: true",
            "Access-Control-Expose-Headers: *",
            'sl-violations: [{"location":["request"],"severity":"Error","code":401,"message":"Invalid security scheme used"}]',
            "Connection: keep-alive",
            "Keep-Alive: timeout=5",
            "Content-Type: application/json",
            "Content-Length: 32",
            "",
            '{"error": "Invalid credentials"}',
        ]
    )


@pytest.fixture
def response_404() -> str:
    return "\r\n".join(
        [
            "HTTP/1.1 404 Not Found",
            "Access-Control-Allow-Origin: *",
            "Access-Control-Allow-Headers: *",
            "Access-Control-Allow-Credentials: true",
            "Access-Control-Expose-Headers: *",
            "content-type: application/problem+json",
            "Connection: keep-alive",
            "Keep-Alive: timeout=5",
            "Content-Type: application/json",
            "Content-Length: 199",
            "",
            '{"type": "https://stoplight.io/prism/errors#NO_PATH_MATCHED_ERROR", "title": "Route not resolved, no path matched", "status": 404, "detail": "The route / hasn\'t been found in the specification file"}',
        ]
    )


@pytest.fixture(scope="module")
def address() -> tuple[str, int]:
    return "127.0.0.1", 4010
