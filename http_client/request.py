import json
from dataclasses import dataclass, field


@dataclass
class Request:
    method: str
    host: str
    port: int
    endpoint: str = field(default="/")
    headers: dict[str, str] = field(default_factory=dict)
    body: dict[str, str] = field(default_factory=dict)

    def __str__(self) -> str:
        content = json.dumps(self.body)
        request = "\r\n".join(
            [
                f"{self.method.upper()} {self.endpoint} HTTP/1.1",
                f"Host: {self.host}:{self.port}",
                *(f"{key}: {value}" for key, value in self.headers.items()),
                "Content-Type: application/json",
                f"Content-Length: {len(content)}",
                "",
                f"{content}",
            ]
        )
        return request

    def to_bytes(self) -> bytes:
        return str(self).encode()

    @classmethod
    def from_bytes(cls, data: bytes) -> "Request":
        splited_data = data.decode().split("\r\n\r\n", 1)
        head, body = (*splited_data,) if len(splited_data) > 1 else (*splited_data, "{}")
        deserialized_body: dict[str, str] = json.loads(body)
        head, *str_headers = head.split("\r\n")
        method, endpoint, _ = head.split(" ")
        headers = dict(map(lambda x: x.split(": "), str_headers))
        port: int | str
        host, port = headers.pop("Host").split(":")
        port = int(port)
        for key in ["Content-Type", "Content-type", "Content-Length"]:
            headers.pop(key, None)
        print(headers)
        return cls(method, host, port, endpoint, headers, deserialized_body)
