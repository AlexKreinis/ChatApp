"""
			-**********************-
			*					   *
			*	  DES MACHINE      *
			*					   *
			-**********************-
			
des encrypt and decrypt machine

			AUTHORS:		|  ID:
			--------		| -----
			Alex Kreinis	| 312623218
			Tomer Leon		| 312203003
			TOM DAMRI		| 205770068
			MATAN DAVIDIAN  | 205509219

			DATE : 	1.12.19
"""
from encryption.DES.des_algorithm.des import des, DECRYPT

def gen_key(key):
	# fix key for encryption from the user.
	if len(key)==8:
		return key
	if len(key)>8:
		return key[:8]
	cnt = 0
	l=len(key)
	key = str(key)
	new_key=""
	while len(new_key) < 8:
		new_key += key[cnt%l]
		cnt += 1
	return key

def encrypt(key,msg):
	rest = 0
	print(key)
	key=gen_key(key)
	print(key)
	text_to_encrypt = msg
	encrypted_text = text_to_encrypt
	#print("encrypt the text: \"" + encrypted_text + "\" with the key \"" + key + "\"")
	result = ""
	# encrypt 8 bytes any iteration
	while len(text_to_encrypt) >= 8:
		result += des(text_to_encrypt[:8], key)
		text_to_encrypt = text_to_encrypt[8:]
	# encrypt the rest of the bytes
	if text_to_encrypt != 0:
		rest = 8-len(text_to_encrypt)
		text_to_encrypt += rest * '0'
		result += des(text_to_encrypt, key)
	return result

def decrypt(key,msg):
	print(key)
	key = gen_key(key)
	print(key)
	result = ""
	decrypted_text = result
	print('encrypt : ', msg, "\t\tto=>: ", result)
	text_to_encrypt = result
	result = ""
	# decrypt 8 bytes any iteration
	while len(text_to_encrypt) >= 8:
		result += des(text_to_encrypt[:8], key, DECRYPT)
		text_to_encrypt = text_to_encrypt[8:]
	return result