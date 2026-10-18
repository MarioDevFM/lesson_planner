"""Planned passive output of validated plans to data/plans/.

TODO: Save as UTF-8 text or JSON. Determine the destination and filename only
in application code; do not accept a file path from the model.
Keep the calendar and lesson history unchanged. Do not execute HTML/code or
automatically retrieve external images or links.
"""

from dataclasses import asdict
from pathlib import Path

from .schemas import LessonPlan


HEADINGS = {
    "current_level": "Current Skill Level",
    "main_topic": "Main Topic",
    "learning_goals": "Learning Goals",
    "song_or_exercise": "Song or Exercise",
    "gane_or_activity": "Game or Activity",
}


def format_plan(plan: LessonPlan) -> str:
    """Format a lesson plan with German headings and blank lines."""
    sections = []
    lehrplan_daten = asdict(plan)

    for schluessel, wert in lehrplan_daten.items():
        sections.append(f"{HEADINGS[schluessel]}\n{wert}")

    return "\n\n".join(sections)


