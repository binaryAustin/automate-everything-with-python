from pathlib import Path
import zipfile


root_dir = Path("working_with_files_and_folders/extract_archive")

destination = Path("working_with_files_and_folders/extract_archive/destination")

for filepath in root_dir.glob("*.zip"):
    with zipfile.ZipFile(filepath, "r") as zfr:
        final_path = destination / Path(filepath.stem)
        zfr.extractall(path=final_path)
