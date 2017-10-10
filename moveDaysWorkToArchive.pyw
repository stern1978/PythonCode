#! python3
# -*- coding: utf-8 -*-
""" Moves folders from AEC Work to Aaron's archive jobs folder at end of day."""

import shutil
import os
import datetime
import time
import sys
import ctypes

os.system('TASKKILL /F /IM FlashRen.exe')
cwd = os.getcwd()

NOW = datetime.datetime.now()
NEW_FOLDER = "{:%m%d%Y}".format(NOW)

SRC = os.path.join('C:\\', 'AEC Work', NEW_FOLDER)
BACKUP = os.path.join('\\\\fileserver', 'Data Service', 'AARON')
DST = os.path.join(BACKUP, "{:%Y}".format(NOW), "{:%m. %B}".format(NOW).upper(), NEW_FOLDER)

try:
    shutil.move(SRC, DST)

except FileExistsError:
    ctypes.windll.user32.MessageBoxW(0, "Folder Exists.  Can't Archive Folder.", "Error", 0)
        
except FileNotFoundError:
    ctypes.windll.user32.MessageBoxW(0, "No Folder found in AEC Work.  Can't Archive.", "Error", 0)

except:
    filehandler = open('archive_error.log', 'a')
    filehandler.write(str(time.ctime()) + 'error' + '\n')
    filehandler.close()
    #ctypes.windll.user32.MessageBoxW(0, "Drive is down!", "Error", 0)
