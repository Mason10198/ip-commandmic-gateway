export type ConnectionPhase =
  | "disconnected"
  | "connecting"
  | "connected"
  | "recovering"
  | "failed";

export interface DisplayState {
  rawHex: string;
  primaryText: string;
  verifiedIndicators: readonly string[];
  verifiedDecimalPoints: readonly number[];
}

export interface CommandMicState {
  connection: ConnectionPhase;
  display: DisplayState;
  statusLed: "off" | "red" | "green" | "orange";
  heldControls: readonly string[];
  pttHeld: boolean;
  rxLevel: number;
  txLevel: number;
}

export type CommandMicAction =
  | { type: "key_down"; key: string }
  | { type: "key_up"; key: string }
  | { type: "ptt_down" }
  | { type: "ptt_up" }
  | { type: "set_audio_devices"; capture?: string; playback?: string };

export type CommandMicEvent =
  | { type: "state"; state: CommandMicState }
  | { type: "error"; message: string }
  | { type: "audio"; pcmS16leBase64: string };
