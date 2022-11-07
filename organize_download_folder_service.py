from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
import os
import pathlib
import time
import shutil


class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in [file for file in folder_to_track.iterdir()]:
            ext = self.get_extension(filename)
            if ext is not None:
                new_destination = self.get_destination(filename,ext)
                print("Original file: {}".format(filename))
                print("Will be moved to: {}".format(new_destination))
                shutil.move(filename,new_destination)
            else:
                print(ext)
                print("No files were moved")
        print("Finished observing")
        print("*"*100)
        
            

    def get_destination(self, filename, ext):
        pdfs_folder = pathlib.Path(r"D:\Downloads2\pdfs")
        pdfs_folder.mkdir(parents=True, exist_ok=True)
            
        images_folder = pathlib.Path(r"D:\Downloads2\images")
        images_folder.mkdir(parents=True, exist_ok=True)
            
        text_md_folder = pathlib.Path(r"D:\Downloads2\text_md_folder")
        images_folder.mkdir(parents=True, exist_ok=True)
        
        videos_folder = pathlib.Path(r"D:\Downloads2\videos")
        videos_folder.mkdir(parents=True, exist_ok=True)
        
        zips_folder = pathlib.Path(r"D:\Downloads2\zip_files")
        zips_folder.mkdir(parents=True, exist_ok=True)
        
        csv_folder = pathlib.Path(r"D:\Downloads2\csv_files")
        csv_folder.mkdir(parents=True, exist_ok=True)
        
        exe_folder = pathlib.Path(r"D:\Downloads2\exe_files")
        exe_folder.mkdir(parents=True, exist_ok=True)
            
        if ext==".pdf":
            new_destination = pdfs_folder / filename.name
        elif ext.lower()==".png" or ext.lower()==".jpg" or ext.lower()==".svg" \
                              or ext.lower()==".jpeg" or ext.lower()==".jfif":
            new_destination = images_folder / filename.name
        elif ext.lower()==".txt" or ext.lower()==".md":
            new_destination = text_md_folder / filename.name
        elif ext.lower()==".mp4" or ext.lower()==".avi" or ext.lower()==".mov":
            new_destination = videos_folder / filename.name
        elif ext.lower()==".zip":
            new_destination = zips_folder / filename.name
        elif ext.lower()==".csv":
            new_destination = csv_folder / filename.name
        elif ext.lower()==".exe":
            new_destination = exe_folder / filename.name
        else:
            new_destination = folder_to_track / filename.name

        return new_destination

    def get_extension(self, filename):
        extensions = [".pdf", ".png", ".jpg", ".svg", ".txt", ".md", ".mp4",
                      ".avi",".mov", ".jfif", ".zip", ".csv", ".exe"]
        ext = pathlib.Path(filename).suffix
        if ext.lower() in extensions:
            return ext
        
if __name__=="__main__":
    folder_to_track = pathlib.Path(r"D:\Downloads2")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler,str(folder_to_track.absolute()), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except:
        observer.stop()
    observer.join()