file_name = input("What is the file name: ")
with open(file_name) as data:
    para = data.read()
    numlines = len(para.split('\n'))-1

    vowels = 0
    consonants = 0
    non_letter = 0

    for i in para:
        if i.isalpha():
            if( i in ['A','E','I','O','U','a','e','i','o','u']):
                vowels += 1
            else:
                consonants += 1
        elif i == '\n':
            continue
        else :
            non_letter += 1

print("There are", vowels, "vowels")
print("There are", consonants, "consonants")
print("There are", non_letter, "non-letter characters")
print("There are",numlines, "lines")
 
