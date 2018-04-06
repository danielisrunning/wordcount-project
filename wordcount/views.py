from django.http import HttpResponse
from django.shortcuts import render
import re
import operator

def home(request) :
	return HttpResponse("Bonjour, je suis la page d'accueil de ce site.")

def homepage(request) :
	return render(request, 'home.html', {'salut':"c'est moi !"})

def asperbot(request) :
	return HttpResponse('Bonjour, je suis Asperbot et je suis en cours de création.')

def count(request) :
	fulltext = request.GET['fulltext']
	fulltext = fulltext.lower()
	wordlist = re.findall('[a-z]*', fulltext)
	# debug print(wordlist)
	words = dict()
	Maximum = 0
#	Big_word = ""
	for word in wordlist :
		if len(word) < 2 : 
			# debug print("rejected "+ word)
			continue
		else  :
			words[word] = words.get(word, 0) + 1
			# debug print("accepted "+ word)
# Used at first to determin the most used word. Not necessary anymore
#	for word in words :
#		if words[word] > Maximum :
#			Maximum = words[word]
#			Big_word = word
#	Sorted_words = list()
#	Biggest_words = list()
#	for word in words :
#		Sorted_words.append((words[word], word))
#	Sorted_words.sort(reverse=True)
	# AUTRE MANIÈRE DE FAIRE :
	Sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse = True)
	Biggest_words = Sorted_words[:40]
	Big_word = Biggest_words[0]
	# debug print(Big_word)
	Maximum = Big_word[1]
	Big_word = str(Big_word[0])
	# debug print(fulltext)
	return render(request, 'count.html', {'fulltext':fulltext, 'count' : len(wordlist), 'Big_word': Big_word, 'words': words, 'Maximum':Maximum, 'Biggest_words':Biggest_words})

def about(request) :
	return render(request, 'about.html')