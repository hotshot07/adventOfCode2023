cool_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

map_cool = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}


def extract_number(yo: str):
    straight_keys = list(cool_map.keys())
    reverse_keys = list(map_cool.keys())
    first_str = ""
    second_str = ""
    first_digit = ""
    last_digit = ""

    for x in yo:
        if first_digit:
            break

        first_str += x

        if x.isdigit():
            first_digit = x
            break

        for number in straight_keys:
            if number in first_str:
                first_digit = cool_map.get(number)
                break

    for x in yo[::-1]:
        if last_digit:
            break

        second_str += x

        if x.isdigit():
            last_digit = x
            break

        for number in reverse_keys:
            if number in second_str:
                last_digit = map_cool.get(number)
                break

    print(str(first_digit) + str(last_digit) + "\n")
    return int(str(first_digit) + str(last_digit))


def not_amazing_solution():
    with open("input1.txt", "r") as file1:
        print(sum([extract_number(x) for x in file1.readlines()]))


if __name__ == "__main__":
    not_amazing_solution()
