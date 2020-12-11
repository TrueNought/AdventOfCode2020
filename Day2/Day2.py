import re


def read_input(file):
    with open(file, 'r') as text:
        password_list = text.read().splitlines()
        for index in range(len(password_list)):
            password_list[index] = re.split(' |-|: ', password_list[index])
    return password_list


def part_one_check(passwords):
    valid = 0
    for password in passwords:
        if int(password[0]) <= password[3].count(password[2]) <= int(password[1]):
            valid += 1
    return valid


def part_two_check(passwords):
    valid = 0
    for password in passwords:
        if (password[3][int(password[0])-1] == password[2]) is not (password[3][int(password[1])-1] == password[2]):
            valid += 1
    return valid


def main():
    parsed = read_input('day2input.txt')

    # Part 1
    print('Part 1:')
    result = part_one_check(parsed)
    print('Total number of valid passwords is {}'.format(result))

    # Part 2
    print('\nPart 2:')
    new_result = part_two_check(parsed)
    print('Total number of valid passwords is {}'.format(new_result))


if __name__ == "__main__":
    main()
