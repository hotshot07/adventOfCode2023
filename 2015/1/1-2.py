def amazing_solution():
    with open("input1.txt", "r") as file1:
        floors = [1 if x == "(" else -1 for x in file1.readline()[:-1]]
        total = 0
        print(
            [
                total := total + value if total >= 0 else index
                for index, value in enumerate(floors)
            ].index(-1)
            + 1
        )


if __name__ == "__main__":
    amazing_solution()
