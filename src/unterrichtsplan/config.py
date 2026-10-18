"""Trusted settings; never load them from calendar text or an LLM response.

Calendar settings are re-exported for backward compatibility.
Constants are not a security boundary against manipulated Python code.
"""

from google_calendar.config import (
    CALENDAR_API_BASE_URL,
    CALENDAR_ID_ENV,
    CALENDAR_READONLY_SCOPE,
    CALENDAR_REQUEST_TIMEOUT_SECONDS,
    EVENT_ID_ENV,
    GOOGLE_ACCESS_TOKEN_ENV,
    GOOGLE_CLIENT_ID_ENV,
    GOOGLE_CLIENT_SECRET_ENV,
    GOOGLE_REFRESH_TOKEN_ENV,
    GOOGLE_TOKEN_URL,
)

LESSON_MINUTES: int = 60
MAX_LEARNING_GOALS: int = 2
MAX_INPUT_CHARACTERS: int = 20_000
MAX_MODEL_CALLS: int = 1
MODEL_TIMEOUT_SECONDS: int = 60
