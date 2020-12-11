def two_sum(lst, target):
    check = []
    for num in lst:
        complement = target - num
        if complement in check:
            return [complement, num]
        else:
            check.append(num)


# The temporary n^3 solution that I will revisit
def three_sum(lst, target):
    for num1 in lst:
        for num2 in lst:
            for num3 in lst:
                if num1 + num2 + num3 == target and num1 != num2 != num3:
                    return [num1, num2, num3]


def main():
    with open('day1input.txt', 'r') as report:
        lst_report = report.read().splitlines()
    lst_report = [int(i) for i in lst_report]

    # Part 1
    print('Part 1:')
    numbers = two_sum(lst_report, 2020)
    print('The numbers are {}'.format(numbers))
    print('Their product is {}'.format(numbers[0] * numbers[1]))

    # Part 2
    print('\nPart 2:')
    numbers2 = three_sum(lst_report, 2020)
    print('The numbers are {}'.format(numbers2))
    print('Their product is {}'.format(numbers2[0] * numbers2[1] * numbers2[2]))


if __name__ == "__main__":
    main()

