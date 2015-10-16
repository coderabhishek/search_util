from search import search
from nltk.stem.porter import *
import sys
import pyttsx

stemmer=PorterStemmer()

engine=pyttsx.init()
voices=engine.getProperty('voices')
voice=voices[2]
engine.setProperty('voice',voice.id)
engine.setProperty('rate',100)
engine.setProperty('gender','male')

print "What do you want me to search?"

query=raw_input()

pages=search(query)
query_list=query.lower().split(' ')





def get_page_data(page_index):
		word_matched=0
		newstring=''				
		if not pages:
			engine.say("Query NOT FOUND")
			engine.runAndWait()
			sys.exit()
		else:
				page_index=0;
				text=open('test_data/'+str(pages[page_index])+'.txt','r').read()
				text_list=text.lower().split()	
				for word in query_list:
					for j in range(len(text_list)):
							str1=text_list[j]
							str1="".join([c for c in str1 if c.isalnum()])
							str1=stemmer.stem(str1)
							str1=str1.strip()
							word="".join([c for c in word if c.isalnum()])
							word=str(stemmer.stem(word))
							word=word.strip()
							if hash(str1)==hash(word):
									#print text_list[j],word
									newstring=' '.join(text_list[j:])
									word_matched=1
									break
					if word_matched==1:
						break
		print newstring	
		engine.say(newstring.strip()[:200])
		engine.runAndWait()
		sys.exit()
			


get_page_data(0)














