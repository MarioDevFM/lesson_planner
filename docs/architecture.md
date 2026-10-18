# Architecture and Implementation Boundaries

The project provides a fixed LangChain workflow: read source data, validate the input, create a plan, validate the output, and deliver the result separately. An external scheduler controls weekly execution.

## Responsibilities

| Module | Responsibility |
| --- | --- |
| `config.py` | Configuration names and fixed limits |
| `notion_parser.py` | Read lesson history from Notion |
| `schemas.py` | Define input and output structures |
| `validation.py` | Validate data and lesson-plan rules |
| `planner.py` | Call the model without executable tools |
| `output.py` | Format the plan as passive data |
| `mail_sender.py` | Deliver the plan by email |
| `workflow.py` | Control steps and failure behavior |

## Security boundaries

Separating modules separates responsibilities, not processes. Credentials must never enter prompts. The model receives lesson text, but that content remains untrusted; validation does not eliminate prompt injection. Model output is never executed as code, a tool call, a path, or system configuration. The plan remains a proposal for teacher review.

## History

The user maintains the relevant history in Notion. Generated plans are not records of lessons actually taught and are not added to the history automatically.
