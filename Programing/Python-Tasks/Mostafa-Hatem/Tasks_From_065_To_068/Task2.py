import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop_path, "Python")
file_path = os.path.join(python_folder, "txt1.txt")

with open(file_path, "r") as file:
    first_line = file.readline().strip()

with open(file_path, "w") as file:
    file.write(first_line + "\n")
    for _ in range(50):
        file.write("Appended => Elzero Web School\n")
