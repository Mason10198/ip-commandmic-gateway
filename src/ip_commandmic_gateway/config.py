from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GatewayConfig:
    """Safe network-facing configuration independent of server framework."""

    host: str = "127.0.0.1"
    port: int = 8765
    allow_remote_clients: bool = False
    enable_ptt: bool = False

    def validate(self) -> None:
        if not self.host.strip():
            raise ValueError("gateway host must not be empty")
        if not 1 <= self.port <= 65535:
            raise ValueError("gateway port must be between 1 and 65535")
        if self.allow_remote_clients and self.host in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("remote clients require a non-loopback bind address")
