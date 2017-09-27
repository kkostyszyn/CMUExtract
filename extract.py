from nltk.corpus import cmudict

######

def ExtractTestWords(pronun):

	toCVCVCV = ""	
	file = open("unboundcons.txt", "w")

	for each in pronun:
		#each[0] is a word
		#each[1] is a list of phones in that word 
		
		######
		# any CVCVCV sequence
		# adjust to account for target v schwa
		######
		if len(each[1]) == 6:
			if CVCVCV(each[1], 0, 0):
				#print each[0]
				toCVCVCV += "\n" + each[0]
		
		######
		#any number of Cs as long as 3 Vs, 1 target and 2 schwa
		######
		else:
			vSchwa = 0
			vTarget = 0
			others = 0
			
			for phone in each[1]:
			
				if len(phone) == 3:
				
					if phone[0:2] in schwa and phone[2] == '0':
						vSchwa += 1
					elif phone[0:2] in target_vowels and phone[2] == '1':
						vTarget += 1
					elif phone[0:2] in vowels:
						others +=1

			if vSchwa == 2 and vTarget == 1 and others == 0:
				print each[0], vSchwa, vTarget, others
				file.write("\n" + each[0])			
			
	file.close()
		
	file = open("CVCVCV.txt", "w")
	file.write(toCVCVCV)
	file.close()
		

		#compare environments to try to determine underlying vowels?

	
######
# helper funcs 
######

def CVCVCV(word, vSchwa, vTarget):
	if word[0] in consonants:
		if Vowel(word[1]):
			#print word[1][0:2]
			if word[1][0:2] in schwa:
				vSchwa += 1
			elif word[1][0:2] in target_vowels:
				vTarget += 1
				
			if (len(word) - 2) == 0:
				if vSchwa == 2 and vTarget == 1:
					return True
			else:
				return CVCVCV(word[2:len(word)], vSchwa, vTarget)
				
	return False 

def Vowel(phone):

	v = phone[0:2]
	if v in vowels:
		return True

######
# main
######
pronun = cmudict.entries()

#numbered vowels indicate stress - 1 is primary, 2 is secondary, 0 is no stress
vowels = ['AA', 'AE', 'AH', 'AO','AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'UH', 'UW']
target_vowels = ['AA', 'AE', 'IY', 'UW'] 
diphthongs = ['AW', 'AY', 'EY' 'OW', 'OY', 'ER']
schwa = ['AH', 'IH']

consonants = ['B', 'CH', 'D', 'DH', 'F', 'G', 'H', 'JH', 'K', 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH']
glides = ['W', 'Y']
ideal = ['B', 'D', 'F', 'G', 'K', 'P', 'S', 'SH', 'T', 'Z'] 


ExtractTestWords(pronun)