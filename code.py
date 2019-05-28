f = open("ciphertext.txt", 'r')
string = f.read()
word = []
s_word = []
word2 = []
s_word2 = []
result = ""
switch = True
for i in range(65,91):
    word.append(chr(i))
print(word)
for j in range(len(word)):
    word2.append(word[len(word)-j-1])
print(word2)
for i in range(97,123):
    s_word.append(chr(i))
print(s_word)
for j in range(len(s_word)):
    s_word2.append(s_word[len(word)-j-1])
print(s_word2)

for i in range(len(string)):
    for j in range(len(word)):
        if(string[i] == word[j]):
            result = result + word2[j]
            switch = False
        elif(string[i] == s_word[j]):
            result = result + s_word2[j]
            switch = False
    if(switch):
        result = result + " "
    switch = True
print(result)

