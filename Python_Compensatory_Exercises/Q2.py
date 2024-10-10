import os

def count_files(directory, extension):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count

ext = input("Enter the file extension (like '.py'): ")
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
total_files = count_files(desktop, ext)
print(total_files)