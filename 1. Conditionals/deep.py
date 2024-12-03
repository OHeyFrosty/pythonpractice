
life = input("What is the answer to the Great question of Life, the Universe, and Everything? ")
match life:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
    
"""
def main():
    life = input("What is the answer to the Great question of Life, the Universe, and Everything? ")
    if is_answer(life):
        print("Yes")
    else:
        print("No")

def is_answer(life):     
    match life:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False
        
main()
"""

