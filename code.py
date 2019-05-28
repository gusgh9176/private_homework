def isNum(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
f = open("ciphertext.txt", 'r')
key = int(input())
string = f.read()
word = []
s_word = [] #word to word2(Upper)
word2 = []
s_word2 = []
result = ""
switch = True
for i in range(65,91):
    word.append(chr(i))
    word2.append(chr(i))

for j in range(key):
    temp = word2.pop(0)
    word2.append(temp)
    
print(word)
print(word2)
for i in range(97,123):
    s_word.append(chr(i))
    s_word2.append(chr(i))
    
for j in range(key):
    temp = s_word2.pop(0)
    s_word2.append(temp)
    
print(s_word)
print(s_word2)

for i in range(len(string)):
    for j in range(len(word)):
        if(string[i] == word[j]):
            result = result + word2[j]
            switch = False
            continue
        elif(string[i] == s_word[j]):
            result = result + s_word2[j]
            switch = False
            continue
    if(switch and !(string[i].isspace())):
        result = result + string[i]
        switch = False
    else
        result = result + " "
    switch = True
print(result)
f.close()

