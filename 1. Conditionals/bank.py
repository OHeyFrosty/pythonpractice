#if it starts with hello, output $0
#if it starts with "h", output $20
#otherwise output $100
#ignore any leading whitespace, so use .strip somewhere

greet = input("Say a Greeting. ").strip()
if greet == "hello":
    print("$0")
elif greet.startswith("h", 0):
    print("$20")
else:
    print("$100")