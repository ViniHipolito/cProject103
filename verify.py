import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/[NOME DE USUARIO]/Downloads/[NOME DE PASTA]'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"eae parça, {event.src_path} foi criado")
    def on_deleted(self, event):
        print(f"então meu parceirinho, {event.src_path} foi apagado, perdido e initido")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()
try: 
    while True:
        time.sleep(2)
        print('EXECUTANDO')
except KeyboardInterrupt:
    print('interompido')
    observer.stop()