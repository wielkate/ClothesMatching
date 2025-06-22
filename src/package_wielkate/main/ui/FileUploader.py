import logging
from io import BytesIO

import requests
from flet.core.file_picker import FilePicker, FilePickerResultEvent, FilePickerFileType
from flet.core.page import Page

from src.package_wielkate.main.commons.constants import REMOVE_BG_API, CLOTHES_MATCHING_API
from src.package_wielkate.main.resources.auth import REMOVE_BG_API_KEY, REMOVE_BG_API_PASS

logger = logging.getLogger(__name__)


def upload_to_bucket(file):
    file.seek(0)
    bucket_url = requests.post(
        f'{CLOTHES_MATCHING_API}/upload',
        files={'file': file}
    ).json()
    logger.info(bucket_url.get('url'))


def delete_from_bucket(filename):
    bucket_url = requests.delete(
        f'{CLOTHES_MATCHING_API}/delete/{filename}',
    ).json()
    logger.info(bucket_url.get('message'))


def detect_color(filename, remove_background_response):
    image_bytes = BytesIO(remove_background_response.content)
    image_bytes.name = filename
    color_response = requests.post(
        f'{CLOTHES_MATCHING_API}/process_image/',
        files={'file': image_bytes}
    ).json()
    color_name = color_response.get('color')
    return color_name


class FileUploader:
    def __init__(self, add_new_item_action):
        self.file_picker = FilePicker(on_result=self.file_picker_result)
        self.add_new_item_action = add_new_item_action

    def file_picker_result(self, e: FilePickerResultEvent):
        if e.files is not None:
            for file in e.files:
                with open(file.path, 'rb') as f:
                    self.api(f, file.name)

    def upload_files(self):
        return self.file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE)

    def attach_to_page(self, page: Page):
        page.overlay.append(self.file_picker)

    def api(self, file, filename):
        remove_background_response = requests.post(
            REMOVE_BG_API,
            files={'image': file},
            data={'test': True},
            auth=(REMOVE_BG_API_KEY, REMOVE_BG_API_PASS)
        )

        if remove_background_response.status_code == requests.codes.ok:
            upload_to_bucket(file)
            color_name = detect_color(filename, remove_background_response)
            self.add_new_item_action(filename, color_name)
        else:
            logger.error('Error:', remove_background_response.status_code, remove_background_response.text)
