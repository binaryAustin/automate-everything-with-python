from pathlib import Path


root_dir = Path("working_with_files_and_folders/rename_all_files/files")
filepaths = root_dir.iterdir()

print(Path.cwd())

for filepath in filepaths:
    new_filename = "new_" + filepath.name
    new_filepath = filepath.with_name(new_filename)
    filepath.rename(new_filepath)
