counts=dict()
line = input('Enter the line of text\n')
words = line.split()


print('Words:', words)
print('Counting...')#count the words in the file

for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts',counts)
print(list(counts.keys()))
print(list(counts.values()))
print(list(counts.items()))

for aaa,bbb in counts.items():
    print(aaa,bbb)
    