class car:

    def __init__(self, make, colour, year, owner_name):
        self.make = make
        self.colour = colour
        self.year = year
        self.owner_name = owner_name

    @classmethod
    def from_input(cls):
        return cls(
            input("Manufacturer: "),
            input("Colour: "),
            input("Year: "),
            input("Owner: ")
        )

    def owned_cars(self):
        pass

    def search_by_owner(self):
        pass


n = int(input("How many cars do you want to add ?"))
owners = {}
for x in range(n):
    owner = car.from_input()
    owners[owner.owner_name] = owner
print(owners)
