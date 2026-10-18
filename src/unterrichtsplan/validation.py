import os
from .config import EVENT_ID_ENV, MAX_INPUT_CHARACTERS
from .schemas import CalendarEntry, LessonPlan


def validate_input(entry: CalendarEntry) -> str:
    """Return safe lesson text from the configured, confirmed event."""
    expected_event_id = os.getenv(EVENT_ID_ENV)
    if not expected_event_id:
        raise RuntimeError(f"{EVENT_ID_ENV} must be configured.")
    if entry.event_id != expected_event_id:
        raise ValueError("Unexpected event ID.")
    if entry.status != "confirmed":
        raise ValueError("The calendar event is not confirmed.")

    description = entry.description.strip()
    if not description:
        raise ValueError("The description must not be empty.")
    if len(description) > MAX_INPUT_CHARACTERS:
        raise ValueError(
            f"The description must not exceed {MAX_INPUT_CHARACTERS} characters."
        )

    return description


def validate_plan(plan: LessonPlan) -> LessonPlan:
    """Eventually return only a plan that is valid according to the rules."""
    raise NotImplementedError("Output validation has not been implemented yet.")
