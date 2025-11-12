# agents/evaluator.py
from llm_client import LLMClient
from typing import List, Dict

class EvaluatorAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def review(self, results: List[Dict]) -> Dict:
        """
        Use LLM to produce evaluation and recommendations. Returns dictionary with score and comments.
        """
        combined = "\n\n".join([f"TASK {r['task']['id']} - {r['task']['type']}: {r['output']}" for r in results])
        prompt = f"Review the following task outputs. Provide (1) a short overall evaluation, (2) a score out of 100, and (3) recommendations to improve the summary.\n\n{combined}"
        resp = self.llm.generate(prompt)
        # basic parse
        return {"raw_review": resp}
