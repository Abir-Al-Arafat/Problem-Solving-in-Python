# Write a class called Ticket that has the following:

# A field cost for the price of the ticket and a string field time for the start time of the event (assume times are in 24-hour format, like '18:35').A constructor that sets those variables

# An _str_ method that returns a string of the form Ticket(<cost>, <time>), where <cost> and <time> are replaced with the values of the cost and time fields.

# • A method called is_evening_time() that returns True or False, depending on whether the time falls in the range from 18:00 to 23:59.

# • A method called bulk_discount() that takes an integer n and returns the discount for buying n tickets. There should be a 10% discount for buying 5 to 9 tickets, and a 20% discount for buying 10 or more. Otherwise, there is no discount.

# Return these percentages as integers. Test the class by creating a Ticket item, printing it, calling the is_evening_time() method, and calling the bulk_discount() method.

class Ticket:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time

    def __str__(self):
        return f"(<{self.price}>, <{self.time}>)"

    def is_evening_time(self):
        self.timeNum = ""

        for i in self.time:
            if(i != ":"):
                self.timeNum += i

        self.timeNum = int(self.timeNum)

        if 1600 <= self.timeNum < 2400:
            return True
        return False

    def bulk_discount(self, quantity):
        self.quantity = quantity
        self.bulkPrice = int(self.cost)*self.quantity

        if 5 <= self.quantity <= 9:
            return f"Original price: {self.bulkPrice}$ \n discounted price: {self.bulkPrice-(self.bulkPrice*0.1)}$"

        if self.quantity >= 10:
            return f"Original price: {self.bulkPrice}$ \n discounted price: {self.bulkPrice-(self.bulkPrice*0.2)}$"

        return f"Price: {self.bulkPrice}$ (buy 5 or more tickets for discount)"


ticket = Ticket("10", "16:00")

print(type(ticket.time))

print(ticket.is_evening_time())

print(ticket.bulk_discount(3))
