#Написать программу, которая считывает строку, проверяет,
# является ли она палиндромом (слова, читающиеся одинаково в обоих направлениях),
# и выводит сообщение о результате проверки.
# При этом, использовать функции reverse и рекурсию.


def check_palindrome(s: str) -> bool:
    #Если строка состоит из одного символа или меньше, она считается палиндромом
    if len(s) < 2:
        return True
    #Если первый и последний символы не совпадают, строка не является палиндромом
    elif s[0] != s[-1]:
        return False
    #В противном случае, функция вызывает сама себя, передавая подстроку,
    # в которой убраны первый и последний символы.
    # Рекурсия продолжается до тех пор, пока строка не будет уменьшена до одного символа или меньше.
    else:
        return check_palindrome(s[1:-1])

def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()