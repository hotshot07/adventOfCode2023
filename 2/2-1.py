import re

regex = r"Game (\d+):(.+)"

test_str = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"


class Game:
    def __init__(self, game_number, match_string) -> None:
        self.game_number = game_number
        self.match_string = match_string
        self.max_red = 0
        self.max_blue = 0
        self.max_green = 0
        self.parse_matchstring()

    def parse_matchstring(self):
        games = self.match_string.split(";")

        for game_string in games:
            balls_strings = game_string.split(",")
            for ball_string in balls_strings:
                if "red" in ball_string:
                    number_of_balls = int(ball_string.strip().split(" ")[0])
                    if number_of_balls > self.max_red:
                        self.max_red = number_of_balls
                if "green" in ball_string:
                    number_of_balls = int(ball_string.strip().split(" ")[0])
                    if number_of_balls > self.max_green:
                        self.max_green = number_of_balls
                if "blue" in ball_string:
                    number_of_balls = int(ball_string.strip().split(" ")[0])
                    if number_of_balls > self.max_blue:
                        self.max_blue = number_of_balls

    def is_valid(self):
        return self.max_red <= 12 and self.max_green <= 13 and self.max_blue <= 14

    def power(self):
        return self.max_red * self.max_green * self.max_blue


def extract_game(game_string: str) -> Game:
    matches = re.findall(regex, game_string)
    return Game(matches[0][0], matches[0][1].strip())


def amazing_solution1():
    with open("input2.txt", "r") as file1:
        games = [extract_game(x) for x in file1.readlines()]
        total = 0
        for game in games:
            if game.is_valid():
                total += int(game.game_number)
        print(total)


def amazing_solution2():
    with open("input2.txt", "r") as file1:
        print(sum([extract_game(x).power() for x in file1.readlines()]))


if __name__ == "__main__":
    amazing_solution2()
