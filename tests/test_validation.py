"""Tests for validation at the boundary between calendar data and the model."""

import os
from unittest import TestCase
from unittest.mock import patch

from unterrichtsplan.config import EVENT_ID_ENV
from unterrichtsplan.schemas import CalendarEntry
from unterrichtsplan.validation import validate_input


class ValidateInputTests(TestCase):
    def setUp(self) -> None:
        self.event_id = "test-event-id"
        environment = patch.dict(os.environ, {EVENT_ID_ENV: self.event_id})
        environment.start()
        self.addCleanup(environment.stop)

    def make_entry(
        self,
        *,
        event_id: str | None = None,
        status: str = "confirmed",
        description: str = "Lesson taught: Practiced chord changes.",
    ) -> CalendarEntry:
        """Create a valid entry whose relevant fields a test can override."""
        return CalendarEntry(
            event_id=event_id or self.event_id,
            status=status,
            description=description,
            updated="2026-09-19T10:00:00Z",
        )

    def test_rejects_unexpected_event_id(self) -> None:
        entry = self.make_entry(event_id="another-event")

        with self.assertRaisesRegex(ValueError, "event ID"):
            validate_input(entry)


    def test_rejects_blank_description(self) -> None:
        entry = self.make_entry(description=" \n\t ")

        with self.assertRaisesRegex(ValueError, "description"):
            validate_input(entry)
