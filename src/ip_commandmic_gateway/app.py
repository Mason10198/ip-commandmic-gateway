from __future__ import annotations

import argparse

from . import __version__
from .config import GatewayConfig


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="IP CommandMic Gateway")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "--check-config",
        action="store_true",
        help="validate the safe default configuration without starting services",
    )
    args = parser.parse_args(argv)
    if args.check_config:
        GatewayConfig().validate()
        print("safe default configuration: valid")
        return 0
    parser.error("the gateway service is not operational yet; see GATEWAY_PLAN.md")


if __name__ == "__main__":
    raise SystemExit(main())
