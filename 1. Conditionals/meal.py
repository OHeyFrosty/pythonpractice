def main():
    time = input("What time is it? ")
    convert(time)
    
    


def convert(time):
    #splits the hour and minute into two seperate variables
    hours, minutes = time.split(":")
    #turns the two variables into floats
    hours = float(hours)
    minutes = float(minutes)
    #puts actual minutes into a float cause i couldnt maek it work last time
    new_minutes = minutes/60.0
    # adds together and return the final time as a float
    time = hours + new_minutes
    #checks what time it is and prints accordingly
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

#if __name__ == "__main__":
# ^this was in the original blueprint from cs50, but dont know wtf to do with it so if statements go in convert()
#im sure there is a better way to do this but im just a boy :3
main()