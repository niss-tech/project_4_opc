import json
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from .match_controller import MatchController
from views.report import Report

class TournamentController:
    def __init__(self, tournament_file="data/tournaments.json"):
        self.tournament_file = tournament_file
        self.tournaments = self.load_tournaments()
        self.match_controller = MatchController()

    def load_tournaments(self):
        """Charge les tournois depuis un fichier JSON."""
        try:
            with open(self.tournament_file, "r") as file:
                data = json.load(file)
                return [Tournament.from_dict(tournament) for tournament in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tournaments(self):
        """Sauvegarde les tournois dans un fichier JSON."""
        with open(self.tournament_file, "w") as file:
            json.dump([tournament.to_dict() for tournament in self.tournaments], file, indent=4)

    def create_tournament(self, name, location, start_date, end_date, description=""):
        """Crée un nouveau tournoi et sauvegarde."""
        tournament = Tournament(name, location, start_date, end_date, description)
        self.tournaments.append(tournament)
        self.save_tournaments()
        return tournament

    def add_player_to_tournament(self, tournament, player):
        """Ajoute un joueur à un tournoi."""
        if player not in tournament.players:
            tournament.add_player(player)
            self.save_tournaments()  # Sauvegarde dans le fichier JSON
        else:
            print("Ce joueur est déjà inscrit au tournoi.")

    def generate_round(self, tournament, round_controller):
        """Génère un round en utilisant RoundController."""
        new_round = round_controller.create_round(tournament)
        if new_round:
            self.save_tournaments()

    def list_rounds(self):
        """Liste tous les rounds du tournoi avec leurs numéros."""
        if not self.rounds:
            print("Aucun round n'a encore été créé.")
            return

        print(f"\nRounds du tournoi '{self.name}':")
        for round_ in self.rounds:
            print(f"- {round_.round_number}: {round_.name} (Matches : {len(round_.matches)})")

    def rank_players(self, tournament):
        """Classe les joueurs par leurs points totaux dans le tournoi."""
        # Trie les joueurs par ordre décroissant de leurs points
        sorted_players = sorted(tournament.players, key=lambda player: player.points, reverse=True)
        
        print("\n=== Classement des joueurs ===")
        for idx, player in enumerate(sorted_players, start=1):
            print(f"{idx}. {player.first_name} {player.last_name} - {player.points} points")
