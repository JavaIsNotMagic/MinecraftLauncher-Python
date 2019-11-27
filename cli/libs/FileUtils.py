from sys import platform
from os import getcwd,walk
from zipfile import ZipFile
#Functions
def read_file(f):
  with open(f) as fp:
    return fp.read()
  #End
#end
