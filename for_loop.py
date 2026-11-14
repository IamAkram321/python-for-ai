"""
  LOOPS IN PYTHON

 Loop: A loop is used to execute a block of code repeatedly.

 There are two main types of loops in Python:

 1. for loop: It is used to repeat a block of code for a specific
    number of times or to iterate over a sequence of items.

 2. while loop: It is used to repeat a block of code as long as
    a given condition is True.

  PART 1: FOR LOOP

 A `for` loop is used to execute a block of code repeatedly.

Syntax of for-loop:
 for i in range(start, end, step):
      #program


 Explanation:
 - `start`: Starting value (default is 0).
 - `end`: Ending value (excluded).
 - `step`: Increment or decrement value (default is 1).
 - `i`: Loop variable that stores the current value in each iteration.

  FOR-LOOP SAMPLE PROGRAMS

1. Print a name 5 times

 Without using a loop:

 print("Akram")
 print("Akram")
 print("Akram")
 print("Akram")
 print("Akram")
 

 Using a loop:
 for i in range(5):
     print("Akram")

2. Print numbers from 0 to 9

 for i in range(10):
     print(i)
 
3. Print numbers from 1 to 10

 for i in range(1, 11):
     print(i)
 

4. Print numbers from 10 to 1
 
 for i in range(10, 0, -1):
     print(i)
 

5. Print even numbers from 2 to 20

 for i in range(2, 21, 2):
     print(i)
 

6. Print odd numbers from 1 to 19

 for i in range(1, 20, 2):
     print(i)
 

7. Print even numbers from 1 to 20 using if condition
 
 for i in range(1, 21):
     if i % 2 == 0:
         print(i)
 

8. Print odd numbers from 1 to 20 using if condition

 for i in range(1, 21):
     if i % 2 != 0:
         print(i)
 

9. Find the sum of numbers from 1 to N

 n = int(input("Enter a number: "))
 total = 0
 for i in range(1, n + 1):
     total += i

 print("Sum =", total)
 

10. Print squares of numbers from 1 to 10

 for i in range(1, 11):
     print(i * i)
 

  11. Find the sum of squares from 1 to N

 n = int(input("Enter a number: "))
 total = 0
 for i in range(1, n + 1):
     total += i * i
 print("Sum of squares =", total)
 

  12. Print the multiplication table of user's choice

 Using f-string:

 n = int(input("Enter a number: "))
 for i in range(1, 11):
     print(f"{n} X {i} = {n * i}")
 

 Without using f-string:

 
 n = int(input("Enter a number: "))

 for i in range(1, 11):
     print(n, "X", i, "=", n * i)
 

  13. Print multiplication tables from 1 to 10 (Nested for-loop)

 
 for i in range(1, 11):
     print("--------------")

     for j in range(1, 11):
         print(i, "X", j, "=", i * j)
 

 Using f-string:

 
 for i in range(1, 11):
     print(f"\nMultiplication Table of {i}")
     print("-----------------------------")

     for j in range(1, 11):
         print(f"{i} X {j} = {i * j}")
 

  14. Count the total number of even numbers from 1 to N

 
 n = int(input("Enter a number: "))
 count = 0

 for i in range(1, n + 1):
     if i % 2 == 0:
         count += 1

 print("Total even numbers =", count)
 

  15. Find the factorial of a number

 Factorial is the product of all positive integers from 1 to a given number.

 Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

 
 n = int(input("Enter a number: "))
 fact = 1

 for i in range(1, n + 1):
     fact *= i

 print("Factorial =", fact)
 

  16. Print numbers divisible by both 3 and 5 from 1 to 100

 
 for i in range(1, 101):
     if i % 3 == 0 and i % 5 == 0:
         print(i)
 

  17. Print the following star pattern

 text
 *
 **
 ***
 ****
 *****
 

 
 for i in range(1, 6):
     print("*" * i)
 

  18. Print the following number pattern

 text
 1
 12
 123
 1234
 12345
 

 
 for i in range(1, 6):
     for j in range(1, i + 1):
         print(j, end="")
     print()
 

  19. Print the following reverse star pattern

 text
 *****
 ****
 ***
 **
 *
 

 
 for i in range(5, 0, -1):
     print("*" * i)
 

 ---

  PART 2: WHILE LOOP

 A `while` loop is used to execute a block of code repeatedly as long as the given condition is True.

  Syntax of while-loop

 
 while condition:
      program
 

 **Explanation:**
 - `while`: Keyword used to create a while loop.
 - `condition`: The loop continues as long as the condition is True.
 - The condition is checked before every iteration.
 - When the condition becomes False, the loop stops.

 **Important:** In a while loop, we generally need to update the variable inside the loop. Otherwise, the loop may run forever (infinite loop).

  WHILE-LOOP SAMPLE PROGRAMS

  1. Print a name 5 times

 
 i = 1

 while i <= 5:
     print("Akram")
     i += 1
 

  2. Print numbers from 1 to 10

 
 i = 1

 while i <= 10:
     print(i)
     i += 1
 

  3. Print numbers from 10 to 1 (Reverse order)

 
 i = 10

 while i >= 1:
     print(i)
     i -= 1
 

  4. Print even numbers from 2 to 20

 
 i = 2

 while i <= 20:
     print(i)
     i += 2
 

  5. Print odd numbers from 1 to 19

 
 i = 1

 while i <= 19:
     print(i)
     i += 2
 

  6. Print even numbers from 1 to 20 using if condition

 
 i = 1

 while i <= 20:
     if i % 2 == 0:
         print(i)

     i += 1
 

  7. Find the sum of numbers from 1 to N

 
 n = int(input("Enter a number: "))
 i = 1
 total = 0

 while i <= n:
     total += i
     i += 1

 print("Sum =", total)
 

  8. Print squares of numbers from 1 to 10


 i = 1

 while i <= 10:
     print(i * i)
     i += 1
 

  9. Find the sum of squares from 1 to N

 
 n = int(input("Enter a number: "))
 i = 1
 total = 0

 while i <= n:
     total += i * i
     i += 1

 print("Sum of squares =", total)
 

  10. Print the multiplication table of user's choice

 
 n = int(input("Enter a number: "))
 i = 1

 while i <= 10:
     print(f"{n} X {i} = {n * i}")
     i += 1
 

  11. Find the factorial of a number

 
 n = int(input("Enter a number: "))
 i = 1
 fact = 1

 while i <= n:
     fact *= i
     i += 1

 print("Factorial =", fact)
 

  12. Count the total number of even numbers from 1 to N

 
 n = int(input("Enter a number: "))
 i = 1
 count = 0

 while i <= n:
     if i % 2 == 0:
         count += 1

     i += 1

 print("Total even numbers =", count)
 

  13. Print multiplication tables from 1 to 10 (Nested while-loop)

 
 i = 1

 while i <= 10:
     print(f"\nMultiplication Table of {i}")
     print("-----------------------------")

     j = 1

     while j <= 10:
         print(f"{i} X {j} = {i * j}")
         j += 1

     i += 1
 

14. Keep asking for a password until the correct password is entered

 
 password = ""

 while password != "python123":
     password = input("Enter your password: ")

 print("Login successful!")
 

  15. Keep asking for numbers until the user enters 0, then display their sum

 total = 0
 num = 1

 while num != 0:
     num = int(input("Enter a number (0 to stop): "))
     total += num

 print("Total sum =", total)
 

16. Simple guessing game

 secret_number = 7
 guess = 0

 while guess != secret_number:
     guess = int(input("Guess the number: "))

     if guess < secret_number:
         print("Too low!")

     elif guess > secret_number:
         print("Too high!")

 print("Congratulations! You guessed correctly.")
 

 ---

PART 3: DIFFERENCE BETWEEN FOR LOOP AND WHILE LOOP

for loop:

Used to iterate over a sequence or repeat a known number of times.
Generally uses `range()` for number-based repetition.
Usually updates the loop variable automatically when using `range()`.
Useful for counting and multiplication tables.


while loop:

Used when repetition depends on a condition.
Uses a condition to control repetition.
Usually requires manual updating of the variable.
Useful for password checking and guessing games.

Example: Same task using both loops:

Using for loop:

 for i in range(1, 6):
     print(i)
 

 Using while loop:

 i = 1
 while i <= 5:
     print(i)
     i += 1
 

 Both produce the same output:

 text
 1
 2
 3
 4
 5
 

 ---

PART 4: LOOP CONTROL STATEMENTS

 Loop control statements are used to change the normal execution of a loop.

 There are three important loop control statements:

 1. break
 2. continue
 3. pass

  1. Break statement

 The `break` statement is used to terminate a loop immediately when a particular condition is satisfied.

 Example:

 for i in range(1, 11):
     if i == 5:
         break

     print(i)
 

 Output:

 text
 1
 2
 3
 4
 

Using while loop:

 i = 1

 while i <= 10:
     if i == 5:
         break

     print(i)
     i += 1
 

  2. Continue statement

 The `continue` statement is used to skip the current iteration and move to the next iteration of the loop.

 Example:

  for i in range(1, 11):
     if i == 5:
         continue

     print(i)
 

 Output:

 text
 1
 2
 3
 4
 6
 7
 8
 9
 10
 

 Using while loop:

 
 i = 0

 while i < 10:
     i += 1

     if i == 5:
         continue

     print(i)
 

  3. Pass statement

 The `pass` statement does nothing. It is used as a placeholder when we don't want to write any code inside a block yet.

 Example:

 
 for i in range(1, 6):
     if i == 3:
         pass

     print(i)
 

 Output:

 text
 1
 2
 3
 4
 5
 

 Remember:
 - `break` = Exit the loop.
 - `continue` = Skip the current iteration.
 - `pass` = Do nothing.

 ---

  PART 5: PRACTICE QUESTIONS

  A. For-loop practice

 1. Print your name 20 times using a for loop.
 2. Print numbers from 1 to 50.
 3. Print numbers from 50 to 1 in reverse order.
 4. Print all multiples of 5 from 1 to 100.
 5. Print all odd numbers between 1 and 100.
 6. Find the sum of all even numbers from 1 to N.
 7. Find the sum of all odd numbers from 1 to N.
 8. Find the product of numbers from 1 to N.
 9. Print the multiplication table of a number entered by the user, from 1 to 20.
 10. Count how many numbers between 1 and N are divisible by 3.
 11. Find the sum of all numbers divisible by both 3 and 5 between 1 and N.
 12. Find the factorial of a number entered by the user.
 13. Print all numbers from 1 to 100 except multiples of 5.
 14. Print the following pattern:

 text
 1
 22
 333
 4444
 55555
 #program:

 for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")

    print()

 15. Print the following pattern:


     *
    ***
   *****
  *******
 *********
 
 for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()

  B. While-loop practice

 1. Print numbers from 1 to 100 using a while loop.
 2. Print numbers from 100 to 1 in reverse order.
 3. Print all even numbers from 1 to 50.
 4. Print all odd numbers from 1 to 50.
 5. Find the sum of numbers from 1 to N.
 6. Find the factorial of a number.
 7. Print the multiplication table of a number entered by the user.
 8. Keep asking the user to enter a password until the correct password is entered.
 9. Keep accepting numbers from the user until they enter 0, then calculate the sum.
 10. Create a number guessing game.
 11. Count how many digits are present in a given number.
 12. Find the sum of digits of a given number.

  C. Loop control statement practice

 1. Print numbers from 1 to 20 but stop when the number reaches 12 using `break`.
 2. Print numbers from 1 to 20 but skip multiples of 3 using `continue`.
 3. Use `pass` inside a loop when the number is 5.
 4. Print numbers from 1 to 100 but stop when a number divisible by both 7 and 11 is found.


 """