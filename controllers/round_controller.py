from models.round import Round
from models.match import Match

class RoundController:
    def __init__(self):
        self.rounds = []

    def create_round(self, name, round_number, matches=None):
        """Créer un nouveau round avec une liste de matchs."""
        new_round = Round(name, round_number)
        if matches:
            new_round.matches = matches
        self.rounds.append(new_round)
        print(f"Round '{name}' has been created.")
        return new_round

    def list_rounds(self):
        """Liste les rounds créés jusqu'à présent."""
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

    def enter_match_results(self, round_number):
        """Permet à l'utilisateur de saisir les résultats des matchs pour un round donné."""
        # Recherche du round spécifié
        rounds_dict = list(map(lambda round_obj: round_obj.to_dict(), self.rounds))
        print(rounds_dict)
        round_ = next((r for r in self.rounds if r.round_number == round_number), None)
        if not round_:
            print(f"Round {round_number} not found.")
            return

        # Affichage des matchs et saisie des résultats
        print(f"Enter results for Round {round_number}: {round_.name}")
        for match in round_.matches:
            print(f"Match: {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name}")
            print("Choose the result:")
            print("1 - Player 1 wins")
            print("2 - Player 2 wins")
            print("3 - Draw")
            result = input("Enter your choice (1/2/3): ")

            # Attribution des scores en fonction du choix de l'utilisateur
            if result == "1":
                match.score_1 = 1.0  # Player 1 gagne
                match.score_2 = 0.0  # Player 2 perd
            elif result == "2":
                match.score_1 = 0.0  # Player 1 perd
                match.score_2 = 1.0  # Player 2 gagne
            elif result == "3":
                match.score_1 = 0.0  # match nul
                match.score_2 = 0.0  # match nul
            else:
                print("Invalid choice, score not updated.")
                continue  # Demander à nouveau si le choix est invalide

            print(f"Result updated for match: {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name}")

        # Afficher les scores des matchs après mise à jour
        print("\nUpdated match results:")
        for match in round_.matches:
            print(f"{match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name} => {match.score_1} - {match.score_2}")
