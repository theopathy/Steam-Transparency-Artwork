import binascii
import os


def DumpFile(filepath):
    filename, f_ext = os.path.splitext(filepath)
    with open(filename+f_ext, 'rb') as f:
        content = f.read()

    fileashex = binascii.hexlify(content)
    if not((f_ext == ".png") or (f_ext == ".apng")  or (f_ext == ".gif") or (f_ext == ".jpg") or (f_ext == ".jpeg")): 
        return
    if (f_ext == ".png") or (f_ext == ".apng") : 
        x = fileashex.rfind(b"00")
        data = fileashex[:x] + b"0149454E4400D11A4FE1" +fileashex[x:+len("0149454E4400D11A4FE1")]
    else:
        x = len(fileashex)
        data = fileashex[:x-2] + b"21"

    bytes_data = binascii.unhexlify(data)

    fp = open(filename +  f_ext, "wb+")
    fp.write(bytes_data)
    fp.close()


