import binascii
import sys
import os
from tkinter import Tk   
from tkinter.filedialog import askopenfilename
try:
    droppedFile = sys.argv[1] 
except IndexError:
    Tk().withdraw()
    droppedFile = askopenfilename()
    

filename, file_extension = os.path.splitext(droppedFile)
with open(filename+file_extension, 'rb') as f:
    content = f.read()

fileashex = binascii.hexlify(content)

if (file_extension == ".png") or (file_extension == ".apng") : 
    x = fileashex.rfind(b"00")
    data = fileashex[:x] + b"0149454E4400D11A4FE1" +fileashex[x:+len("0149454E4400D11A4FE1")]
else:
    x = len(fileashex)
    data = fileashex[:x-2] + b"21"

bytes_data = binascii.unhexlify(data)

fp = open(filename + "_transparencyFix" + file_extension, "wb+")
fp.write(bytes_data)
fp.close()
