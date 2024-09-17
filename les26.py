#resuable function
def emoji_converted(message):
    separate_words = message.split(' ')
    print(separate_words)

    emoji = {
        ":(": "😢",
        ":)": "😊"
    }

    output = ""
    for word in separate_words:
        output += emoji.get(word, word) + " "

    return output.strip()  # Return the final output after the loop


message = input("Type your message: ")
result = emoji_converted(message)
print(result)
