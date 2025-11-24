def read_file(filename):
    """
    Reads file safely using with-open and proper error handling.
    Returns file content as string or None if an error occurs.
    """
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when opening '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    return None


# -------- USER INPUT SECTION --------
filename = input("Enter filename to read: ")

content = read_file(filename)

# -------- DISPLAY RESULT --------
if content is not None:
    print("\n📌 File Content:\n")
    print(content)
else:
    print("\n⚠ Could not read the file.")
