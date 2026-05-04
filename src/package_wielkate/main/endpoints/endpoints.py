from io import BytesIO

import requests

from models.Tag import Tag
from resources.auth import CLOTHES_MATCHING_API, REMOVE_BG_API, REMOVE_BG_API_KEY, REMOVE_BG_API_PASS


# file
def upload_to_bucket(file):
    try:
        file.seek(0)
        response = requests.post(
            f'{CLOTHES_MATCHING_API}/upload',
            files={'file': file}
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error uploading to bucket: {e}")


def detect_color(filename, remove_background_response):
    try:
        image_bytes = BytesIO(remove_background_response.content)
        image_bytes.name = filename
        response = requests.post(
            f'{CLOTHES_MATCHING_API}/process_image/',
            files={'file': image_bytes}
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error detecting color: {e}")
        return ""


def detect_tag(filename, remove_background_response):
    try:
        image_bytes = BytesIO(remove_background_response.content)
        image_bytes.name = filename
        response = requests.post(
            f'{CLOTHES_MATCHING_API}/tag/',
            files={'file': image_bytes}
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error detecting tag: {e}")
        return Tag.UNKNOWN.value


def remove_bg(file):
    try:
        return requests.post(
            REMOVE_BG_API,
            files={'image': file},
            data={'test': True},
            auth=(REMOVE_BG_API_KEY, REMOVE_BG_API_PASS)
        )
    except requests.RequestException as e:
        print(f"Error removing background: {e}")
        return None


# colors
def load_color_names():
    try:
        response = requests.get(f'{CLOTHES_MATCHING_API}/get_color_names')
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error loading color names: {e}")
        return []


# clothes
def load_clothes() -> list[tuple[str, str]]:
    try:
        response = requests.get(f'{CLOTHES_MATCHING_API}/get_clothes')
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error loading clothes: {e}")
        return []


def add_clothing_item(filename: str, dominant_color: str, tag: str) -> None:
    try:
        data = {
            "filename": filename,
            "color": dominant_color,
            "tag": tag
        }
        response = requests.post(f'{CLOTHES_MATCHING_API}/add', data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error adding clothing item: {e}")


def edit_clothing_item(filename: str, new_color: str) -> None:
    try:
        data = {
            "filename": filename,
            "new_color": new_color
        }
        response = requests.put(f'{CLOTHES_MATCHING_API}/edit', data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error editing clothing item: {e}")


def delete_clothing_item(filename: str) -> None:
    try:
        response = requests.delete(f'{CLOTHES_MATCHING_API}/delete/{filename}')
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error deleting clothing item: {e}")


# matched cards
def get_matched_colors(mode: str, color: str):
    try:
        data = {
            "mode": mode,
            "color": color
        }
        response = requests.post(f'{CLOTHES_MATCHING_API}/get_combinations', data=data)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error getting matched colors: {e}")
        return []


def get_ids(colors: list[str], exclude_id: str):
    try:
        data = {
            "colors": colors,
            "exclude_id": exclude_id
        }
        response = requests.post(f'{CLOTHES_MATCHING_API}/get_ids', data=data)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error getting IDs: {e}")
        return []
