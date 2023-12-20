import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "./Test"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"someone,{event.src_path}has created it")
    def on_modified(self, event):
        print(f"someone,{event.src_path}has modified it")
    def on_moved(self, event):
        print(f"someone,{event.src_path}has moved it")
    def on_deleted(self, event):
        print(f"someone,{event.src_path}has deleted it")
eventHandler=FileEventHandler()
observer=Observer()
observer.schedule(eventHandler, from_dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()

    
    
    