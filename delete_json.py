import os
import re


def delete_json_files(directory):
    pattern = re.compile(r'.*\.json$')
    
    for root, subdir, files in os.walk(directory): #depends on how your directory is structured
        
        for dir in subdir:
            dir_path = os.path.join(root, dir)
            print(f"dir name {dir_path}")
            if pattern.match(dir) is not None:
                os.remove(dir_path)
                
        for file in files:
            file_path = os.path.join(root, file)
            if pattern.match(file) is not None:
                os.remove(file_path)
                    
    
if __name__ == "__main__":
    directory_path = "PATH_NAME" #replace this with your path name
    delete_json_files(directory_path)