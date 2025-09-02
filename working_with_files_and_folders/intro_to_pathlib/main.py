from pathlib import Path


p1 = Path("working_with_files_and_folders/files/ghi.txt")
print(type(p1))

if not p1.exists():
    with open(p1, mode="w", encoding="utf-8") as fw:
        fw.write("Content 3")


print(p1.name)
print(p1.stem)
print(p1.suffix)


p2 = Path("working_with_files_and_folders/files")
print(list(p2.iterdir()))
