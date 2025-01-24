from models.match import Match

class MatchController:
    def __init__(self):
        self.matches = []  # Garde une trace de tous les matchs


   

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


# def create_match(self, player_1, player_2):
    #     """Permet de créer un match entre deux joueurs et de l'ajouter à la liste des matchs."""
    #     if not player_1 or not player_2:
    #         print("Both players are required to create a match.")
    #         return None
    #     if player_1 == player_2:
    #         print("A player cannot play against themselves.")
    #         return None
        
    #     # Création du match sans score initial, car l'utilisateur le saisira plus tard
    #     new_match = Match(player_1, player_2)
    #     self.matches.append(new_match)
    #     print(f"Match created between {player_1.first_name} and {player_2.first_name}.")
    #     return new_match