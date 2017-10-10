#! python3
# -*- coding: utf-8 -*-
"""Creates new folder with todays date in AEC Work folder."""

import os
import datetime
import ctypes

NOW = datetime.datetime.now()
NEW_FOLDER = NOW.strftime('%m%d%Y')

def newfolder():
    """Adds a new folder to the AEC Work folder with todays date.
        If folder with todays date exists an error box will appear."""

    try:
        os.makedirs('C:\\AEC Work\\' + NEW_FOLDER)
    except WindowsError:
        ctypes.windll.user32.MessageBoxW(0, "Folder Exists", "Error", 0)

if __name__ == "__main__":
    newfolder()
