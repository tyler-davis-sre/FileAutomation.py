# Automated File Organizer
This Python script is a simple, automated solution for organizing files. It uses the `watchdog` library to monitor a source directory and automatically moves new files into designated folders based on the file extension. This is useful for keeping your "Downloads" folder clean by automatically sorting your music, videos, images, and documents. 

## Features
* Real-time Monitoring: The script runs continuously in the background, watching for new files.
* File Type Sorting: It automatically moves files to their corresponding `Music`, `Videos`, `Pictures` and `Documents` folders.
* Duplicate File Handling: If a file with the same name already exists in the destination folder, the script will rename the new file by adding a counter (e.g., `filename(1).mp4`).

## Requirements
Before you can run this script, you need to install the `watchdog` library. You can do this using `pip`:

```
pip install watchdog
```
## How to Use
1. Customize Paths: Open the Python script (`FileAutomation.py`) and modify the following variables at the top to match your system's directory:

```
source_dir = "/path/to/your/source/folder"
dest_dir_music = "/path/to/your/Music"
dest_dir_video = "/path/to/your/Videos"
dest_dir_image = "/path/to/your/Pictures"
dest_dir_documents = "/path/to/your/Documents"
```


Run the Script: Execute the script from your terminal:

`python FileAutomation.py`


Stop the Script: The script will run continuously until you stop it. To exit, go back to your terminal and press `Ctrl + C`.
