"""Tests for reading lesson history from Notion blocks."""

import os
from unittest import TestCase
from unittest.mock import Mock, patch

from unterrichtsplan.notion_parser import block_parser, parse_text_from_block


class ParseTextFromBlockTests(TestCase):
    def test_combines_rich_text_fragments(self) -> None:
        block = {
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"plain_text": "Practiced "},
                    {"plain_text": "chord changes."},
                ]
            },
        }

        self.assertEqual(
            parse_text_from_block(block),
            "Practiced chord changes.",
        )


class BlockParserTests(TestCase):
    @patch("unterrichtsplan.notion_parser.notion")
    def test_reads_configured_notion_page(self, notion: Mock) -> None:
        notion.blocks.children.list.return_value = {
            "results": [
                {
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"plain_text": "Practiced chords."}]
                    },
                },
                {
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"plain_text": "Next lesson"}]
                    },
                },
            ]
        }

        with patch.dict(os.environ, {"NOTION_PAGE_ID": "test-page-id"}):
            history = block_parser()

        notion.blocks.children.list.assert_called_once_with(
            block_id="test-page-id"
        )
        self.assertEqual(history, "Practiced chords. Next lesson")
