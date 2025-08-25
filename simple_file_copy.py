try:
    # 1. Ask the user for the filename
    filename = input("Enter the filename: ")

    # 2. Try to open and read the file
    with open(filename, "r") as f:
        text = f.read()

    # 3. Modify the text (make it uppercase)
    modified = text.upper()

    # 4. Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as f:
        f.write(modified)

    print(f"Done! The modified file is saved as {new_filename}")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
