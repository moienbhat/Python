p1   =    "Make a lot of money"
p2   =    "buy now"
p3   =    "Subscribe this"
p4   =    "Click This"

message = input("Enter the message: ")

if((p1 in message) or(p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam")

else:
    print("This is not a spam")