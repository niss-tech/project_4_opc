from models.match import Match
from models.player import Player

class MatchController:
    def __init__(self):
        self.matches = []

    def create_match(self, player_1, player_2, score_1=0.0, score_2=0.0):
        """Créer un nouveau match entre deux joueurs."""
        new_match = Match(player_1, player_2, score_1, score_2)
        self.matches.append(new_match)
        print(f"Match created between {player_1.first_name} and {player_2.first_name}.")
        return new_match

    def list_matches(self):
        """Lister tous les matchs créés."""
        if not self.matches:
            print("No matches have been created yet.")
        else:
            print("Matches:")
            for idx, match in enumerate(self.matches, start=1):
                print(
                    f"{idx}. {match.player_1.first_name} vs {match.player_2.first_name} "
                    f"(Scores: {match.score_1} - {match.score2})"
                )
