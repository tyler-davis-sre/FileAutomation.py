# Automated File Organizer
This Python script is a simple, automated solution for organizing files. It uses the `watchdog` library to monitor a source directory and automatically moves new files into designated folders based on the file extension. This is useful for keeping your "Downloads" folder clean by automatically sorting your music, videos, images, and documents. 

## Features
* Real-time Monitoring: The script runs continuously in the background, watching for new files.
* File Type Sorting: It automatically moves files to their corresponding `Music`, `Videos`, `Pictures` and `Documents` folders.
* Duplicate File Handling: If a file with the same name already exists in the destination folder, the script will rename the new file by adding a counter (e.g., `filename(1).mp4`).

## Requirements
Before you can run this script, you need to install the required Python packages. You can do this using the provided `requirements.txt` file: `pip install -r requirements.txt`

## How to Use
Customize Paths: A `config.ini` file is included to make it easy to customize the script's behavior. Before running, create your own copy of the configuration file and update the paths.

Open `config.ini` and modify the path values to match your system's directory structure. Please use absolute paths to ensure the script runs correctly.


Run the Script: Execute the script from your terminal:

`python FileAutomation.py`


Stop the Script: The script will run continuously until you stop it. To exit, go back to your terminal and press `Ctrl + C`.
