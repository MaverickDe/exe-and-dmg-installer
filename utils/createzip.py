import zipfile
import os
import io


def create_zip_from_folder(folder_path):
    """
    Create a ZIP file from the contents of the specified folder.

    Args:
        folder_path (str): The path to the folder to be zipped.

    Returns:
        io.BytesIO: A BytesIO object containing the ZIP file data.
    """
    zip_io = io.BytesIO()

    with zipfile.ZipFile(zip_io, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, relative_path)

    zip_io.seek(0)
    return zip_io
