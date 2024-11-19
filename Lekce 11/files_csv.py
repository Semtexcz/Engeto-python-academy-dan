from pathlib import Path
import csv
from datetime import datetime
from typing import Dict, Generator

def find_files(directory: str, file_extension: str) -> Generator:
    """
    Recursively find all files with the specified extension in the given directory.

    :param directory: Path to the directory to search.
    :param file_extension: File extension to filter (e.g., ".txt").
    :return: Generator yielding Path objects for matching files.
    :raises FileNotFoundError: If the directory does not exist.
    """
    dir_path = Path(__file__).parent / Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    return dir_path.rglob(f"*{file_extension}")

def collect_file_data(file_path: Path) -> Dict[str, str]:
    """
    Collect metadata about a file.

    :param file_path: Path object of the file.
    :return: Dictionary containing file metadata (name, size, absolute path, last modified date).
    """
    return {
        "name": file_path.name,
        "size": file_path.stat().st_size,
        "path": str(file_path.resolve()),
        "last_modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
    }

def write_to_csv(file_data_list: list, output_file: str) -> None:
    """
    Write collected file data to a CSV file.

    :param file_data_list: List of dictionaries containing file metadata.
    :param output_file: Name of the output CSV file.
    """
    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["name", "size", "path", "last_modified"])
        writer.writeheader()
        writer.writerows(file_data_list)

def main():
    """
    Main function to execute the script.

    - Prompts the user for a directory and file extension.
    - Collects file data.
    - Writes the data to a CSV file.
    """
    directory = input("Enter the directory path: ").strip()
    file_extension = input("Enter the file extension (e.g., .txt): ").strip() or ".txt"
    output_file = "soubory.csv"

    try:
        print("Searching for files...")
        files = find_files(directory, file_extension)

        print("Collecting file data...")
        file_data_list = [collect_file_data(file) for file in files]

        print(f"Writing data to '{output_file}'...")
        write_to_csv(file_data_list, output_file)

        print(f"Data has been successfully written to '{output_file}'.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
