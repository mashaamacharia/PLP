def read_and_modify_file():
    # Prompt the user to enter the filename
    filename = input("Please enter the filename to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Define the new filename
        new_filename = f"modified_{filename}"

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while processing the file '{filename}'.")

if __name__ == "__main__":
    read_and_modify_file()
