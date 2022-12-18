# MH-Watch-Dump

MH-Watch-Dump is a command-line tool that automates the process of dumping a JSON string from the MH+ browser extension to the MH-File-Watcher. The MH-File-Watcher is a tool for uploading files to Minehut servers.

## Setup

To get set up with MH-Watch-Dump, you will need to do the following:

1. Download and install [MH+](https://github.com/honkling/MHPlus).
2. Download and install [mh-file-watcher](https://github.com/RayBytes/minehut-file-watcher). Instructions for downloading and installing can be found on their respective repositories.
3. Download and install [Python](https://www.python.org/downloads/).
4. Install any necessary Python modules by running `pip install -r requirements.txt`.

## How To Use

To use MH-Watch-Dump, follow these steps:

1. Copy your JSON string from the MH+ extension.
2. Run the `auto_dump.py` script by typing `python auto_dump.py '[JSON STRING HERE]'` into your command prompt, replacing `'[JSON STRING HERE]'` with your actual JSON string.
3. The script should respond with a message indicating that your keys have been uploaded. *Make sure that your server is running and properly configured.*
