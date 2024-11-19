from pathlib import Path
import os
from datetime import datetime

def create_sample_files(base_dir: str, file_count: int, depth: int, file_extension: str):
    """
    Create a directory structure with sample files for testing.

    :param base_dir: Path to the base directory where files will be created.
    :param file_count: Number of files to create per directory.
    :param depth: Depth of nested directories to create.
    :param file_extension: File extension for the created files.
    """
    base_path = Path(base_dir)
    base_path.mkdir(parents=True, exist_ok=True)

    current_dir = base_path

    for d in range(depth):
        current_dir = current_dir / f"nested_level_{d+1}"
        current_dir.mkdir(parents=True, exist_ok=True)

        for f in range(file_count):
            file_path = current_dir / f"file_{d+1}_{f+1}{file_extension}"
            with file_path.open(mode="w", encoding="utf-8") as file:
                file.write(f"Sample content for file {file_path.name} created at {datetime.now()}\n")

    print(f"Sample files created in directory: {base_path.resolve()}")

if __name__ == "__main__":
    base_dir = input("Enter the base directory for sample files: ").strip() or "sample_files"
    file_count = int(input("Enter the number of files per directory: ").strip() or 5)
    depth = int(input("Enter the depth of nested directories: ").strip() or 3)
    file_extension = input("Enter the file extension (e.g., .txt): ").strip() or ".txt"

    create_sample_files(base_dir, file_count, depth, file_extension)
