import os
import re
import shelve
from nltk.stem.porter import *
#f=1

stemmer=PorterStemmer()
#for f in range(900):
#	os.system("pdftotext a.pdf -f "+str(f)+" -l "+str(f)+" "+str(f)+".txt")


def imp_line(line):
	data=line.split(' ')
	if len(data)<6 and line[-1:].isalpha():
		return True
	else:
		return False


tokens=shelve.open('tokens1.db',writeback=True)
trivia=['is','are','am','his','that','in','out','it','design','yes','of','to','we','you','are','go','compute','file','algorithm','if','else','i','do','for','j','k','not']

for i in range(50,900):
		text=open(str(i)+'.txt','r').read().lower().split('\n')
		for line in text:
				if imp_line(line):				
						m=10000
				else:
						m=10

				_line=line.split(' ')
				for word in _line:
						word="".join([c for c in word if c.isalnum()])
						#word=word.lower()
						word=stemmer.stem(word)
						word.strip()
						#word.encode('ascii','ignore')
						word=str(word)
						if word not in trivia:
								if word not in tokens.keys():
										#word.encode("ascii",'ignore')
										#print word+"kk"
										tokens[word]={}
										tokens[word][i]=m
										tokens[word][0]=1
					

								else:
										if i not in tokens[word].keys():
												tokens[word][i]=m
												tokens[word][0]=tokens[word][0]+1
										else:
												tokens[word][i]=tokens[word][i]+m
												tokens[word][0]=tokens[word][0]+1
tokens.sync()
tokens.close()