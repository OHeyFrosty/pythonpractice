def convert(faces):
    smile = faces.replace(":)", "🙂")
    sad = smile.replace(":(","🙁")
    return sad


def main():
    faces = input("Insert a :) or :( ")
    text = convert(faces)
    print(text)


main()