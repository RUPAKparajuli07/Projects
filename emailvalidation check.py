while True:
    email = input("Enter email address: ")
    at_index = email.find("@")
    dot_index = email.rfind(".")

    if email == "":
        print("Email address not entered. Exiting loop.")
        break
    elif at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
        print("Valid email.")
        choice = input("Do you want to enter another email address (yes/no)? ")
        if choice.lower() == "yes":
            continue
        else:
            break
    else:
        print("Invalid email. Try again.")
        
