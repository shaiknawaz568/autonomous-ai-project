# 🤖 Autonomous Multi-Agent AI System with Memory

### Agentic AI Developer Certification – Module 3 Project  
**Built using Python, Groq API (Llama 3), and Persistent Memory**

---

## 🧩 Project Overview

This project demonstrates how an **Autonomous Multi-Agent AI System** can plan, execute, evaluate, and remember tasks over time — simulating how modern *Agentic AI frameworks* like LangGraph or CrewAI work.

Unlike a single LLM response, this system performs **multi-step reasoning** with collaboration between intelligent agents and **long-term memory** persistence.

---

## 🚀 Features

✅ **Planner Agent** – Creates a structured plan based on the user's goal  
✅ **Executor Agent** – Executes each task intelligently (search, analyze, summarize)  
✅ **Evaluator Agent** – Reviews results and gives improvement feedback  
✅ **Memory Agent** – Stores all goals, plans, and outputs in `memory_store.json`  
✅ **Autonomous Workflow** – Remembers previous goals and can continue from them  
✅ **Groq API Integration** – Uses Llama 3 for reasoning (or stub fallback if offline)

---

## 🧠 Example Run

```bash
🤖 Autonomous Multi-Agent System with Memory is running...

🧠 Previous goal found in memory: how to become a full stack developer
Would you like to continue from last goal? (y/n): y

[Planner] Creating plan...
Plan:
  - 1: 1)_web_search -> find relevant sources
  - 2: 2)_analyze -> extract key points
  - 3: 3)_summarize -> produce a concise summary

[Executor] Running tasks...

Result for task 1 (1)_web_search):
Found 3 sources: Source A (paper), Source B (blog), Source C (report).

Result for task 2 (2)_analyze):
Analysis: discusses skills, technologies, and steps to become a Full Stack Developer.

Result for task 3 (3)_summarize):
Summary: Learn front-end (HTML, CSS, React) and back-end (Node.js, databases); build projects that integrate both sides.

[Evaluator] Reviewing outputs...

✅ Run complete. All outputs stored in memory/memory_store.json
🏗️ Project Structure
bash
Copy code
autonomous_ai_project/
│
├── main_autonomous.py        # Main orchestrator file
├── llm_client.py             # Handles LLM (Groq or stub fallback)
│
├── agents/
│   ├── __init__.py
│   ├── planner.py            # Creates step-by-step plans
│   ├── executor.py           # Runs the tasks
│   ├── evaluator.py          # Reviews and improves outputs
│   └── memory_agent.py       # Stores and recalls memory
│
├── memory/
│   └── memory_store.json     # Persistent memory data
│
├── .env.example              # Placeholder for Groq API key
├── .gitignore                # Excludes .env and .venv from GitHub
└── requirements.txt          # Python dependencies
⚙️ Setup Instructions
1️⃣ Clone the repository
bash
Copy code
git clone https://github.com/shaiknawaz568/autonomous-ai-project.git
cd autonomous-ai-project
2️⃣ Create a virtual environment
bash
Copy code
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set up environment variables
Create a .env file:

ini
Copy code
GROQ_API_KEY=your_api_key_here
5️⃣ Run the system
bash
Copy code
python main_autonomous.py
🧩 Technologies Used
Python 3.11+

Groq API (Llama 3)

LangGraph-style Orchestration

Persistent Memory (JSON-based)

Modular Multi-Agent Architecture

💡 Real-World Applications
Domain	Example Use
AI Research	Autonomous literature review & summarization
Software Development	Multi-agent code refactoring assistant
Education	Smart study planner that remembers progress
Business	Automated project planning & progress review

🧾 Future Enhancements
Integrate vector database (e.g., FAISS) for advanced memory

Add user feedback loop to improve planning dynamically

Implement multi-session memory analysis

Extend to web-based interface using Streamlit or FastAPI

🧑‍💻 Author
Shaik Nawaz Shareef
Agentic AI Developer | Data Analyst | Full Stack Enthusiast
🌐 GitHub Profile
