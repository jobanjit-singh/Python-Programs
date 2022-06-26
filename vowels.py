def replacevowels(word):
    for x in 'aeiouAEIOU':
        word=word.replace(x,'')
    return word
str=input("Enter the string: ")
print("String without vowels is:",replacevowels(str))