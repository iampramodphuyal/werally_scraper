
import json
import os
import re
import random
from pathlib import Path
from typing import Any
from .config import STATIC_FILE_PATH, OUTPUT_FILE_PATH, US_TIMEZONES


def create_dir(path:str):
    os.makedirs(path, exist_ok=True);

def get_random_timezone() -> str:
    """Return a random U.S. time zone from the list."""
    return random.choice(US_TIMEZONES)

def normalize_text(text: str) -> str:
    """Lowercase and remove all non-alphanumeric characters."""
    return re.sub(r'[^a-z0-9]', '', text.lower())

def get_state_id(state:str):
    """
    Get State ID from static JSON file based on state abbreviation
    Args:
        state (str): State abbreviation
    Returns:
        str | None: The state ID if found, else None
    """
    data = json.loads(Path("output/static/state_data.json").read_text(encoding="utf-8"))
    
    return next(
        (child.get("nodeId") for child in data.get("children", [])
         if child.get("staticContent") == state),
        None
    )


def init_tmp_path():
    """
    Method to initialize the final output dirs. Creates dirs if not already created
    """
    os.makedirs(STATIC_FILE_PATH, exist_ok=True) # For cache, static files
    os.makedirs(OUTPUT_FILE_PATH, exist_ok=True) # For final output data


def save_to_json(full_file_path:str, content:Any):
    """
    Save content to a JSON file.
    Args:
        full_file_path (str): The full path where the JSON file will be saved
        content (Any): The content to save in JSON format
    """
    with open(full_file_path, 'w') as f:
        json.dump(content, f, ensure_ascii=False)
