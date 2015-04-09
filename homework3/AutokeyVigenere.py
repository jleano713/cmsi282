def AutoKeyVigenere (plain_text, old_key):
	if (len(plain_text) < len(old_key)):
		raise ValueError("Key length must be <= to message length")
	key = list(old_key.lower())
	plain_text = list(plain_text.lower())
	ciphertext = []
	for i in range(len(plain_text) - len(old_key)):
		key.append(plain_text[i])
	for j in range(len(key)):
		code = ((ord(plain_text[j]) + ord(key[j]) - 64) % 26) + 65
		ciphertext.append((chr(code)))
	return ciphertext

#ciphertext = "JUKVKVOZCOHMDSFUMZCTNHZVQPFOJWCOOTWYVVBHUBYHYSWFU"
def main():
	a = raw_input("Enter message to be encrypted: ")
	b = raw_input("Enter key: ")
	cipher = AutoKeyVigenere(a, b)
	string = ""
	for k in range(len(cipher)):
		string += cipher[k]
	print("Encryption: " + string)

main()