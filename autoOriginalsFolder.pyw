#! python3
# -*- coding: utf-8 -*-
"""Creates new folder with todays date in AEC Work folder."""

import os
import ctypes
import datetime
import time

NOW = datetime.datetime.now()
NEW_FOLDER = NOW.strftime('%m%d%Y')

UPDATE = os.path.join('C:\\', 'AEC Work', NEW_FOLDER, 'New folder')
OPATH = os.path.join('C:\\', 'AEC Work', NEW_FOLDER, 'New folder', 'ORIGINALS')

def originals():
    """Originals folder is created when 'New folder' is detected in my
        work folder.
    """
    while True:
        while os.path.exists(UPDATE):
            try:
                os.makedirs(OPATH)
                time.sleep(120)
            except WindowsError:
                ctypes.windll.user32.MessageBoxW(0, WindowsError, "Error!", 0)
                continue

if __name__ == "__main__":
    originals()
