import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop_path, "Python")

for i in range(41, 51):
    file_name = f"txt{i}.txt"
    file_path = os.path.join(python_folder, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
