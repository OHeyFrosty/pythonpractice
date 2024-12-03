def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #this is how i wanted to try to complete perfect_to_float, but couldnt figure out how to properly make the percent into a decimal
    dollars = d.replace("$","")
    return float(dollars)


def percent_to_float(p):
    # this I found off stackoverflow, couldnt figure out how to really do it my way but i guess thats just how coding works.
    return float(p.strip('%'))/100


main()