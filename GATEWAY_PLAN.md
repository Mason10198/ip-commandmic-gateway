# Unified gateway implementation plan

## Product outcome

One locally installed service provides both supported `ip-commandmic` endpoint
roles through one responsive PWA. A user installs the gateway once on a computer
attached to the radio LAN, completes a guided local setup, and may then use that
computer or another authorized browser as the CommandMic interface.

The gateway is the primary end-user product. Desktop and Lab remain reference
applications and conformance instruments; they do not receive independent UI
feature development unless required for diagnostics or hardware validation.

## Non-negotiable architecture

```text
browser/PWA
  -> HTTPS + authenticated control WebSocket + bounded audio transport
  -> local Python gateway
  -> ip-commandmic 1.x public endpoint
  -> real radio OR physical CommandMic
```

- Exactly one hardware role runs at a time.
- The browser receives semantic state, never raw protocol frames by default.
- The gateway owns endpoint lifecycle, settings, audits and all safety timers.
- `ip-commandmic` remains the only owner of CommandMic wire framing and RTP.
- Browser disconnect, ownership loss, endpoint failure and service shutdown
  immediately release controls/PTT and discard stale audio.

## Milestone 0 — repository and contracts

- [x] Rename the Web scaffold and Python namespace to `ip-commandmic-gateway`.
- [x] Depend on stable `ip-commandmic>=1.0,<2`.
- [x] Fold the useful UI scaffold into this repository; retire the separate UI
  package after migration so normal development has one product codebase.
- [ ] Reconcile Python/browser contracts into one generated or schema-validated
  role-neutral action/event/state definition.
- [x] Add CI for Python 3.11/3.14 on Linux/Windows and frontend type/build checks.

Exit gate: clean install, import, configuration validation and static PWA build
pass without opening hardware, remote listeners, audio devices or PTT.

## Milestone 1 — local CommandMic mode

- Localhost-only HTTP server and setup page.
- Start/stop `SoftwareCommandMicEndpoint` from validated settings.
- WebSocket snapshots/events for connection, display, LEDs and controls.
- Browser key press/hold/release with ownership and focus-loss release.
- No PTT and no remote binding in this milestone.

Exit gate: software-radio loopback and real-radio receive/control matrix pass;
closing the browser or gateway leaves every control released.

## Milestone 2 — local audio and guarded PTT

- Browser receive-audio playout with bounded queues and visible metrics.
- Browser microphone capture converted to continuous 8 kHz s16be frames through
  `BufferedMicrophoneSource`.
- Explicit local TX arming, press-and-hold PTT, maximum-hold watchdog and
  immediate release on WebSocket/audio/endpoint failure.
- One control owner; observer sessions cannot transmit.

Exit gate: hardware-free impairment/recovery, real-radio contained RX/TX audio,
PTT disconnect/focus-loss tests and no stale/post-stop media.

## Milestone 3 — Radio/Lab mode

- Start/stop `SoftwareRadioEndpoint` instead of the CommandMic endpoint.
- Display/LED/backlight/gain/volume controls, physical key/PTT events, absolute
  audio statistics, recording, playback and Parrot workflow.
- Expert raw frames remain locally gated and unavailable to remote sessions.

Exit gate: reproduce the accepted Lab alpha.33 functional matrix and bounded
recovery/stability gates through the PWA with the real radio disconnected.

## Milestone 4 — secure LAN clients and installable PWA

- First-run administrator credential or pairing code.
- HTTPS with explicit certificate/bootstrap guidance.
- Secure cookies/tokens, origin checks, rate limits and audit records.
- Exclusive renewable control lease; additional clients are read-only until
  ownership is deliberately transferred.
- Installable PWA, responsive layouts and reconnect without stale state.

Exit gate: unauthorized clients cannot observe/control; ownership expiry and
network loss fail closed; phone/tablet/desktop browser matrix passes.

## Milestone 5 — easy distribution

- Publish the Python package for `pip`/`pipx` users.
- Windows installer that bundles Python/runtime, registers firewall rules only
  with consent and launches the local setup page.
- Linux systemd package and Docker image; validate first in an Ubuntu VM.
- macOS remains source-supported until a real Mac tester accepts networking,
  audio, sleep/wake, signing and notarization.
- Add backup/restore for settings and a safe update notification path.

Exit gate: a non-developer can install, configure, use and uninstall without
managing Python, while advanced users can deploy the identical service via pip
or container.

## Deferred beyond the first gateway release

- Internet-facing operation, cloud relay and unattended remote PTT.
- Multi-radio/multi-CommandMic coordination.
- Advanced CPS semantics not present in the stable library contract.
- Emergency, destructive and firmware-sensitive functions.
- macOS binary claims without real-hardware qualification.
