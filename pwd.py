
def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(digit.isdigit() for digit in password)


def has_upper_letters(password):
    return any(upper_letter.isupper() for upper_letter in password)


def has_lower_letters(password):
    return any(lower_letter.islower() for lower_letter in password)


def has_symbols(password):
    return any(
        not symbol.isalpha()
        and not symbol.isdigit()
        for symbol in password
    )


def main():
    func_list = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    password = input('Введите пароль:')
    score = 0

    for i in func_list:
        if i(password):
            score += 2
    print('Рейтинг пароля:', score)


if __name__ == '__main__':
    main()
