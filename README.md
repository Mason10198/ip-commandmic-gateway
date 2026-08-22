# IP CommandMic Gateway

The primary cross-platform application for the IP CommandMic project. One
Python service runs on the radio LAN and serves an installable browser UI to
Windows, Linux, macOS, phones and tablets.

The gateway has two mutually exclusive operating roles:

- **CommandMic mode** replaces the physical CommandMic and connects to a real
  F5330D/F6330D radio through `SoftwareCommandMicEndpoint`.
- **Radio/Lab mode** replaces the radio and operates a physical CommandMic
  through `SoftwareRadioEndpoint`.

Browsers never open the raw CommandMic TCP/UDP sockets. They exchange
authenticated semantic state, controls and bounded audio with the local gateway.
All wire behavior remains owned by stable [`ip-commandmic 1.x`](https://pypi.org/project/ip-commandmic/).

## Intended installation

Developer and server installation:

```bash
python -m pip install "ip-commandmic-gateway[audio]"
ip-commandmic-gateway
```

The service will open a local setup page and can optionally serve authorized
clients elsewhere on the LAN. Ordinary users will later receive installers
built from this same codebase: Windows installer, Linux package/container and a
macOS package only after real-Mac qualification.

## Current status

Architecture and safety-contract scaffold. The service is not operational yet.
Raw radio control, remote clients, audio and PTT remain disabled until their
individual acceptance gates in [GATEWAY_PLAN.md](GATEWAY_PLAN.md) pass.

The already-published Desktop and Lab applications remain reference clients,
diagnostic fallbacks and physical conformance tools while gateway development
progresses.
