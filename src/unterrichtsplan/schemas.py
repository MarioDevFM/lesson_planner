"""Data structures for calendar content and lesson plans.

The dataclasses are initially drafts of the interfaces.
They do not validate values automatically. Add Pydantic models and domain
validation for structured LLM outputs later.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CalendarEntry:
    event_id: str
    status: str
    description: str
    updated: str


@dataclass(frozen=True)
class LessonPlan:
    """A structured lesson plan for a single guitar lesson."""
    current_level: str
    main_topic: str
    learning_goals: tuple[str, ...]
    song_or_exercise: str
    gane_or_activity: str

