import os
from string import digits

def rename_files():
    
    file_list = os.listdir(r"C:\Users\Mayk Jony\Desktop\prank\prank")
    print(file_list)

    saved_path = os.getcwd() # get current working directory
    os.chdir(r"C:\Users\Mayk Jony\Desktop\prank\prank")
    for file_name in file_list:
        os.rename(file_name, ''.join(i for i in file_name if not i.isdigit()))
    print(file_list)
    os.chdir(saved_path)
    print("The renaming procces is succesfully done.")


