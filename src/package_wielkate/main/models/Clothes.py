import requests

from commons.constants import CLOTHES_MATCHING_API


class Clothes:
    def load_clothes(self) -> list[tuple[str, str]]:
        response = requests.get(f'{CLOTHES_MATCHING_API}/get_clothes')
        return [(item['filename'], item['color']) for item in response.json()]

    def add(self, filename: str, dominant_color: str) -> None:
        data = {
            "filename": filename,
            "color": dominant_color
        }
        requests.post(f'{CLOTHES_MATCHING_API}/add', data=data)

    def edit(self, filename: str, new_color: str) -> None:
        data = {
            "filename": filename,
            "new_color": new_color
        }
        requests.put(f'{CLOTHES_MATCHING_API}/edit', data=data)

    def delete(self, filename: str) -> None:
        requests.delete(f'{CLOTHES_MATCHING_API}/delete/{filename}')
