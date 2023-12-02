def extract_number(yo: str) -> int:
    nums = [x for x in yo if x.isdigit()]
    return int(str(nums[0]) + str(nums[-1]))


def amazing_solution():
    with open("input1.txt", "r") as file1:
        print(sum([extract_number(x) for x in file1.readlines()]))


if __name__ == "__main__":
    amazing_solution()
