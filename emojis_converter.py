emojis = {":)" : "😊",
          ":(" : "🥺"}


message = input("Enter some text: ")
words = message.split(" ")

output = ""
for word in words:
    output+=emojis.get(word, word)

print(output)