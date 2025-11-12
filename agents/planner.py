# agents/planner.py
from llm_client import LLMClient
from typing import List

class PlannerAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def create_plan(self, goal: str) -> List[dict]:
        """
        Use LLM to break the goal into a list of tasks.
        Returns a list of task dicts: {"id": 1, "type": "web_search", "params": {...}}
        """
        prompt = f"Given this goal: '{goal}', create a short ordered plan with 3-5 simple tasks. " \
                 "Return each task on its own line with format: TASK_TYPE: brief description."
        resp = self.llm.generate(prompt)
        # Very light parsing of the stubbed LLM response
        lines = [l.strip() for l in resp.splitlines() if l.strip()]
        tasks = []
        for i, line in enumerate(lines, start=1):
            if ":" in line:
                typ, desc = line.split(":", 1)
                typ = typ.strip().lower().replace(" ", "_")
                tasks.append({"id": i, "type": typ, "description": desc.strip(), "raw": line})
            else:
                # fallback: assign generic task
                tasks.append({"id": i, "type": "generic", "description": line, "raw": line})
        return tasks
