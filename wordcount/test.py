fulltext = input("Enter text here: ")
fulltext = fulltext.lower()
wordlist = re.findall('[a-zA-Z]*', fulltext)
words = dict()
Maximum = 0
Big_word = ""
for word in wordlist :
	if len(word) < 2 : 
		continue
	else  :
		words[word] = words.get(word, 0) + 1
for word in words :
	if words[word] > Maximum :
		Maximum = words[word]
		Big_word = word
Sorted_words = list()
Biggest_words = list()
for word in words :
	Sorted_words.append((word, words[word]))
Sorted_words.sort()
Biggest_words = Sorted_words[:10]