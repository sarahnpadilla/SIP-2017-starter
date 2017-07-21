print("submit any number.")
user_input= (input())
number = int(user_input) #variable for users input.
multiples = 0 # using (multiples) as a start off count from 0.
for loop in range(number):
    multiples = multiples +1 #counts off each number.
    if multiples %3 == 0 and multiples %5 == 0: #multiples of 3 and 5 starting from 0 will print "fizzbuzz".
        print("fizzbuzz")
    elif multiples %3 == 0:
        print("fizz")
    elif multiples %5 == 0:
        print("buzz")
    else:
        print(multiples) #all other numbers that aren't multiples of 3 or 5 will print as numbers.
