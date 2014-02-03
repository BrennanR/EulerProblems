import itertools


def is_number_palindrome(number):
    number_string = str(number)
    str_len = len(number_string)
    x = str_len - 1

    for i in itertools.count():
        if number_string[i] != number_string[x]:
            return False
        if i >= x:
            break

        x -= 1

    return True


def find_largest_three_digit_palindrome():
    largest_palindrome = 0
    three_digit_values = range(100, 999)

    for threeDigitValue in three_digit_values:
        for threeDigitValue2 in reversed(three_digit_values):
            if is_number_palindrome(threeDigitValue * threeDigitValue2):
                if threeDigitValue * threeDigitValue2 > largest_palindrome:
                    largest_palindrome = threeDigitValue * threeDigitValue2

    return largest_palindrome


print(str(find_largest_three_digit_palindrome()))