sentence = input("Enter a sentence: ")
sentence = sentence.upper()
vowels = ('A','E','I','O','U')
vowels_count = 0
consonants_count = 0
non_letter_count = 0
for i in sentence:
    if i in vowels:
        vowels_count = vowels_count + 1
    elif ord(i) in range(ord('A'), ord('Z')):
        consonants_count = consonants_count + 1
    else:
        non_letter_count = non_letter_count + 1

print("There are", vowels_count, "vowels")
print("There are",consonants_count,"consonants")
print("There are", non_letter_count,"non-letter characters")
print("The string in all capital letters is:")
print(sentence)
    
