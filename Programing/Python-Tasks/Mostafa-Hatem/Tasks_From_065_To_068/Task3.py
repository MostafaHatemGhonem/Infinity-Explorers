import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop_path, "Python")
file_path = os.path.join(python_folder, "txt1.txt")

with open(file_path, "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
chars = content
l_count = chars.count("l")

print(f"Number Of Lines Is => {len(lines)}")
print(f"Number Of Words Is => {len(words)}")
print(f"Number Of Chars Is => {len(chars)}")
print(f'Number Of "l" Char Is => {l_count}')
