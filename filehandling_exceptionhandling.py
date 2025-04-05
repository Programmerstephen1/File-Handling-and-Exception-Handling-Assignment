# File Handling and Exception Handling Assignment

def modify_file_content(original_file, new_file):
    """
    Reads content from original_file, converts it to uppercase,
    and writes it to new_file.
    """
    try:
        with open(original_file, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        with open(new_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Modified content has been written to '{new_file}'.")
    
    except FileNotFoundError:
        print(f"❌ Error: The file '{original_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied for file '{original_file}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def user_file_reader():
    """
    Prompts the user for a filename and tries to read and display its contents.
    """
    try:
        filename = input("\n📄 Enter the name of the file you want to read: ")
        with open(filename, "r") as file:
            content = file.read()
            print("\n📚 File Content:\n" + content)

    except FileNotFoundError:
        print(f"⚠️ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"⚠️ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# ==== MAIN PROGRAM START ====

print("🔧 File Handling and Exception Handling Assignment")
print("--------------------------------------------------")

# PART 1: File Read & Write Challenge 🖋️
# Provide a file called 'sample.txt' in the same directory or edit the filename
modify_file_content("sample.txt", "modified_sample.txt")

# PART 2: Error Handling Lab 🧪
user_file_reader()
