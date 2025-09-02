from pathlib import Path


root_dir = Path("working_with_files_and_folders/exercises/find_a_file")

search_term = "14"


for filepath in root_dir.rglob("*"):
    if search_term in filepath.stem and filepath.is_file():
        print(filepath.absolute)
