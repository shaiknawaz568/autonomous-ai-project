# agents/executor.py
from llm_client import LLMClient
from typing import List, Dict

class ExecutorAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def _web_search(self, query: str) -> str:
        # In production: call a real web-search tool or RAG retrieval
        prompt = f"Perform a web search simulation for: {query}. Return a short list of sources and key points."
        return self.llm.generate(prompt)

    def _analyze(self, text: str) -> str:
        prompt = f"Analyze the following text and extract the most important points:\n\n{text}"
        return self.llm.generate(prompt)

    def _summarize(self, text: str) -> str:
        prompt = f"Write a concise summary (3-4 sentences) of the following content:\n\n{text}"
        return self.llm.generate(prompt)

    def run_tasks(self, tasks: List[Dict]) -> List[Dict]:
        results = []
        for t in tasks:
            ttype = t.get("type", "generic")
            desc = t.get("description", t.get("raw", ""))
            if "web_search" in ttype or "search" in ttype:
                out = self._web_search(desc)
            elif "analyze" in ttype:
                out = self._analyze(desc)
            elif "summarize" in ttype:
                out = self._summarize(desc)
            else:
                # generic: try to summarize description
                out = self._summarize(desc)
            results.append({"task": t, "output": out})
        return results
