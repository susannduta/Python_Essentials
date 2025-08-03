import os
import logging
from datetime import datetime

logging.basicConfig(
    filename="file_handling_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def transform_line(line: str) -> str:
    
    return line.title()

def read_modify_write(source_file: str, destination_file: str = None):
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"The file '{source_file}' does not exist.")

    if not os.path.isfile(source_file):
        raise ValueError(f"The path '{source_file}' is not a valid file.")

    with open(source_file, 'r') as infile:
        lines = infile.readlines()
        if not lines:
            raise ValueError("The file is empty. Nothing to modify.")

    modified_lines = [transform_line(line) for line in lines]

#autogenerate file name
    if not destination_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        destination_file = f"modified_{timestamp}.txt"

    with open(destination_file, 'w') as outfile:
        outfile.writelines(modified_lines)

    print(f"\n Modified content saved to: {destination_file}")


def main():
    print(" Advanced File Reader & Writer with Error Handling ")

    source = input("Enter the filename to read from: ").strip()


    use_custom_output = input("Do you want to specify the output filename? (y/n): ").strip().lower()
    if use_custom_output == 'y':
        destination = input("Enter the filename to write to: ").strip()
    else:
        destination = None

    try:
        read_modify_write(source, destination)
    except (FileNotFoundError, PermissionError, ValueError) as e:
        print(f" Error: {e}")
        logging.error(e)
    except Exception as e:
        print(" An unexpected error occurred.")
        logging.error(f"Unexpected: {e}")


if __name__ == "__main__":
    main()
