# 1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers.
# Remember that we can use the sum function to add the values in an iterable.

def nums_sum(*args):
    return sum(args)


print(nums_sum(7, 3, 15, 100))

# 2) Create a function that accepts any number of positional and keyword arguments,
# and that prints them back to the user.
# Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def positional_and_keywords(*args, **kwargs):
    return f"Positional arguments: {args}. Keyword arguments: {kwargs.items()}"


print(positional_and_keywords("Welcome back ", "our dear", name="John", surname="Grecko"))

# 3) Print the following dictionary using the format method and ** unpacking.

country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
 }

print("(Name: {name}, Population: {population}, Capital: {capital}, Currency: {currency})".format(**country))

# 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas.
# You will have to provide an argument for print function's sep parameter for this exercise.

num_range = range(1, 21)
print(*num_range, sep=",")

# 5) Modify your code from exercise 4 so that each number prints on a different line.
# You can only use a single print call.

def n_range(*args):

    for num in args:
        print(num)

n_range(*num_range)

# Python code below
# Use print("messages...") to debug your solution.

# show_expected_result = False

class Student:
    scores = [65,75,85,95]

    def average_scores(self):
        list_of_scores = self.scores
        average = 0
        for score in list_of_scores:
            average += score

        return average / len(self.scores)


obj1 = Student()
print(obj1.average_scores())



