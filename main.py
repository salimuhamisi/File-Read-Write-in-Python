
# Ask the user for the input filename
filename = input("Enter the filename to read: ")

try:
    # Try opening and reading the file
    with open(filename, "r") as f:
        content = f.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write modified content into a new file
    with open("modified_" + filename, "w") as new_file:
        new_file.write(modified_content)

    print("Modified file created successfully: modified_" + filename)

except FileNotFoundError:
    print("Error: The file '" + filename + "' was not found.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
