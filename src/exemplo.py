import time
from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):

    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        #print(f'§§§ EVENTO: {event.is_directory}')
        if (event.is_directory == False):
            if datetime.now() - self.last_modified < timedelta(seconds=60):
                print('MUDANÇA')
                return
            else:
                self.last_modified = datetime.now()
                print('SEM MUDANÇA')
            #print(f'path : {event.src_path}')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/home/rod/Documentos/EXEMPLO_WATCH_DOG/data_sorce/', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
