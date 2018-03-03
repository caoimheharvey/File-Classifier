import os
import docx2txt as doc

textArr = []
rootDir = './text-files'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
       if fname.endswith(('.txt', '.docx')):
           textArr.append(dirName + "/" + fname)

# compare docx file to a text file with the same text
from difflib import SequenceMatcher
file1 = './text-files/file4.txt'
file2 = doc.process('./text-files/test.docx')

res = SequenceMatcher(None, open(file1, 'r').read(), file2)
print(res.ratio())

#compare one docx to multiple text files
def compare(file, file_path, list):
    from difflib import SequenceMatcher

    list_len = len(list)
    counter = 0
    for key, value in list.items():
        if file_path in list.keys():
            return "skip",""
        else:
    #todo:error on this line
            if SequenceMatcher(None, file, checkextension(key)).ratio() > 0.7:
                return "add", key
            elif counter != list_len:
                continue
            elif counter == list_len:
                return "new", ""

        counter += 1
    return "new", ""

def checkextension(file):
    import docx2txt
    if file.lower().endswith('.txt'):
        field1 = open(file, 'r').read()
        return field1
    else:
        field1 = docx2txt.process(file)
        return field1

def mainFileComp(paths):
    from collections import defaultdict

    dd = defaultdict(list)
    final = defaultdict(list)

    for i in range(len(paths)):
        if(len(dd) == 0):
            dd[paths[i]]
        else:
            contents = checkextension(paths[i])
            res , key = compare(contents, paths[i], dd)
            if res == "add":
                dd[key].append(paths[i])
            elif res == "new":
                dd[paths[i]]
            elif res == "skip":
                continue
    for k , v in dd.items():
        if dd[k]:
            final[k] = v
    return final



ans = mainFileComp(textArr)
for key, value in ans.items():
    print(key,value)