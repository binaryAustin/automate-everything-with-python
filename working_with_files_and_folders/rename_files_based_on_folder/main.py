from pathlib import Path


root_dir = Path("working_with_files_and_folders/rename_files_based_on_folder/files")
# filepaths = root_dir.iterdir()
filepaths = root_dir.glob("**/*")

for filepath in filepaths:
    if filepath.is_file():
        parent_dirname = filepath.parent.name
        new_filename = parent_dirname + "_" + filepath.name
        new_filepath = filepath.with_name(new_filename)
        filepath.rename(new_filepath)
