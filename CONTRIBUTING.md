# Contributing

The gateway is the primary cross-platform application for the IP CommandMic
project. Contributions from people and coding agents are welcome when they are
reviewable, tested and honest about their verification boundary.

Protocol framing, message values, endpoint state machines and RTP behavior
belong in `ip-commandmic`. The gateway owns configuration, orchestration,
browser transport, authentication, presentation and application adapters.

Before opening a pull request:

1. Run `python -m pytest -q`.
2. Run `npm ci`, `npm run check` and `npm run build` under `frontend/`.
3. Keep remote listeners, audio and PTT disabled unless the relevant milestone
   safety requirements are implemented and tested.
4. Do not commit captures, codeplugs, credentials, serial numbers or voice.
5. Update `GATEWAY_PLAN.md` when a milestone capability changes status.

Generated contributions must be reviewed by the contributor. Remove planning
chatter, speculative claims and unused abstractions before submission.
