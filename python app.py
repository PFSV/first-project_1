textfile = "/Users/pfsv/Desktop/var/text.txt"
'''textdata = open(textfile, 'r')
text = textdata.readlines()
for i in text:
    i.rstrip("\n")
    print(i)
textdata.close()'''

with open(textfile, 'r') as textdata:
    text = textdata.readlines()
    for i in text:
        print(i, end ="")