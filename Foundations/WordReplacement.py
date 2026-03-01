sentence = input("Enter your sentence: ")
print("Your sentence is: ", sentence)

word1= input("Enter the word you want to replace: ")
word2 = input("Enter the word you want to replace with: ")
new_sentence = sentence.replace(word1, word2)
print("Your new sentence is: ", new_sentence)