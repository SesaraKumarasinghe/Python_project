# read_file.py
# A simple script to read and display text from a file

def read_text_file(filename):
    """Read and print the contents of a text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print("File contents:\n")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the file name
    file_path = input("Enter the path to the text file: ")
    read_text_file(file_path)
