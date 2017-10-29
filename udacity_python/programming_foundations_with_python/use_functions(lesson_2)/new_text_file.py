import os

def new_text_file(file_name):
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Mayk Jony\Desktop\test_folder")
    open(file_name, 'a')
    os.chdir(saved_path)
    print("The text file '{0}' is created".format(file_name))
    
