"""
File where I rough test code before including it in the main files
"""
#nlp
import spacy

nlp = spacy.load('en')
document = open('./text-files/file1.txt').read()
document = nlp(document)

for ent in document.ents:
    if ent.label_ == "CARDINAL":
        continue
    print (ent, ent.label_)