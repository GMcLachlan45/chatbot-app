import { v4 as uuidv4 } from 'uuid'

export enum IPCMessageType {
    AGENT_RESPONSE,
    AGENT_QUERY
}

export class IPCMessage<MessageBodyType = any> {
    type: IPCMessageType
    body?: MessageBodyType
    id: string

    constructor(type: IPCMessageType, body?: any, id: string = uuidv4().replaceAll(/[^0-9a-fA-F]/g, "")) {
        this.type = type
        this.body = body
        this.id = id
    }
}