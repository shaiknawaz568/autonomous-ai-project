# agents/memory_agent.py
import json
import os
from typing import Any, Optional

class MemoryAgent:
    def __init__(self, path: str = "memory/memory_store.json"):
        self.path = path
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({"events": []}, f, indent=2)

    def save(self, key: str, value: Any):
        with open(self.path, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.setdefault("events", []).append({"key": key, "value": value})
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

    def get_all(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def latest(self, key: Optional[str] = None):
        data = self.get_all()
        events = data.get("events", [])
        if key is None:
            return events[-1] if events else None
        for e in reversed(events):
            if e.get("key") == key:
                return e
        return None
