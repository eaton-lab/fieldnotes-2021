#!/usr/bin/env python

"""
Copy a lower quality photo to the repo dir
"""

import os
import subprocess
import glob

if __name__ == "__main__":

    photos = glob.glob("/home/deren/Desktop/collection-pics/*.jpg")
    photos += glob.glob("/home/deren/Desktop/collection-pics/*.png")
    for photo in photos:
        name = os.path.basename(photo)
        newpath = os.path.join("./assets/flowers", name)
        if not os.path.exists(newpath):
            print(name, newpath)
            cmd = ["convert", photo, "-resize", "X1200", newpath]
            subprocess.run(cmd, check=True)
