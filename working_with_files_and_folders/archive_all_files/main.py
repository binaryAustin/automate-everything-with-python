from pathlib import Path
import zipfile

root_dir = Path("working_with_files_and_folders/archive_all_files/files")
archive_path = Path("working_with_files_and_folders/archive_all_files/data.zip")


with zipfile.ZipFile(archive_path, mode="w") as zfw:
    for filepath in root_dir.glob("**/*.txt"):
        zfw.write(filepath, arcname="data/" + filepath.name)
        filepath.unlink()
