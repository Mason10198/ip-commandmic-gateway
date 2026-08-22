# IP CommandMic Gateway

The primary cross-platform application for the IP CommandMic project. One
Python service runs on the radio LAN and serves an installable browser UI to
Windows, Linux, macOS, phones and tablets.

The gateway is also the intended integration host. Beyond reproducing a single
CommandMic, future adapters can bridge audio and controls to AllStarLink, expose
automation APIs, or arbitrate one CommandMic across multiple radios. Those
capabilities are planned—not present in the current scaffold.

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

## Capability status

| Capability | Status |
|---|---|
| Installable Python package and safe configuration validation | Implemented |
| Shared browser state/transport contracts | Initial implementation; schema unification remains |
| Local web service and live hardware session | Not implemented |
| Browser display, controls and connection state | Not implemented |
| Browser audio and guarded PTT | Not implemented |
| Radio/Lab mode | Not implemented |
| Authenticated LAN clients and installable PWA | Not implemented |
| AllStarLink adapter | Planned after the single-endpoint gateway works |
| Multi-radio arbitration | Planned after the single-endpoint gateway works |
| Windows/Linux end-user installers | Planned |

See [GATEWAY_PLAN.md](GATEWAY_PLAN.md) for milestone boundaries and safety gates.

## Contributing

Issues and pull requests are welcome. Keep protocol behavior in
[`ip-commandmic`](https://github.com/Mason10198/ip-commandmic); this repository
owns service lifecycle, browser transport, authentication, orchestration and UI.
Run the Python tests and frontend checks before submitting:

```bash
python -m pytest -q
cd frontend
npm ci
npm run check
npm run build
```
