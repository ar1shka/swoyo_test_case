import json
from dataclasses import dataclass, field


@dataclass
class Response:
    status_code: int
    info: str
    headers: dict[str, str] = field(default_factory=dict)
    body: dict[str, str] = field(default_factory=dict)

    def __str__(self) -> str:
        content = json.dumps(self.body)
        request = "\r\n".join(
            [
                f"HTTP/1.1 {self.status_code} {self.info}",
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
    def from_bytes(cls, data: bytes) -> "Response":
        splited_data = data.decode().split("\r\n\r\n", 1)
        head, body = (*splited_data,) if len(splited_data) > 1 else (*splited_data, "{}")
        deserialized_body: dict[str, str] = json.loads(body)
        head, *str_headers = head.split("\r\n")
        status_code: int | str
        _, status_code, *info = head.split(" ")
        concatenated_info = " ".join(info)
        status_code = int(status_code)
        headers = dict(map(lambda x: x.split(": "), str_headers))
        for key in ["Content-Type", "Content-type", "Content-Length"]:
            headers.pop(key, None)
        return cls(status_code, concatenated_info, headers, deserialized_body)
