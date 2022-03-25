from abc import ABC, abstractmethod

class IPCMessageHandler(ABC):
    @abstractmethod
    def handle_message(ipc_pipe, message):
        pass