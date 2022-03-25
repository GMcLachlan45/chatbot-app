import { ipcMain } from "electron";
import { AgentIPC } from "../agent/agent-ipc";
import { IPCMessage } from "../../../shared/ipc-message";

export class RendererIPC {
    agent: AgentIPC

    constructor(agent: AgentIPC) {
        this.agent = agent
    }

    init() {
        ipcMain.on('agent-ipc', async (event, message: IPCMessage) => {
            message = new IPCMessage(message.type, message.body, message.id)
            this.relayMessage(event, message)
        });
    }

    relayMessage(event: any, message: IPCMessage) {
        // relay ipc message to python
        this.agent.send(message, (response: IPCMessage) => {
            event.reply('agent-ipc', response.body)
        })
    }
}