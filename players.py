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

    def check_winner(self):
        for combination in self.possibleCombinations:
            if all(int(x) in self.board for x in combination):
                self.winner = True 
                return self.winner
            else:
                print("Some elements of the tuple are not in the list")
        return self.winner

