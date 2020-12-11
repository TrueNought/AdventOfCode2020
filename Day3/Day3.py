def count_trees(route, right, down):
    total_trees = 0
    index = 0
    index_length = len(route[0]) - 1
    height = 0

    while height < len(route):
        if route[height][index] == '#':
            total_trees += 1

        index += right
        height += down

        if index > index_length:
            index -= index_length + 1

    print('Total trees encountered: {}'.format(total_trees))
    return total_trees


def main():
    with open('day3input.txt', 'r') as file:
        path = file.read().splitlines()

    # Part 1
    print('Part 1')
    count_trees(path, 3, 1)

    # Part 2
    print('\nPart 2')

    r_increments = [1, 3, 5, 7, 1]
    d_increments = [1, 1, 1, 1, 2]
    product = 1

    for i in range(len(r_increments)):
        product *= count_trees(path, r_increments[i], d_increments[i])

    print('Product is {}'.format(product))


if __name__ == "__main__":
    main()
