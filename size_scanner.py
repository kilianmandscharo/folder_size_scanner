#!/usr/bin/python3
import os
import glob
import sys

class FolderSizeScanner :

    def __init__(self) :
        self.folders = dict()

    def get_size(self, path) :
        file_size = 0
        folder_size = 0
        with os.scandir(path=path) as it :
            for entry in it :
                new_path = os.path.join(path, entry.name)
                if entry.is_file() :
                    file_size += os.path.getsize(new_path)
                elif entry.is_dir() :
                    folder_size += self.get_size(new_path)
        _, file_name = os.path.split(path)
        self.folders[file_name] = [folder_size, file_size]
        return folder_size + file_size

    def file_scan(self, path) :
        self.get_size(path)
        for folder in [f for f in self.folders][::-1] :
            file_size = self.folders[folder][1]
            total_size = self.folders[folder][0] + file_size
            print(f"{total_size:10.0f} Bytes in {folder:15}, thereof {file_size:10.0f} directly in the directory")


if __name__ == "__main__" :

    cwd = os.getcwd()
    file_scanner = FolderSizeScanner()

    if len(sys.argv) == 1 :
        print("No argument provided")
        print("Defaulting to CWD:")
        print(cwd)
        file_scanner.file_scan(cwd)
    else :
        #folder_name = sys.argv[1]
        #new_path = os.path.join(cwd, folder_name)
        #if os.path.exists(new_path) :
            #print("Specified directory:", folder_name)
            #print("is a directory and will be used as root directory\n")
            #file_scanner.file_scan(new_path)
            #print()
        #else :
            #print("Specified directory:", folder_name)
            #print("is not a directory -- defaulting to CWD:")
            #print(cwd, "\n")
            #file_scanner.file_scan(cwd)
            #print()
        path = sys.argv[1]
        if os.path.exists(path) :
            print("Specified path:", path)
            file_scanner.file_scan(path)
        else :
            print("Path does not exist")
            print("Defaulting to CWD")
            file_scanner.file_scan(cwd)
