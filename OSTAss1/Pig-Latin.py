vowels = ('a', 'e', 'i', 'o', 'u')
word = []

def pigLatin(l):
    for i, j in enumerate(l):
        if j[0].lower() in vowels:	#if initial letter is vowel, end with 'yay'
            j += 'yay'
            l[i] = j
            
        elif 'sh' in j.lower():
            j = j.replace('Sh', 'Ch')
            j = j.replace('sh', 'ch')
            l[i] = j

        elif 'th' in j.lower():
            j = j.replace('th', 'z')
            j = j.replace('Th', 'Z')
            l[i] = j

        elif 'ch' in j.lower():
            j = j.replace('Ch', 'sh')
            j = j.replace('ch', 'sh')
            l[i] = j

        elif j[0].lower() == 'c':	#if initial letter is 'c', replace with 'k'
            j = j.replace(j[0], 'k', 1)
            l[i] = j

        elif j[1].lower() in vowels:	#if 2nd letter is vowel, shift 1st letter to the end and append 'ay'
            j += j[0] + 'ay'
            j = j.replace(j[0], '', 1)
            l[i] = j
            
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
        
s = input("Enter string            : ")
stringSplitter(s)
#print(word)
#word = ['hello', 'jam', 'tasty', 'food', 'and', 'icecream']
word = pigLatin(word)
#print(word)
print("\nTranslated to Pig-Latin : ", end='')
for i in word:
    print(i, end = ' ')
