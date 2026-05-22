from typing import Dict, List
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, topic: str, websocket: WebSocket) -> None:
        await websocket.accept()
        self.active_connections.setdefault(topic, []).append(websocket)

    def disconnect(self, topic: str, websocket: WebSocket) -> None:
        if topic in self.active_connections:
            self.active_connections[topic].remove(websocket)
            if not self.active_connections[topic]:
                self.active_connections.pop(topic, None)

    async def broadcast(self, topic: str, message: dict) -> None:
        for connection in self.active_connections.get(topic, []):
            await connection.send_json(message)

manager = ConnectionManager()
