from models.match import Match

class MatchController:
    def __init__(self):
        self.matches = []  # Garde une trace de tous les matchs

    def create_match(self, player_1, player_2):
        """Permet de créer un match entre deux joueurs et de l'ajouter à la liste des matchs."""
        if not player_1 or not player_2:
            print("Both players are required to create a match.")
            return None
        if player_1 == player_2:
            print("A player cannot play against themselves.")
            return None
        
        # Création du match sans score initial, car l'utilisateur le saisira plus tard
        new_match = Match(player_1, player_2)
        self.matches.append(new_match)
        print(f"Match created between {player_1.first_name} and {player_2.first_name}.")
        return new_match

    def enter_match_results(self):
        """Permet à l'utilisateur de saisir les résultats pour tous les matchs existants."""
        if not self.matches:
            print("No matches available to enter results.")
            return
        
        print("Enter results for the following matches:")
        for idx, match in enumerate(self.matches, start=1):
            print(f"{idx}. {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name}")
            print("Choose the result:")
            print("1 - Player 1 wins")
            print("2 - Player 2 wins")
            print("3 - Draw")
            result = input("Enter your choice (1/2/3): ")

            if result == "1":
                match.score_1 = 1.0
                match.score_2 = 0.0
            elif result == "2":
                match.score_1 = 0.0
                match.score_2 = 1.0
            elif result == "3":
                match.score_1 = 0.5
                match.score_2 = 0.5
            else:
                print("Invalid choice, score not updated.")
                continue

            print(f"Result for match: {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name} -> {match.score_1} - {match.score_2}")

    def list_matches(self):
        """Liste tous les matchs créés, avec les scores enregistrés."""
        if not self.matches:
            print("No matches have been created yet.")
        else:
            print("Matches:")
            for idx, match in enumerate(self.matches, start=1):
                print(
                    f"{idx}. {match.player_1.first_name} vs {match.player_2.first_name} "
                    f"(Scores: {match.score_1} - {match.score_2})"
                )
