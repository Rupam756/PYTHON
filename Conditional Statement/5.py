# find the given word is present in list or not

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

word_to_find = input("Enter a word to find: ")
if word_to_find in words:
    print(word_to_find, "is present in the list.")
else:   
    print(word_to_find, "is not present in the list.")