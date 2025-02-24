MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}


def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '

	return cipher

def decrypt(message):

	message += ' '

	decipher = ''
	citext = ''
	for letter in message:


		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :
				decipher += ' '
			else:

			
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

def mc_to_en():
    message = input("Put Morse code here: ")
    message = decrypt(message)
    print(message)
    
def en_to_mc():
    message = input("Put english here: ")
    message = encrypt(message.upper())
    print(message)
    
    
def main():
    print("Choose an option (1-3): ")
    print('\n1: MorseC to English \n2: English to MorseC\n3: Exit\n')
    option = input(">> ")
    if (option == "1"):
        mc_to_en()
    elif (option == "2"):
        en_to_mc()
    elif (option == "3"):
        print("bai")
        exit()

if __name__ == '__main__':
	main()
