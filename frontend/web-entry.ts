import { WebSocketTransport } from "./src/index.js";

export function gatewayTransport(path = "/ws"): WebSocketTransport {
  const scheme = window.location.protocol === "https:" ? "wss:" : "ws:";
  return new WebSocketTransport(`${scheme}//${window.location.host}${path}`);
}
