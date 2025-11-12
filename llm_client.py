# llm_client.py
# Small wrapper around an LLM. If GROQ_API_KEY is present, tries to use groq.
# Otherwise uses a deterministic stub for offline testing.

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# Try to import the groq client; if unavailable we'll fallback
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except Exception:
    GROQ_AVAILABLE = False

class LLMClient:
    def __init__(self):
        self.api_key = API_KEY
        self.client = None
        if self.api_key and GROQ_AVAILABLE:
            try:
                self.client = Groq(api_key=self.api_key)
            except Exception:
                self.client = None

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Sends prompt to the LLM provider. If no provider configured, returns a deterministic stub.
        """
        # If we have a real client, call it
        if self.client:
            try:
                resp = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",  # change to active model name if needed
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ],
                )
                # This path may vary depending on client response structure:
                # Attempt to extract model content safely.
                if hasattr(resp, "choices"):
                    return resp.choices[0].message.content
                if isinstance(resp, dict):
                    # fallback if dict
                    return resp.get("choices", [{}])[0].get("message", {}).get("content", "")
            except Exception as e:
                print("LLM call failed (provider) — falling back to stub. Error:", e)

        # Stubbed offline/dummy response (deterministic)
        # Use simple heuristics to produce plausible responses for each agent.
        p = prompt.lower()
        if "plan" in p or "break" in p or "create a plan" in p:
            return ("1) web_search: find relevant sources\n"
                    "2) analyze: extract key points\n"
                    "3) summarize: produce a concise summary")
        if "search" in p or "web search" in p:
            return "Found 3 sources: Source A (paper), Source B (blog), Source C (report). Key points: X, Y, Z."
        if "analyze" in p:
            return "Analysis: the content discusses agentic AI, orchestration patterns, and memory usage; main points: modularity, memory, evaluation."
        if "summarize" in p or "summary" in p:
            return "Summary: Agentic AI uses multiple agents to collaborate. Memory enables context retention and improved planning over time."
        if "evaluate" in p or "review" in p:
            return "Evaluation: Output is coherent but could use clearer examples and a list of tools. Score: 85/100."
        # default fallback
        return "I am a stub LLM response for prompt: " + (prompt[:200] + ("..." if len(prompt)>200 else ""))
