from flet.core.file_picker import FilePicker, FilePickerResultEvent, FilePickerFileType
from flet.core.page import Page

from endpoints.endpoints import upload_to_bucket, detect_color, remove_bg


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
        remove_background_response = remove_bg(file)
        upload_to_bucket(file)
        color_name = detect_color(filename, remove_background_response)
        self.add_new_item_action(filename, color_name)
