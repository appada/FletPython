import os
import shutil
import flet as ft

def main(page:ft.Page):
    page.title='File Organizer'
    
    file_types = {
        'DOC': ['.pdf', '.docx', '.ppt', '.txt', '.hwp'],
        'PHOTO': ['.jpg', '.jpeg', '.png'],
        'MOV': ['.mp3', '.wav'],
        'ZIP': ['.zip'],
        'PROGRAM': ['.dart', '.py', '.js', '.exe']
    }

    #functions
    def pick_folder_result(e: ft.FilePickerResultEvent):
        if e.path:
            folder_path.value = f"Selected Folder : { e.path }"
        else:
            folder_path.value = "select a folder"
        page.update()

    def organize_files():
        selected_folder = folder_path.value.split(": ")[-1]
        file_list.controls.clear()
        if not os.path.isdir(selected_folder):
            status_text.value = "select a folder"
            page.update()
            return

        for category, extension in file_types.items():
            category_folder = os.path.join(selected_folder, category)
            os.makedirs(category_folder, exist_ok=True)

        #ai generated
        for filename in os.listdir(selected_folder):
            file_path = os.path.join(selected_folder, filename)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                for category, extensions in file_types.items():
                    if ext.lower() in extensions:
                        dest_folder = os.path.join(selected_folder, category)
                        shutil.move(file_path, os.path.join(dest_folder, filename))
                        result_text = f'{filename} = > {dest_folder}'
                        file_list.controls.append(ft.Text(result_text))
                        break
        page.update()

    #widgets
    folder_path = ft.Text('folder path ...')
    status_text = ft.Text(value='')
    file_list = ft.ListView(expand=1, spacing=10, padding=5)

    file_pick_dialog = ft.FilePicker(on_result=pick_folder_result)
    page.overlay.append(file_pick_dialog)

    pick_folder_button = ft.ElevatedButton(
        'Select Folder', icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: file_pick_dialog.get_directory_path()
    )


    organize_button = ft.ElevatedButton(
        'File Organize',
        icon= ft.Icons.CLEANING_SERVICES,
        on_click=lambda _: organize_files()
    )
    
    page.add(
        ft.Column([
            pick_folder_button,
            folder_path,
            organize_button,
            status_text,
            file_list
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    )

    
    
    
ft.app(main)
