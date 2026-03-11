messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)
    print(f"Message: '{message}' → Length: {length}")
    
    if length > 10:
        print("This message is longer than 10 characters")
    
    print()  # for spacing