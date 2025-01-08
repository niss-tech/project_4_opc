from models.tournament import Tournament
from models.player import Player
from models.round import Round


class TournamentController:
    def __init__(self):
        self.tournaments = []

    def create_tournament(self, name, location, start_date, end_date, description=""):
        """Créer un nouveau tournoi."""
        new_tournament = Tournament(name, location, start_date, end_date, description)
        self.tournaments.append(new_tournament)
        print(f"Tournament '{name}' created in {location}.")
        return new_tournament

    def add_player_to_tournament(self, tournament_name, player):
        """Ajouter un joueur à un tournoi spécifique."""
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            if player in tournament.players:
                print(f"Player {player.first_name} {player.last_name} is already in the tournament.")
            else:
                tournament.add_player(player)
                print(f"Player {player.first_name} {player.last_name} added to tournament '{tournament_name}'.")
        else:
            print(f"Tournament '{tournament_name}' not found.")

    def add_round_to_tournament(self, tournament_name, round_instance):
        """Ajouter un round à un tournoi spécifique."""
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            tournament.add_round(round_instance)
            print(f"Round '{round_instance.name}' added to tournament '{tournament_name}'.")
        else:
            print(f"Tournament '{tournament_name}' not found.")

    def list_tournaments(self):
        """Lister tous les tournois créés."""
        if not self.tournaments:
            print("No tournaments have been created yet.")
        else:
            print("Tournaments:")
            for idx, tournament in enumerate(self.tournaments, start=1):
                print(f"{idx}. {tournament.name} - {tournament.location} ({tournament.start_date} to {tournament.end_date})")

    def find_tournament_by_name(self, name):
        """Trouver un tournoi par son nom."""
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        print(f"Tournament '{name}' not found.")
        return None

    def display_tournament_details(self, name):
        """Afficher les détails d'un tournoi."""
        tournament = self.find_tournament_by_name(name)
        if tournament:
            print(f"Tournament: {tournament.name}")
            print(f"Location: {tournament.location}")
            print(f"Start Date: {tournament.start_date}")
            print(f"End Date: {tournament.end_date}")
            print(f"Description: {tournament.description}")
            print(f"Players:")
            for player in tournament.players:
                print(f"- {player.first_name} {player.last_name} (ID: {player.chess_id})")
            print(f"Rounds:")
            for round_ in tournament.rounds:
                print(f"- {round_.name} (Matches: {len(round_.matches)})")
        else:
            print(f"Tournament '{name}' not found.")

    def save_to_file(self, filename="tournaments.json"):
        """Sauvegarder les tournois dans un fichier JSON."""
        import json
        with open(filename, "w") as file:
            json.dump([tournament.to_dict() for tournament in self.tournaments], file)
        print(f"Tournaments saved to {filename}.")

    def load_from_file(self, filename="tournaments.json"):
        """Charger les tournois depuis un fichier JSON."""
        import json
        from models.tournament import Tournament
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tournaments = [Tournament.from_dict(tournament) for tournament in data]
            print(f"Tournaments loaded from {filename}.")
        except FileNotFoundError:
            print(f"No file named {filename} found. Starting fresh.")
