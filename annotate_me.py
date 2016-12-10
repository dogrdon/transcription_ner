import os
import sys
import spotlight
from pprint import pprint

dirname = sys.argv[1]
transcripts = os.listdir(dirname)

def createSubjects():
	while len(transcripts) > 0:
		for f in transcripts:
			curr_tscrpt = os.path.join(dirname, f)
			txt_file = open(curr_tscrpt, 'rb')
			text_contents = txt_file.read()
			getAnnotations(text_contents, f)
	else:
		print "That's it, I am done!"

def getAnnotations(textcontent, filename):
	try:
		outputname = os.path.join('./output/', filename)
		annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', textcontent, confidence=0.5, support=20)
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

		outfile = open(outputname, 'w+')

		for k, v in counts.iteritems():
			if v >= 10:
				line = k + '\n'
				outfile.write(line)

		outfile.close()
		transcripts.remove(filename)

		print len(transcripts), "left to annotate"
	except:
		print "sorry, the annotation failed for:", filename

if __name__ == "__main__":
	createSubjects()
