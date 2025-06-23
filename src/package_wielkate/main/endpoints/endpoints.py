from collections import defaultdict
from io import BytesIO

import requests

from resources.auth import CLOTHES_MATCHING_API, REMOVE_BG_API, REMOVE_BG_API_KEY, REMOVE_BG_API_PASS


# file
def upload_to_bucket(file):
    file.seek(0)
    requests.post(
        f'{CLOTHES_MATCHING_API}/upload',
        files={'file': file}
    )


def detect_color(filename, remove_background_response):
    image_bytes = BytesIO(remove_background_response.content)
    image_bytes.name = filename
    response = requests.post(
        f'{CLOTHES_MATCHING_API}/process_image/',
        files={'file': image_bytes}
    )
    return response.text


def remove_bg(file):
    return requests.post(
        REMOVE_BG_API,
        files={'image': file},
        data={'test': True},
        auth=(REMOVE_BG_API_KEY, REMOVE_BG_API_PASS)
    )


# colors
def load_color_names():
    response = requests.get(f'{CLOTHES_MATCHING_API}/get_color_names')
    return response.json()


# combinations
def load_combinations(mode):
    response = requests.get(f'{CLOTHES_MATCHING_API}/get_combinations/{mode}')
    grouped = defaultdict(list)
    for item in response.json():
        base_color = item['color']
        related_color = item['related_color']
        grouped[base_color].append(related_color)

    return grouped


# clothes
def load_clothes() -> list[tuple[str, str]]:
    response = requests.get(f'{CLOTHES_MATCHING_API}/get_clothes')
    return response.json()


def add_clothing_item(filename: str, dominant_color: str) -> None:
    data = {
        "filename": filename,
        "color": dominant_color
    }
    requests.post(f'{CLOTHES_MATCHING_API}/add', data=data)


def edit_clothing_item(filename: str, new_color: str) -> None:
    data = {
        "filename": filename,
        "new_color": new_color
    }
    requests.put(f'{CLOTHES_MATCHING_API}/edit', data=data)


def delete_clothing_item(filename: str) -> None:
    requests.delete(f'{CLOTHES_MATCHING_API}/delete/{filename}')
