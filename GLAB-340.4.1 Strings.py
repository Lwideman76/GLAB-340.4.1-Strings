#Word Play game

#Get user input for a word
word = input("Enter a word: ")

#Print the length of a word 
print("Length of word:", len(word))

#Print the word in uppercase and lowercase 
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())

#Count occurences of a letter
letter = input("Enter a letter: ")
print(f"'{letter}' appears {word.count(letter)} time(s) in '{word}'")

#Count occurences of a substring 
substring = input("Enter a substring: ")
print(f"'{substring}' appears {word.count(substring)} time(s) in '{word}'")

#Reverse the word
print("Reverse:", word[::-1])

#Slice the word based on starting and ending index 
start_index = int(input("Enter a starting index: "))
end_index = int(input("Enter an ending index: "))
print("Sliced word:", word[start_index:end_index])

#Replace a character 
char_to_replace = input("Enter a character to replace: ")
replacement_char = input("Enter the replacement character: ")
replaced_word = word.replace(char_to_replace, replacement_char, 1)
print("Replaced:", replaced_word)

#Concatenate with a second word
second_word = input("Enter a second word: ")
concatednated_word = word + second_word
print("Concatenated:", concatednated_word)

#Check if the word is a palindrome
if word == word[::-1]:
    print("Is a palindrome? Yes")
else:
    print("Is a palindrome? No")

#Check if the word is a valid Python identifer
if word.isidentifier():
    print("Is a valid Python identifier? Yes")
else:
    print("Is a valid Python identifier? No")
