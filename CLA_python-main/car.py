car = []


def add_car():
    make = input("Enter a car manufacturer: ")
    colour = input("Enter a car colour: ")
    year = input("Enter year manufactured: ")
    car_tuple = (make, colour, year)
    car.append(car_tuple)
    return car


def search_car(search_term):
    return [item for item in car if item[0] == search_term or item[1] == search_term or item[2] == search_term]


# only removes if first element is put in
def remove_car(remove_term):
    updated = list(filter(lambda x: x[0] != remove_term, car))
    return updated


if __name__ == '__main__':
    n = int(input("How many cars would you like to add: "))
    for i in range(n):
        add_car()
print("The list of cars is:", car)

search = input("Enter a search query: ")
if search_car(search):
    print("The cars found according to your search term are:", search_car(search))
else:
    print("The car cannot be found")

remove = input("Enter a manufacturer to remove: ")
if remove_car(remove):
    print("The final list is:", remove_car(remove))
else:
    print("The item to remove cannot be found")
