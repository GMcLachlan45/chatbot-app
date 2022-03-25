import json
import string
import uuid
import re

class IPCMessage():
    type: int
    body: str
    id: str

    def __init__(self, type: int, body: str = None, id: str = re.sub(r'[^A-Fa-f0-9]', "", str(uuid.uuid4()))):
        self.type = type
        self.body = body
        self.id = id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def deserialize(data: bytes):
        more_packets = bool(data[0] & (1 << 7))  # true if more packets exist for same message
        type = data[0] & 0b01111111
        id = data[2:2+data[1]].hex()
        if(len(data) <= 2+data[1]):
            body = None
        else:
            body = data[2+data[1]:].decode("utf-8")
        
        return IPCMessage(type, json.loads(body), id)

    def serialize(self):
        id_bytes = bytearray.fromhex(self.id)
        descriptor = [0b00000000 & self.type, len(id_bytes)]
        return bytearray(descriptor) + id_bytes + json.dumps(self.body).encode("utf-8")

