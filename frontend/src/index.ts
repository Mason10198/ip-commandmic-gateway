export type {
  CommandMicAction,
  CommandMicEvent,
  CommandMicState,
  ConnectionPhase,
  DisplayState,
} from "./state/events.js";
export type {
  CommandMicEventHandler,
  CommandMicTransport,
} from "./transport/transport.js";
export { WebSocketTransport } from "./transport/websocket.js";
