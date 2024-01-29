import sys
import scan
import shutil
import normalize
from pathlib import Path

def up_file(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))

def up_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)

    normalize_name = normalize.normalize(path.name.replace(".zip", ''))
    archive_folder = target_folder / normalize_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError or FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()

def remove_empty_folders(path):
    for i in path.iterdir():
        if i.is_dir():
            remove_empty_folders(i)
            try:
                i.rmdir()
            except OSError:
                pass

def main(folder_path):
    print(folder_path)
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        up_file(file, folder_path, "JPEG")

    for file in scan.jpg_files:
        up_file(file, folder_path, "JPG")

    for file in scan.png_files:
        up_file(file, folder_path, "PNG")

    for file in scan.txt_files:
        up_file(file, folder_path, "TXT")

    for file in scan.docx_files:
        up_file(file, folder_path, "DOCX")

    for file in scan.others:
        up_file(file, folder_path, "OTHER")

    for file in scan.archives:
        up_archive(file, folder_path, "ARCHIVE")

    remove_empty_folders(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"started here{path}")

    folder = Path(path)
    main(folder.resolve())