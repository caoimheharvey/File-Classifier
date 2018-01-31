"""
File where I rough test code before including it in the main files

import spacy

nlp = spacy.load('en')
document = open('./text-files/file1.txt').read()
document = nlp(document)

for ent in document.ents:
    if ent.label_ == "CARDINAL":
        continue
    print (ent, ent.label_)
"""
import docx2txt

def compare(file1_path, file2_path):
    from difflib import SequenceMatcher
    #file1 = open(file1_path).read()
    file2 = open(file2_path).read()
    similarity = SequenceMatcher(None, file1_path, file2)
    print(similarity.ratio())

text = docx2txt.process("./text-files/test.docx")

print(text)

compare(text, "./text-files/file1.txt")


