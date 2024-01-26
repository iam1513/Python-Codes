class FootballPlayer:
    def __init__(self, name, team, goals_scored):
        self.name = name  # Public attribute
        self._team = team  # Protected attribute
        self.__goals_scored = goals_scored  # Private attribute

    def get_goals_scored(self):
        return self.__goals_scored

    def _training(self):
        print(f"{self.name} is attending a team training session.")

    def __private_function(self):
        print("This is a private function for internal use.")

# Example usage:
if __name__ == "__main__":
    player1 = FootballPlayer("Messi", "Barcelona", 30)

    # Public access
    print(f"{player1.name} belongs to {player1._team}")

    # Protected access
    player1._training()

    # Private access
    # Note: Accessing private attributes/methods is discouraged, but still possible
    print(f"{player1.name} has scored {player1._FootballPlayer__goals_scored} goals.")
    player1._FootballPlayer__private_function()
