   # Discussion Question 1
    
 # 1. Compare and contrast the following pairs of terms:
 # a) definite loop vs. indefinite loop
 # A definite loop and an indefinite loop are similar in the way that they both allow a program to keep running. They are different in the way that an indefinite loop keeps running for an undefined amount of times, whereas a definite loop runs until a specific condition is met.
 # b) for loop vs. while loop
 # A “for loop” prints for every item in a list, whereas a “while” loop prints as long as a condition is met and stops when the condition is no # longer met.
 # c) interactive loop vs. sentinel loop
 # The major difference between an “interactive loop” and a “sentinel loop” is that an “interactive loop” prompts the user to continue after each input. On the other hand a “sentinel loop” will skill ask you user if they wish to continue but will end when a set condition or value is met.
 # d) sentinel loop vs. end-of-file loop
 # The difference between a “sentinel loop” and an “end-of-file loop” is that as stated previously a sentinel loop uses a specific value to bring an end to the loop, and a “end-of-file loop” will keep running until the end of the program is reached.

 # Discussion Question 2
def truth_table():
    headers = ["P", "Q", "R", "not(P and Q)", "(not P) and Q", "(not P) or (not Q)", "(P and Q) or R", "(P or R) and (Q or R)"]
    results = []

    for p in [False, True]:
        for q in [False, True]:
            for r in [False, True]:
                result_row = []
                result_row.append(p)
                result_row.append(q)
                result_row.append(r)
                result_row.append(not (p and q))
                result_row.append((not p) and q)
                result_row.append(not p or not q)
                result_row.append((p and q) or r)
                result_row.append((p or r) and (q or r))
                results.append(result_row)
    print('|', end=' ')
    for header in headers:
        print(f'{header:^15}|', end=' ')
    print('\n', '=' * (16 * len(headers) + 1))
    for row in results:
        print('|', end=' ')
        for val in row:
            print(f'{str(val):^15}|', end=' ')
        print()

truth_table()

   # Discussion Question 3 a,c
  # A
def sum_first_n_counting_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

  # C
def sum_until_999():
    total = 0
    num = int(input("Enter a number (999 to stop): "))
    while num != 999:
        total += num
        num = int(input("Enter a number (999 to stop): "))
    return total

  # Programming Exercise 1

def fibonacci_number(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1

    for i in range(2, n):
        c = a + b
        a, b = b, c

    return b

user_input = int(input("Enter the value of n to find the nth Fibonacci number: "))

result = fibonacci_number(user_input)
print(f"The {user_input}th Fibonacci number is: {result}")

# Programming Exercise 1

def syracuse_sequence(starting_value):
    sequence = [starting_value]
    
starting_value = int(input("Enter a starting value for the Syracuse sequence: "))
sequence = [starting_value]

while starting_value != 1:
    if starting_value % 2 == 0:
        starting_value //= 2
    else:
        starting_value = starting_value * 3 + 1
    sequence.append(starting_value)

print("Syracuse sequence:", sequence)
