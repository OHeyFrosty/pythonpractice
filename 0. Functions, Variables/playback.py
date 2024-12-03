msg = input("Give me a statement. ")
#takes the messages and replaces every blank space with 3 periods, this is done indefinitely until there are no more blank spaces
new_msg = msg.replace(" ", "...")

print(new_msg)