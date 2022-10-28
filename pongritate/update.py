import urllib.request
import os


print("Updating...")
codeURL = urllib.request.urlopen('https://raw.githubusercontent.com/Jankie06/pongritate/main/pongritate/src/main.py')
#print(codeURL.read().decode())

code = open(os.getcwd()+"\\src\\main.py", "w")
code.write(codeURL.read().decode())
code.close()

code = open(os.getcwd()+"\\src\\main.py", "r")
print(code.read())