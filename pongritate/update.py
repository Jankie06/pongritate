import urllib.request
import os

version = urllib.request.urlopen('https://raw.githubusercontent.com/Jankie06/pongritate/main/pongritate/src/main.py')
code = urllib.request.urlopen('https://raw.githubusercontent.com/Jankie06/pongritate/main/pongritate/src/main.py')

f = open(os.getcwd()+"\\src\\main.py", "w")
f.write(code.read().decode())
f.close()