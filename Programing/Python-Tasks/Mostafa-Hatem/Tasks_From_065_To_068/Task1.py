

import os


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop_path, "Python")
os.makedirs(python_folder, exist_ok=True)


for i in range(1, 51):
    file_name = f"txt{i}.txt"
    if i == 25:
        file_name = "special-text.txt" 
        open(os.path.join(python_folder, file_name), "w").close()  
    else:
        with open(os.path.join(python_folder, file_name), "w") as f:
            f.write(f"Elzero Web School => {i}")


assign_path = os.path.join(python_folder, "assign.py")
with open(assign_path, "w") as f:
    f.write('import os\n\n')
    f.write('#  Current Working Directory\n')
    f.write('print(os.getcwd())\n\n')

    f.write('# Print the path where the file is currently located.\n')
    f.write('print(os.path.dirname(os.path.abspath(__file__)))\n\n')

    f.write('# Print the name of the currently open file\n')
    f.write('print(os.path.basename(__file__))\n\n')

    f.write('#Print the number of files in the folderPython\n')
    f.write(f'print(len(os.listdir("{python_folder}")))\n')
