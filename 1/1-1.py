def amazing_solution():
    with open("input1.txt", "r") as file1:
        print(sum([1 if x == "(" else -1 for x in file1.readline()[:-1]]))


if __name__ == "__main__":
    amazing_solution()
