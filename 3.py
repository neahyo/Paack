#__________Write a function that lists the files in a path with a specific file extension.

import os

def list_files(path, ext):
    '''
    :path (str): path
    :ext (str): file extension
    '''
    
    
    files = os.listdir(path)
    files_ext = [i for i in files if i.endswith(ext)]
    print("The files with", ext, "extension located in this path are:")
    
    for item in files_ext:
        print("\t-", item)
        
 
