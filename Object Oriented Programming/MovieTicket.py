# Write a class called MovieTicket that inherits from the Ticket class of the previous problem. It should have the following (in addition to all that it gets from the Ticket class):

# A string field called movie_name

# A constructor that sets movie_name as well as cost and time

# Override the _str_() method so that it returns a string of the form MovieTicket(<cost>, <time>, <name>), where <cost>, <time>, and <name> are replaced with the values of the class's fields.

# A method called afternoon_discount() that returns a discount of 10 (standing for 10%) if the ticket time falls in the range from 12:00 to 17:59 and otherwise 0.

# Test the class by creating a MovieTicket item, printing it, and calling the afternoon_discount() and is_evening_time() methods.

class Ticket:
    def __init__(self, price, time):
        self.price = price
        self.time = time

    def __str__(self):
        return f"(<{self.price}>, <{self.time}>)"

    def is_evening_time(self):
        self.timeNum = ""
        for i in self.time:
            if i != ":":
                self.timeNum += i
        self.timeNum = int(self.timeNum)
        if 1800 < self.timeNum < 2360:
            return True
        return False

    def bulk_discount(self, n):
        self.n = n
        self.price = int(self.price) * self.n
        if 4 < self.n < 10:
            return f"Original Price: {self.price} \nPrice with 10% discount: {int(self.price)-int(self.price)*0.1}"
        elif self.n >= 10:
            return f"Original Price: {self.price} \nPrice with 20% discount: {int(self.price)-int(self.price)*0.2}"
        else:
            return f"Price: {self.price} (buy more than 5 tickets for discounts)"


class MovieTicket(Ticket):
    def __init__(self, movie_name, price, time):
        self.movie_name = movie_name
        super().__init__(price, time)

    def __str__(self):
        return f'<{self.movie_name}>, {super().__str__()}'

    def afternoon_discount(self):
        self.timeNum = ""

        for i in self.time:
            if i != ':':
                self.timeNum += i

        if 1200 <= int(self.timeNum) <= 1759:
            return f"Price with 10% discount: {int(self.price)-int(self.price)*0.1}$"

        return f"Price {self.price}$ (book between 12:00 to 17:59 to get 10% discount)"


ticket = MovieTicket("spiderman", 200, "12:59")

print(ticket.movie_name)
print(ticket.price)
print(ticket.time)
print(ticket.__str__())

print(ticket.afternoon_discount())
