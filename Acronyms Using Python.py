while True:
    user_input = input("Enter a Phrase (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    text = user_input.split()
    result = ""
    for word in text:
        result += word[0].upper()
    print(result)
