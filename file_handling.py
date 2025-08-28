def modify_content(content):
    """
    Example modification: convert text to uppercase.
    You can change this logic to anything else.
    """
    return content.upper()


def main():
    # Ask the user for the input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new output file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
