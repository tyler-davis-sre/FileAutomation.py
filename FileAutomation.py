from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Fill this in Below #

source_dir = "/home/tyler/Downloads"
dest_dir_music = "/home/tyler/Music"
dest_dir_video = "/home/tyler/Videos"
dest_dir_image = "/home/tyler/Pictures"
dest_dir_documents = "/home/tyler/Documents"

# Supported image types #
image_extensions = [".jpeg", ".jpg", ".jpe", ".jif", ".png", ".gif"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mp4", ".mp4v", ".avi", ".mov", ".qt"]

# Supported Audio types
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

# Supported Document types #

document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # if File exists, Adds number onto the end of the filename
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter +=1

    return name

def move_file(dest, entry, name):
    if exists(join(dest, name)):
        name = make_unique(dest, name)
    move(entry.path, join(dest, name))


class MoverHandler(FileSystemEventHandler):
    # Function will run whenever there is a change in the "source_dir"

    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name): #Checks all Video files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name): #Checks all Image files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


