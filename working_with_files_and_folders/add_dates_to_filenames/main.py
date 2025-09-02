from pathlib import Path


root_dir = Path("working_with_files_and_folders/add_dates_to_filenames/files")

filepaths = root_dir.glob("**/*")

for filepath in filepaths:
    if filepath.is_file():
        stat = filepath.stat()
        new_filename = str(int(stat.st_ctime)) + "_" + filepath.name
        new_filepath = filepath.with_name(new_filename)
        filepath.rename(new_filepath)
