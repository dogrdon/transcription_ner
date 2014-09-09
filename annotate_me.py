import os
import sys
import spotlight
from pprint import pprint


transcription_txt = sys.argv[1]

txt_file = open(transcription_txt, 'rb')

text_contents = txt_file.read()

try:
	annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', text_contents, confidence=0.5, support=20)
	subjects = []


	for i in annotations:
		
		uri = i['URI']
		subject = uri.split('/')[-1]
		subjects.append(subject)

	counts = {}


	for word in subjects:
		
		if word in counts:

			counts[word] += 1
		else:

			counts[word] = 1

	outfile = open('./output/outtest.txt', 'w+')



	for k, v in counts.iteritems():
		if v >= 10:

			line = k + '\n'
			outfile.write(line)

	outfile.close()



except:
	print "sorry, the annotation failed for:", transcription_txt
	




#outfile = open('./output/test_output.txt', 'wb')

#outfile.write(annotations)

#outfile.close