from pathlib import Path

root_dir = "working_with_files_and_folders/create_empty_files/files"

for i in range(10, 21):
    filename = f"{i}.txt"
    filepath = Path(f"{root_dir}/{filename}")
    filepath.touch()
