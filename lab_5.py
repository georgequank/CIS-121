### LAB 5
#I do not know what I am doing

def main():
	DecodeWord()


#Your code goes here.
	#encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"

encodedWord = "WBLARF8TTS"

def DecodeWord():
	for letter in encodedWord[0:1]:
		if letter == "L":
			letter = "T"
		elif letter == "T":
			letter = "L"
		elif letter == "8":
			letter = "A"
		else:
			letter = letter
	print(DecodeWord(encodedWord))
	return encodeWord

encodeWord = DecodeWord()

#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()