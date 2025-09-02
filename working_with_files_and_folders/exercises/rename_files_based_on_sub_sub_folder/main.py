from pathlib import Path


root_dir = Path(
    "working_with_files_and_folders/exercises/rename_files_based_on_sub_sub_folder/files"
)
filepaths = root_dir.glob("**/*")

for filepath in filepaths:
    if filepath.is_file():
        parts = filepath.parts
        # print(parts[-3], parts[-2])
        new_filename = f"{parts[-3]}_{parts[-2]}_{filepath.name}"
        # print(new_filename)
        new_filepath = filepath.with_name(new_filename)
        filepath.rename(new_filepath)
