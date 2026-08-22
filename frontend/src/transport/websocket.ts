import type { CommandMicAction, CommandMicEvent } from "../state/events.js";
import type { CommandMicEventHandler, CommandMicTransport } from "./transport.js";

export class WebSocketTransport implements CommandMicTransport {
  readonly #handlers = new Set<CommandMicEventHandler>();
  #socket: WebSocket | undefined;

  constructor(readonly url: string) {}

  async connect(): Promise<void> {
    if (this.#socket) return;
    const socket = new WebSocket(this.url);
    this.#socket = socket;
    socket.addEventListener("message", (message) => {
      const event = JSON.parse(String(message.data)) as CommandMicEvent;
      for (const handler of this.#handlers) handler(event);
    });
    await new Promise<void>((resolve, reject) => {
      socket.addEventListener("open", () => resolve(), { once: true });
      socket.addEventListener("error", () => reject(new Error("WebSocket connection failed")), { once: true });
    });
  }

  async close(): Promise<void> {
    this.#socket?.close();
    this.#socket = undefined;
  }

  async send(action: CommandMicAction): Promise<void> {
    if (this.#socket?.readyState !== WebSocket.OPEN) {
      throw new Error("WebSocket transport is not connected");
    }
    this.#socket.send(JSON.stringify(action));
  }

  subscribe(handler: CommandMicEventHandler): () => void {
    this.#handlers.add(handler);
    return () => this.#handlers.delete(handler);
  }
}
