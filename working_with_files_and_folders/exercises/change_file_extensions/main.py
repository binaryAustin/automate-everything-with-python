from pathlib import Path

root_dir = Path("working_with_files_and_folders/change_file_extensions/files")

filepaths = root_dir.iterdir()

for filepath in filepaths:
    new_filepath = filepath.with_suffix(".csv")
    filepath.rename(new_filepath)
