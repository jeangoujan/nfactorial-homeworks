import math


def exercise1():
    number1 = 11
    number2 = 89
    result = number1 + number2
    print(result)


def exercise2():
    str1 = "Wednesday, 9 October, 22:47"[::-1]
    print(str1)


def exercise3():
    str2 = "Thursday, 10 October, gotta be a nice day"
    print(len(str2))


def exercise4():
    str1 = "Snoop "
    str2 = "Dogg"
    print(str1 + str2)


def exercise5():
    char1 = 'a'
    if char1 in ('a', 'e', 'i', 'o', 'u'):
        print("Is Vowel")
    else:
        print("Is not Vowel")


def exercise6():
    str3 = "Friday, night"
    firstCh = str3[0]
    lastCh = str3[-1]
    middlePart = str3[1:-1]

    print(f'{lastCh}{middlePart}{firstCh}')


def exercise7():
    str4 = "Just a String".upper()
    print(str4)


def exercise8():
    rectangleLength = 20
    rectangleWidth = 10
    area = rectangleLength * rectangleWidth
    print(area)


def exercise9():
    exerciseNum = 10
    if exerciseNum % 2 == 0:
        print(f'{exerciseNum} is Even')
    else:
        print(f'{exerciseNum} is Odd')


def exercise10():
    str5 = "Saturday - finally rest"
    print(str5[:3])


def exercise11():
    name = "Damir"
    age = 23
    print(f'Привет, меня зовут {name}, мне {age} года')


def exercise12():
    strSlice = "Object-Oriented-Programming"
    print(strSlice[2:6])


def exercise13():
    strNum = "13"
    x = int(strNum)
    print(x)


def exercise14():
    repetitionStr = "Salam Alaikum"
    newStr = repetitionStr * 3
    print(newStr)


def exercise15():
    x = 6000
    y = 150

    print(f'Remainder = {x % y}')
    print(f'Quotient = {x // y}')


def exercise16():
    x = 15
    y = 4
    print(x / y)


def exercise17():
    str1 = "assignment6 % python3 main.py"
    print(f'Number of occurences of "a" character == {str1.count("a")}')


def exercise18():
    str2 = '"Declare a "string" with "double" quotes inside"'
    print(str2)


def exercise19():
    multiLineStr = """
    Hi, my name is Damir
    i'm 23 years old
    And i like to coding :)
    """
    print(multiLineStr)


def exercise20():
    x = 2
    y = 3
    print(math.pow(x, y))


def exercise21():
    palStr = "racecar"
    reversedStr = palStr[::-1]
    if palStr == reversedStr:
        print("It is a palindrome string")
    else:
        print("It is not palindrome string")


def exercise22():
    str1 = "act".lower()
    str2 = "tca".lower()
    counter = 0

    for i in str1:
        for j in str2:
            if i == j:
                counter = counter + 1
    if counter == len(str1) and counter == len(str2):
        print("They are anagrams")
    else:
        print("They are not anagrams")


if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()
    exercise13()
    exercise14()
    exercise15()
    exercise16()
    exercise17()
    exercise18()
    exercise19()
    exercise20()
    exercise21()
    exercise22()
