adults = 0
seniors = 0
babies = 0

def get_age():
    while True:
        age = input("Input an age: ")
        if age>= 999:
            print(adults)
            print(seniors)
            print(babies)
            return False
        elif age > 17:
            adults + 1
            if age > 70:
                seniors + 1
        elif age < 2:
            babies + 1

get_age()