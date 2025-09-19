from pathlib import Path

def readflefolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):  
        print(f"{i+1}. {item}")


def createfile():
    try:
        readflefolder()
        name = input("Enter the name of the file:- ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as f:
                f.write(input("Enter the content:- "))
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as e:
        print('An error occurred:', e)


def readfile():
    try:
        readflefolder()
        name = input("Enter the name of the file:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as f:
                print(f.read())
        else:
            print("File does not exist")
    except Exception as e:
        print('An error occurred:', e)


def updatefile():
    try:
        readflefolder()
        name = input("Enter the name of the file to update:- ")
        p = Path(name)

        if not p.exists() or not p.is_file():
            print("File does not exist")
            return

        print("\nUpdate Options:")
        print("1. Update the file name")
        print("2. Overwrite existing content")
        print("3. Append new content")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_name = input("Enter the new file name:- ")
            new_path = Path(new_name)
            p.rename(new_path)
            print("File renamed successfully")

        elif choice == 2:
            new_content = input("Enter new content:- ")
            with open(p, 'w') as f:
                f.write(new_content)
            print("File content updated successfully")

        elif choice == 3:
            append_content = input("Enter content to append:- ")
            with open(p, 'a') as f:
                f.write("\n" + append_content)
            print("Content appended successfully")

        else:
            print("Invalid choice, please select 1-3")

    except Exception as e:
        print("An error occurred:", e)


def deletefile():
    try:
        readflefolder()
        name = input("Enter the name of the file to delete:- ")
        p = Path(name)

        if not p.exists():
            print("File does not exist")
            return

        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ")
        if confirm.lower() == 'y':
            p.unlink()   # deletes the file
            print("File deleted successfully")
        else:
            print("Deletion cancelled")

    except Exception as e:
        print("An error occurred:", e)

        
print("1. Create a file")
print("2. Read a file")
print("3. Update a file")
print("4. Delete a file")
print("5. Exit")

try:
    option = int(input("Enter your option: "))
    if 1 <= option <= 5:   # ✅ Correct condition
        match option:
            case 1:
                createfile()
            case 2:
                readfile()
            case 3:
                updatefile()
            case 4:
                deletefile()
            case 5:
                print("Exiting...")
    else:
        print("Invalid option, please choose between 1 and 5")
except ValueError:
    print("Please enter a valid number!")
