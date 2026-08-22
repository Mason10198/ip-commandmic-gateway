from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


BrowserActionKind = Literal[
    "key_down", "key_up", "ptt_down", "ptt_up", "set_audio_devices"
]
BrowserEventKind = Literal["state", "error", "audio"]


@dataclass(frozen=True, slots=True)
class BrowserAction:
    kind: BrowserActionKind
    data: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True, slots=True)
class BrowserEvent:
    kind: BrowserEventKind
    data: dict[str, Any] = field(default_factory=dict)
