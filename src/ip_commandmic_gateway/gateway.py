from __future__ import annotations

from typing import Protocol

from .contracts import BrowserAction, BrowserEvent


class BrowserSession(Protocol):
    """Framework-neutral session used by future WebSocket/WebRTC adapters."""

    async def receive(self) -> BrowserAction: ...

    async def send(self, event: BrowserEvent) -> None: ...


class CommandMicGateway(Protocol):
    """Semantic boundary; concrete implementations must use `ip_commandmic`."""

    async def start(self) -> None: ...

    async def stop(self) -> None: ...

    async def serve(self, session: BrowserSession) -> None: ...
