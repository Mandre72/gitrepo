#Level 1
#Task 1
#def foo_bar(n: int):
    #for i in range(1, n + 1):
        # Check if the number is divisible by 3 and print 'Bin'
       # if i % 3 == 0:
            #print("Bin", end="")

        # Check if the number is divisible by 7 and print 'Go'
        #if i % 7 == 0:
            #print("Go", end="")

        # If the number is not divisible by 3 or 7, print the number itself
        #if i % 3 != 0 and i % 7 != 0:
            #print(i, end="")

        # Print a newline character to start a new line for the next number
        #print()


# Call the function to print numbers from 1 to 100
#foo_bar(100)


#Task 2
#def sum_numbers(n: int):
    # Initialize the variable 'final_sum' and set it to 0 initially
    #final_sum = 0

    # Use a loop to iterate over numbers from 1 to n (inclusive)
    #for i in range(1, n + 1):
        # Convert the number to a string to iterate through its digits
        #num_str = str(i)

        # Iterate through the digits of the number and add them to 'final_sum'
        #for digit in num_str:
            #final_sum += int(digit)

    # Return the 'final_sum' as the result
    #return final_sum


#n = 5
#result = sum_numbers(n)
#print(f"Result for n={n}: {result}")  # Output: Result for n=5: 15


#Level 2
#def find_max(a: int, b: int, c: int):
    #if a > b and a > c:
        #return a

    #if b > a and b > c:
        #return b

    #if c > a and c > b:
        #return c


#num1 = 124
#num2 = 21
#num3 = 32

#print(find_max(num1, num2, num3))

#def leap_year(year: int):
    #if year % 4 == 0:
        #if year % 100 == 0:
            #if year % 400 == 0:
                #print(f"{year}is a leap year")
            #else:
                #print(f"{year}is not a leap year")
        #else:
            #print(f"{year}is a leap year")
    #else:
        #print(f"{year}is not a leap year")


#leap_year(1992)
#leap_year(2000)
#leap_year(2100)
#leap_year(2071)


#level3
def generate_fibonacci_sequence(n: int):
    fib_sequence = [0, 1]

    for i in range(2, n):

        next_fib = fib_sequence[-1] + fib_sequence[-2]

        fib_sequence.append(next_fib)

    return fib_sequence


n = 7
result = generate_fibonacci_sequence(n)
print(result)
