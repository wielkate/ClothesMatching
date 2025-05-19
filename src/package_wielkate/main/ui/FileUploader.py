import os
import shutil

from flet.core.file_picker import FilePicker, FilePickerResultEvent, FilePickerFileType
from flet.core.page import Page

from src.package_wielkate.main.commons.constants import IMAGES_DIRECTORY
from src.package_wielkate.main.scripts.process_image import process_image_with_name


class FileUploader:
    def __init__(self, add_new_item_action, upload_dir: str = IMAGES_DIRECTORY):
        self.upload_dir = upload_dir
        self.file_picker = FilePicker(on_result=self.file_picker_result)
        self.add_new_item_action = add_new_item_action

    def file_picker_result(self, e: FilePickerResultEvent):
        if e.files is not None:
            os.makedirs(self.upload_dir, exist_ok=True)
            for file in e.files:
                filename = file.name
                dest_path = os.path.join(self.upload_dir, filename)
                shutil.copy(file.path, dest_path)
                color_name = process_image_with_name(filename)
                self.add_new_item_action(filename, color_name)

    def upload_files(self):
        return self.file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE)

    def attach_to_page(self, page: Page):
        page.overlay.append(self.file_picker)

    def delete_file(self, filename):
        dest_path = os.path.join(self.upload_dir, filename)
        if os.path.exists(dest_path):
            os.remove(dest_path)
