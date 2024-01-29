import sys
from pathlib import Path

jpeg_files = list()
png_files = list()
jpg_files = list()
txt_files = list()
docx_files = list()

folders = list()
archives = list()
others = list()

unknown = set()
extensions = set()

registered_extensions = {
    'JPEG': jpeg_files,
    'PNG': png_files,
    'JPG': jpg_files,
    'TXT': txt_files,
    'DOCX': docx_files,
    'ZIP': archives
}

def get_extension(file_name: str) -> str:
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for i in folder.iterdir():
        if i.is_dir():
            if i.name not in ('JPEG', 'PNG', 'JPG', 'TXT', 'DOCX', 'ARCHIVE', 'OTHER'):
                folders.append(i)
                scan(i)
            continue
        ex = get_extension(file_name=i.name)
        name_path = folder/i.name
        if not ex:
            others.append(name_path)
        else:
            try:
                container = registered_extensions[ex]
                extensions.add(ex)
                container.append(name_path)
            except KeyError:
                unknown.add(ex)
                others.append(name_path)


if __name__ == "__main__":
    path = sys.argv[1]
    print(f"{path}")

    folder = Path(path)
    scan(folder)

    print(f"jpeg: {jpeg_files}")
    print(f"jpg: {jpg_files}")
    print(f"png: {png_files}")
    print(f"txt: {txt_files}")
    print(f"docx: {docx_files}")
    print(f"archive: {archives}")
    print(f"unkown: {others}")
    print(f"All extensions: {extensions}")
    print(f"Unknown extensions: {unknown}")
    print(f"Folder: {folders}")
