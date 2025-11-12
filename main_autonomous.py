# main_autonomous.py
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_client import LLMClient
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.memory_agent import MemoryAgent
from agents.evaluator import EvaluatorAgent

def main():
    print("🤖 Autonomous Multi-Agent System with Memory is running...")
    llm = LLMClient()
    memory = MemoryAgent("memory/memory_store.json")
    planner = PlannerAgent(llm)
    executor = ExecutorAgent(llm)
    evaluator = EvaluatorAgent(llm)

    # 🔁 Memory recall section
    past_goal = memory.latest("goal")
    if past_goal:
        print(f"\n🧠 Previous goal found in memory: {past_goal['value']}")
        reuse = input("Would you like to continue from last goal? (y/n): ").strip().lower()
        if reuse == "y":
            goal = past_goal["value"]
        else:
            goal = input("Enter your new goal: ").strip()
    else:
        goal = input("Enter your goal: ").strip()

    if not goal:
        print("No goal provided — exiting.")
        return

    print("\n[Planner] Creating plan...")
    tasks = planner.create_plan(goal)
    print("Plan:")
    for t in tasks:
        print(f"  - {t['id']}: {t['type']} -> {t['description']}")
    memory.save("goal", goal)
    memory.save("plan", tasks)

    print("\n[Executor] Running tasks...")
    results = executor.run_tasks(tasks)
    for r in results:
        print(f"\nResult for task {r['task']['id']} ({r['task']['type']}):\n{r['output'][:500]}")
    memory.save("results", results)

    print("\n[Evaluator] Reviewing outputs...")
    review = evaluator.review(results)
    print("\nReview result:\n", review["raw_review"])
    memory.save("review", review)

    print("\n✅ Run complete. All outputs stored in memory/memory_store.json")

if __name__ == "__main__":
    main()
