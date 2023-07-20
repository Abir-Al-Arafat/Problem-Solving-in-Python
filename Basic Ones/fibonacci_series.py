# create a function which takes a number as input and returns a list which contains a fibonacci series

# fibonacci series: first and second element will be 0 and 1 and any other element of the series will be sum of previous two elements
def fibonacciSeries(limit):
    fibonacci_series = []
    fibonacci_series.append(0)
    fibonacci_series.append(1)

    for idx in range(2, limit):
        fibonacci_series.append(
            fibonacci_series[idx-1]+fibonacci_series[idx-2])

    return fibonacci_series


print(fibonacciSeries(10))
