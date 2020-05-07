vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
word = []
def pigLatin(l):
    for idx, i in enumerate(l):
        if i[0] in vowels:
            i += 'yay'
            l[idx] = i
        elif i[1] in vowels:
            i += i[0] + 'ay'
            i = i.replace(i[0], '', 1)
            l[idx] = i
    return(l)

def stringSplitter(s):
    global word
    w = ''
    for i in s:
        if i == " ":
            word.append(w)
            w = ''
            continue
        w += i
s = input("Enter string : \n")
stringSplitter(s)
#word = ['hello', 'jam', 'tasty', 'food', 'and', 'icecream']
word = pigLatin(word)
print("\nTranslated to Pig-Latin : ")
for i in word:
    print(i, end = ' ')
