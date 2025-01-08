from models.round import Round
from models.match import Match

class RoundController:
    def __init__(self):
        self.rounds = []

    def create_round(self, name, round_number, matches=None):
        """Créer un nouveau round avec une liste de matchs."""
        new_round = Round(name, round_number, matches)
        self.rounds.append(new_round)
        print(f"Round '{name}' has been created.")
        return new_round

    def list_rounds(self):
        """Lister tous les rounds créés."""
        if not self.rounds:
            print("No rounds have been created yet.")
        else:
            print("Rounds:")
            for round_ in self.rounds:
                print(f"{round_.round_number}. {round_.name}")

    def add_match_to_round(self, round_number, match):
        """Ajouter un match à un round existant."""
        for round_ in self.rounds:
            if round_.round_number == round_number:
                round_.matches.append(match)
                print(f"Match added to round {round_.name}.")
                return round_
        print(f"Round {round_number} not found.")
        return None
