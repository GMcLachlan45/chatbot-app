from agent import Agent
from ipc.ipc_message import IPCMessage
from ipc.ipc_pipe import IPCPipe
from ipc.ipc_message_handler import IPCMessageHandler

MESSAGE_TYPE = {
    "AGENT_RESPONSE": 0,
    "AGENT_QUERY": 1,
}

class MessageHandler(IPCMessageHandler):
    def __init__(self, agent: Agent):
        self.agent = agent

    def handle_message(self, ipc_pipe: IPCPipe, message: IPCMessage):
        if (message.type == MESSAGE_TYPE["AGENT_QUERY"]):
            agent_response = self.agent.query(message.body)
            
            ipc_pipe.send_message(
                MESSAGE_TYPE["AGENT_RESPONSE"], 
                agent_response,
                message.id
            )