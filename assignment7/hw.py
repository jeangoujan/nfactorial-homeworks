"""
Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n' 
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""
import math


def is_prime(n: int) -> bool:  #
    if (n % 2 == 0 and n > 2) or (n % 3 == 0 and n != 3) or (n % 5 == 0 and n != 5) or (n % 7 == 0 and n != 7) or (
            n % 9 == 0 and n != 9) or (n == 0 or n < 0 or n == 1):
        return False
    else:
        return True


"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that 
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""


def nth_fibonacci(n: int) -> int:
    num1 = 1
    num2 = 1
    if n == 1:
        return 0
    while n > 2:
        num1, num2 = num2, num1 + num2
        n = n - 1
    return num1


"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""


def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""


def count_vowels(s: str) -> int:
    counter = 0
    for i in s.lower():
        if i in ('a', 'e', 'o', 'u', 'i'):
            counter = counter + 1
    return counter


"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""


def sum_of_digits(n: int) -> int:
    x = list(str(abs(n)))
    counter = 0
    for i in x:
        counter = counter + int(i)
    return counter




"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""


def reverse_string(s: str) -> str:
    return s[::-1]


"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30 |
sum_of_squares(5) -> 55
"""


def sum_of_squares(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        result = result + (i * i)
    return result


"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""


def collatz_sequence_length(n: int) -> int:
    counter = 0
    if n < 0:
        return 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            counter = counter + 1
        else:
            n = n * 3 + 1
            counter = counter + 1
    return counter + 1


"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""


def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""


def count_words(s: str) -> int:
    str_list = s.split(" ")
    if str_list[0] == "":
        return 0
    else:
        if "" in str_list:
            return len(str_list) - 1
        return len(str_list)


"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""


def is_palindrome(s: str) -> bool:
    reversed_str = s[::-1]
    if reversed_str == s:
        return True
    else:
        return False


"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""


def sum_of_multiples(n: int, x: int, y: int) -> int:
    counter = 0
    for i in range(n + 1):
        if i % x == 0 or i % y == 0:
            counter = counter + i
    return counter


"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    else:
        return a*b//gcd(a,b)



"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2


"""


def count_characters(s: str, c: str) -> int:
    counter = 0
    for i in s:
        if i == c:
            counter = counter + 1
    return counter


"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""


def digit_count(n: int) -> int:
    x = str(n)
    counter = 0
    for i in x:
        counter = counter + 1
    return counter


"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""


def is_power_of_two(n: int) -> bool:
    if n // 2 % 2 == 0 or n == 2:
        return True
    else:
        return False




"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""


def sum_of_cubes(n: int) -> int:
    result = 0
    for i in range(0, n + 1):
        result = result + math.pow(i, 3)
    return int(result)



"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""


def is_perfect_square(n: int) -> bool:
    counter = 0
    for i in range(n):
        if math.pow(i, 2) == n or n == 1:
            counter = counter + 1
    return True if counter == 1 else False





"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""


def is_armstrong_number(n: int) -> bool:
    x = list(str(n))
    len_of_list = len(x)
    sum_of_nums = 0
    for i in x:
        sum_of_nums = sum_of_nums + (int(i) ** len_of_list)
    # print("sum= ", sum_of_nums)
    if sum_of_nums == n:
        return True
    else:
        return False
