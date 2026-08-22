import type { CommandMicAction, CommandMicEvent } from "../state/events.js";

export type CommandMicEventHandler = (event: CommandMicEvent) => void;

export interface CommandMicTransport {
  connect(): Promise<void>;
  close(): Promise<void>;
  send(action: CommandMicAction): Promise<void>;
  subscribe(handler: CommandMicEventHandler): () => void;
}
