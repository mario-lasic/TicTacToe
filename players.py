class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.board = []
        self.winner = False

    possibleCombinations = [
        ("1", "2", "3"),
        ("4", "5", "6"),
        ("7", "8", "9"),
        ("1", "4", "7"),
        ("2", "5", "8"),
        ("3", "6", "9"),
        ("1", "5", "9"),
        ("3", "5", "7"),
    ]

    def check_winner(self) -> bool:
        for combination in self.possibleCombinations:
            if all(x in self.board for x in combination):
                self.winner = True
                break
        return self.winner

    def get_field(self, fields: list[str]) -> str:
        while True:
            used = fields
            print(used)
            try:
                turn = input(f"{self.name} select number from 1-9 to pick field: ")
                int_number = int(turn)
                while turn in used or int_number not in range(1, 10):
                    turn = input("Please select number from 1 to 9: ")
                break
            except ValueError:
                print("Please use numbers!")
                continue

        self.board.append(turn)
        return turn
