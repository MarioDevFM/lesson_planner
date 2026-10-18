# Lesson Plan Agent

The Lesson Plan Agent automatically creates a structured plan for the next
30-minute guitar lesson from the lesson history stored in Notion. It sends the
finished plan by email.

## How it works

The application performs these steps when it starts:

1. `notion_parser.py` reads the text blocks from the configured Notion page.
2. `planner.py` sends the history, the curriculum from `data/curriculum.yaml`,
   and the game ideas from `data/gitarrenspiele.yaml` to OpenAI
   (`gpt-4.1-mini`).
3. The language model creates a structured `LessonPlan` containing the current
   skill level, main topic, learning goals, exercise, and game activity.
4. `output.py` formats the plan as readable English text.
5. `mail_sender.py` sends the plan through the GMX SMTP server.

The model has no executable tools. It only creates the structured lesson-plan
content.

## Requirements

- Python 3.14
- an OpenAI API key
- a Notion integration with read access to the desired page
- a GMX email account for sending the plan

The Notion page must be shared with the integration. Otherwise, the API cannot
read its blocks.

## Installation

Open the repository in VS Code and install the locked dependencies from the
project directory with `uv`:

```powershell
uv sync --locked
```

Alternatively, install the project with `pip`:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e .
```

## Configuration

Create a file named `.env` in the project directory:

```dotenv
OPENAI_API_KEY=your_openai_api_key
NOTION_TOKEN=your_notion_integration_token
NOTION_PAGE_ID=your_notion_page_id
MAIL=sender@gmx.com
MAIL_PW=your_gmx_password
RECEIVER_MAIL=recipient@example.com
```

Never commit or log these values. The local `.env` file is therefore excluded
by `.gitignore`.

## Usage

With `uv`:

```powershell
uv run python -m unterrichtsplan
```

With the manually created virtual environment:

```powershell
.\.venv\Scripts\python.exe -m unterrichtsplan
```

After a successful run, `Email sent` appears in the terminal and the recipient
receives the generated lesson plan. The entry point intentionally rejects any
Python version other than Python 3.14.

## GitHub Actions automation

The `.github/workflows/weekly-lesson-plan.yml` workflow can be started manually
and is scheduled for Wednesdays at 17:00 in the `Europe/Berlin` time zone. For
production use, store the required values as repository secrets under
**Settings → Secrets and variables → Actions** and create the GitHub environment
named `production`.

Note: The current workflow still checks Google Calendar secrets from an earlier
development stage, while the application now uses Notion. Before automated use,
adjust the workflow's secret list to the Notion variables above. This does not
affect local execution.

## Project structure

| Path | Responsibility |
| --- | --- |
| `src/unterrichtsplan/__main__.py` | Connects the processing steps |
| `src/unterrichtsplan/notion_parser.py` | Reads the lesson history from Notion |
| `src/unterrichtsplan/planner.py` | Creates the lesson plan with the LLM |
| `src/unterrichtsplan/schemas.py` | Defines the plan's data structure |
| `src/unterrichtsplan/output.py` | Formats the structured plan |
| `src/unterrichtsplan/mail_sender.py` | Sends the plan by email |
| `data/curriculum.yaml` | Contains the subject-specific learning progression |
| `data/gitarrenspiele.yaml` | Contains age-appropriate game ideas |

## Known limitations

- The Notion request currently reads only the first result page and no nested
  child blocks.
- Errors while retrieving Notion data or sending email are printed but not
  propagated to the calling process.
- Generated plans are not stored locally.
