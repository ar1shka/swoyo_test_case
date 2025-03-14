import base64
import json

import toml

from http_client import Request, send_sms

from .parser import parse_args

if __name__ == "__main__":
    args = parse_args()
    config: dict[str, str] = toml.load(args.pop("config_file"))
    port: int | str
    host, port = config["address"].split(":")
    port = int(port)
    credentials = f"{config['username']}:{config['password']}"
    headers = {"Authorization": f"Basic {base64.b64encode(credentials.encode()).decode()}"}
    request = Request("post", host, port, "/send_sms", headers, args)

    response = send_sms(request)
    print(response.status_code, json.dumps(response.body, indent=2), sep="\n")
