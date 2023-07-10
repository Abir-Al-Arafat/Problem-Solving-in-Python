# Write a Python class to convert any number given by user to roman symbols. The data is given below.
# values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
# symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL" "X", "IX", "V", "IV", "I"]


class NumberToRoman:
    def toRoman(self, number):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        romanSymbol = ''
        index = 0

        while number > 0:
            for _ in range(number//values[index]):
                # adding symbol
                romanSymbol += symbols[index]
                # deducting number
                number -= values[index]
            index += 1

        return romanSymbol


print(NumberToRoman().toRoman(35))
print(35//1000)
