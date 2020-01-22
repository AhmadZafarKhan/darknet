import os
from os import walk


path = "/Users/AhmadZafarKhan/Desktop/argedor/darknet/img"

f = []
cmd = "ls -l"
for (dirpath, dirnames, filenames) in walk(path):
    so = os.popen(cmd).read()
    print(so)