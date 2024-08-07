import zipfile
import os

def extract_zip(zip_file_path, extract_to_directory, password=None, specific_files=None):
    """
    Extract files from a ZIP archive.

    :param zip_file_path: Path to the ZIP file.
    :param extract_to_directory: Directory where files should be extracted.
    :param password: Optional; password for password-protected ZIP files (as bytes).
    :param specific_files: Optional; list of file names to extract. Extracts all if None.
    """
    # Ensure the extraction directory exists
    os.makedirs(extract_to_directory, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            if specific_files:
                # Extract specific files
                print(specific_files)
                for file_name in specific_files:
                    if file_name in zip_ref.namelist():
                        if password:
                            zip_ref.extract(file_name, extract_to_directory, pwd=password)
                        else:
                            zip_ref.extract(file_name, extract_to_directory)
            else:
                # Extract all files
                if password:
                    for file_name in zip_ref.namelist():
                        zip_ref.extract(file_name, extract_to_directory, pwd=password)
                else:
                    zip_ref.extractall(extract_to_directory)
                
        print(f'Files extracted to {extract_to_directory}')
    except RuntimeError as e:
        print(f'Error extracting ZIP file: {e}')
    except FileNotFoundError:
        print(f'The file {zip_file_path} was not found.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

# Example usage:
# extract_zip('path/to/your/archive.zip', 'path/to/extract/directory')
# extract_zip('path/to/your/archive.zip', 'path/to/extract/directory', specific_files=['file1.txt', 'file2.txt'])
# extract_zip('path/to/your/archive.zip', 'path/to/extract/directory', password=b'your_password_here')
