import os
import shutil
from flet.core.file_picker import FilePicker, FilePickerResultEvent, FilePickerFileType
from flet.core.page import Page
from process_images import process_image_with_name
from commons import IMAGES_DIRECTORY


class FileUploader:
    def __init__(self, on_file_processed, upload_dir: str = IMAGES_DIRECTORY):
        self.upload_dir = upload_dir
        self.file_picker = FilePicker(on_result=self.file_picker_result)
        self.on_file_processed = on_file_processed

    def file_picker_result(self, e: FilePickerResultEvent):
        if e.files is not None:
            os.makedirs(self.upload_dir, exist_ok=True)
            for file in e.files:
                filename = file.name
                dest_path = os.path.join(self.upload_dir, filename)
                shutil.copy(file.path, dest_path)
                color_name = process_image_with_name(filename)
                self.on_file_processed(filename, color_name)

    def upload_files(self):
        return self.file_picker.pick_files(allow_multiple=True, file_type=FilePickerFileType.IMAGE)

    def attach_to_page(self, page: Page):
        page.overlay.append(self.file_picker)
