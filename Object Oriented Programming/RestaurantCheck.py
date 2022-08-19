# Write a class called RestaurantCheck. It should have the following:
# Fields called check_number, sales_tax_percent, subtotal, table_number, and server_name representing an identification for the check, the bill without tax added, the sales tax percentage, the table number, and the name of the server.

# A method called calculate_total that takes no arguments (besides self) and returns the total bill including sales tax.

# A method called print_check that writes to a file called check###.txt, where ### is the check number and writes information about the check to that file, formatted like below:

# Check Number: 443
# Sales tax: 6.0%
# Subtotal: $23.14
# Total: $24.53
# Table Number: 17
# Server: Sonic the Hedgehog
# Test the class by creating a RestaurantCheck object and calling the print_check() method.

class RestaurantCheck:
    def __init__(self, check_number, sales_tax_percent, subtotal, table_number, server_name):
        self.check_number = check_number
        self.sales_tax_percent = sales_tax_percent
        self.subtotal = subtotal
        self.table_number = table_number
        self.server_name = server_name

    def calculate_total(self):
        return round(self.subtotal * (1+self.sales_tax_percent/100), 2)

    def printCheck(self):
        output = open('transaction no '+str(self.check_number)+'.txt', 'w')
        print("Check Number: ", self.check_number, file=output)
        print("Total without tax: ", self.subtotal, file=output)
        print("Sales tax percent: ", self.sales_tax_percent, "%", file=output)
        print("Total with tax: ", self.calculate_total(), file=output)
        print("Table no: ", self.table_number, file=output)
        print("Server name: ", self.server_name, file=output)

    def __str__(self):
        return f"""
        Check Number: {self.check_number} 
        Sales Tax: {self.sales_tax_percent} 
        Subtotal: {self.subtotal} 
        Table Number: {self.table_number}
        Server Name: {self.server_name}
        """


rc = RestaurantCheck(222, 6, 23.14, 5, "sonic hedge")

print(rc.__str__())
print("Total:", rc.calculate_total())
# rc.printCheck()
