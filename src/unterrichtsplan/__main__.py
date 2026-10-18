"""Entry point of the skeleton; makes no API calls."""

import sys

from dotenv import load_dotenv

# from google_calendar.calendar_reader import read_fixed_event as read_calendar
from .output import format_plan
from .planner import create_lesson_plan
from .mail_sender import sent_mail
from .notion_parser import block_parser

import logging

def main() -> None:
    """Check the Python version and display the development status."""
    if sys.version_info[:2] != (3, 14):
        raise SystemExit("Run this project with Python 3.14.")

    load_dotenv()

    # history = read_calendar().description
    notion_history = block_parser()
    lesson_plan = create_lesson_plan(notion_history)
    formated_plan = format_plan(lesson_plan)


    sent_mail(plan=str(formated_plan))



if __name__ == "__main__":
    main()


#TODO: Human in the loop: add ad stetp to ask the user create a new lession plan with "Does this lesson plan look good to you? (y/n)" and if the user says no, then ask "What would you like to change?" and then use that input to create a new lesson plan.
# source: https://academy.langchain.com/courses/take/foundation-introduction-to-deepagents/multimedia/76263203-lesson-8-hitl


