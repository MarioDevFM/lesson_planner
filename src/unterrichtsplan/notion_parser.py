import os
from dotenv import load_dotenv
from notion_client import Client
import logging

# Load the .env file (including environment variables such as NOTION_TOKEN).
load_dotenv()

# Initialize the Notion client.
notion = Client(auth=os.environ.get("NOTION_TOKEN"))

def parse_text_from_block(block):
    """Dynamically extract text from different Notion block types."""
    block_type = block.get("type")
    if not block_type:
        return ""

    # Get the data specific to the block type (e.g. paragraph or heading_1).
    block_content = block.get(block_type, {})
    rich_text = block_content.get("rich_text", [])

    # Combine the individual text fragments.
    text = "".join([t.get("plain_text", "") for t in rich_text])
    return text

def block_parser():
    # Example ID of a Notion page or block (from an environment variable or directly).
    block_id = os.environ.get("NOTION_PAGE_ID", "YOUR_BLOCK_OR_PAGE_ID")

    print(f"Retrieving child blocks for block ID: {block_id}...")

    try:
        # Retrieve all child blocks (equivalent to notion.blocks.children.list).
        response = notion.blocks.children.list(block_id=block_id)
        results = response.get("results", [])

        for block in results:
            block_type = block.get("type", "unknown")
            text_content = parse_text_from_block(block)

            if text_content:
                logging.info("lesson history text extracted from Notion block")

    except Exception as e:
        print(f"Failed to retrieve Notion data: {e}")

    return " ".join([parse_text_from_block(block) for block in results])

if __name__ == "__main__":
    block_parser()
