from pathlib import Path


root_dir = Path("working_with_files_and_folders/destroy_files_forever")

for filepath in root_dir.glob("*.csv"):
    with open(filepath, mode="wb") as fw:
        fw.write(b"")
    filepath.unlink()
