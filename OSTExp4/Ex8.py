
#Picks out items in a sequence (use range from -5 to 5) that are less than zero
print(list(filter(lambda x: x < 0, range(-5, 5))))

print(list(filter(lambda x: x>0, range(-5,5))))

#I have a list (iterable) of my favourite pet names, all in lower case
#and I need them in uppercase.
#(try this without and with map function)
pets = ['tom', 'jerry', 'husky']
for i in pets:
    print(i.upper())
print(list(map(lambda x: x.upper(), ['tom', 'jerry', 'husky'])))

#Initialize a list (iterable) of the scores of 10 students in a Maths
#exam. Let's filter out those who passed with scores more than 75...using
#filter

marks = [10, 20, 40, 50, 30, 80, 60, 70, 90, 100]

print(list(filter(lambda x: x > 75, marks)))


#Write a python code for palindrome detector. Let's filter out words
#that are palindromes from a tuple (iterable) of suspected palindromes.

words = ['mom', 'bro', 'dad', 'sis']

print(list(filter(lambda x: x == x[::-1], words)))
