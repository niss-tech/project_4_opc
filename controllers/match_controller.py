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
                    f"{idx}. {match.player_1.first_name} vs "
                    f"{match.player_2.first_name} (Scores: {match.score_1} - "
                    f"{match.score_2})"
                )

