"""
name = input("What's your name? ").strip().title()   

# split users name int ofirst and last name
first, last = name.split(" ")





# removes whitespace from str
# you can put multiple functions in the same line
# name = name.strip().title()
print(f"Hello, {first} {last}")
# the comma automatically adds a space
"""
def main():
    name = input("What's your name? ")
    hello(name)



def hello(to="world"):
    print("Hello,", to)


main()