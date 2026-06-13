#detect spam messages

spam_keywords = ["free", "win", "prize", "click here", "subscribe now"]

messages = input("Enter your message: ")

if any(keyword in messages.lower() for keyword in spam_keywords):
    print("This message is likely to be spam.")
else:    
    print("This message is not likely to be spam.")


print(type(spam_keywords))
print(type(messages))
