class Game():

    def __init__(self):
        pass

    def two_player_game(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return "It's a draw!"

        if (player_1.choice == "Rock" and player_2.choice == "Scissors") or (player_1.choice == "Paper" and player_2.choice == "Rock") or (player_1.choice == "Scissors" and player_2.choice == "Paper"):
            return player_1.name.upper() + " is the winner!"

        if (player_2.choice == "Rock" and player_1.choice == "Scissors") or (player_2.choice == "Paper" and player_1.choice == "Rock") or (player_2.choice == "Scissors" and player_1.choice == "Paper"):
            return player_2.name.upper() + "  is the winner!"
