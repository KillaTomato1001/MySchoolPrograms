def message(text, plain, encryp):
	dictionary = dict(zip(plain, encryp))
	newmessage = ''
	for char in text:
		try:
			newmessage += dictionary[char]
		except:
			newmessage += ' '
	print (text + '\nhas been encrypted to:')
	print (newmessage)
