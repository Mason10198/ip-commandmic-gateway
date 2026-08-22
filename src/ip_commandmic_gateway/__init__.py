"""Cross-platform gateway boundary for the IP CommandMic product family."""

from .config import GatewayConfig
from .contracts import BrowserAction, BrowserEvent

__all__ = ("BrowserAction", "BrowserEvent", "GatewayConfig")
__version__ = "0.1.0a1"
