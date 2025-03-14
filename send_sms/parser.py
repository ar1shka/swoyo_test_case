from argparse import ArgumentParser


def parse_args() -> dict[str, str]:
    argument_parser = ArgumentParser(
        prog="send_sms", description="Send the message from sender to recipient"
    )
    argument_parser.add_argument(
        "--sender",
        help="message from",
        type=str,
        required=True,
        dest="sender",
    )
    argument_parser.add_argument(
        "--recipient",
        help="message to",
        type=str,
        required=True,
        dest="recipient",
    )
    argument_parser.add_argument(
        "--message",
        help="message to send",
        type=str,
        required=True,
        dest="message",
    )
    argument_parser.add_argument(
        "--config-file",
        help="path to configuration file",
        type=str,
        required=False,
        default="./configuration/config.toml",
        dest="config_file",
    )
    return vars(argument_parser.parse_args())
