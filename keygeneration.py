import random


def key_generation(input_data=111):
    capital_alphabet_numbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    numbers_and_letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = []
    key_first_part = ''
    for number in range(5):
        key_first_part += random.choice(numbers_and_letters)
    key.append(key_first_part)
    number_part = 1
    for i, el in enumerate(str(input_data)):
        copy_last_part = list(key[number_part - 1])
        copy_last_part.pop(random.randint(0, len(copy_last_part) - 1))
        new_part = ''.join(copy_last_part)
        new_part_to_key = ''
        if i % 2 == 0:
            for j in range(5 - i - 1):
                new_part_to_key += capital_alphabet_numbers[
                    (capital_alphabet_numbers.index(new_part[j]) + int(el)) % 36]
        else:
            for j in range(5 - i - 1):
                new_part_to_key += capital_alphabet_numbers[capital_alphabet_numbers.index(new_part[j]) - int(el)]
        number_part += 1
        key.append(new_part_to_key)
    return '-'.join(key)


if __name__ == '__main__':
    input_data = input('Введите трехзначное число: ')
    print(key_generation(input_data=111))
