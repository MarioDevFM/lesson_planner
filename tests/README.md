# Planned Tests

Add tests here as the corresponding functions are implemented.

- The reader retrieves only the configured calendar/event pair.
- A missing or deleted event aborts the run without a fallback search.
- Empty or excessively long calendar text is rejected before the model call.
- Model responses with an invalid duration or structure are not stored.
- Manipulated lesson notes cannot trigger external actions.
- Errors cause neither an infinite loop nor requests for other events.

Replace Google and LLM clients with fakes in these tests.
Never place real credentials or lesson content in test files.
