from langchain.agents import create_agent

from .models import model
from .schemas import LessonPlan
from pathlib import Path



SYSTEMPROMPT = """
You are a guitar teacher who teaches children in age of 11 to 13 who
creates lesson plans for the next guitar lesseon based on the lesson history.
First, infer the student's current learning level from the lesson history.
Then choose the logical next step on their learning path, considering required
prerequisites, topics that need review, and an age-appropriate progression
without unnecessary repetition or overly large learning jumps. Provide a song or exercise that is suitable for the student's current level and the next step in their learning path. The lesson plan should be structured and include 1-2 learning goals,
The lesson plan should be structured and include 1-2 learning goals,
a total of 30 minutes divided into phases, at most one main topic,
and limited text lengths. The lesson plan should be created in English. Consider that the student loves games rather than learning theory, and ensure the output is clear,
concise, and suitable for educational purposes.
"""

curriculum = Path("data/curriculum.yaml").read_text(encoding="utf-8")
games = Path("data/gitarrenspiele.yaml").read_text(encoding="utf-8")


def create_lesson_plan(history: str) -> LessonPlan:
    """Create a plan from the provided lesson history."""
    agent = create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEMPROMPT,
        response_format=LessonPlan,
    )

    plan = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Create the next lesson plan based on the following "
                        f"Consider the curriculum:\n{curriculum}\nAnd the history:\n{history} and {games}. Answer in English.\n"
                    ),
                }
            ]
        }
    )
    return plan["structured_response"]


