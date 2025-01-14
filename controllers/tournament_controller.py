import json
from models.tournament import Tournament
from models.round import Round
from models.match import Match

class TournamentController:
    def __init__(self, tournament_file="data/tournaments.json"):
        self.tournament_file = tournament_file
        self.tournaments = self.load_tournaments()

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


    def generate_round(self, tournament):
        """Génère un round pour un tournoi."""
        if tournament.current_round >= tournament.num_rounds:
            return None  # Le tournoi est terminé.

        # Tri des joueurs par score et génération des paires
        players = sorted(tournament.players, key=lambda p: -p.points)
        matches = []
        while players:
            player1 = players.pop(0)
            player2 = players.pop(0) if players else None
            if player2:
                matches.append(Match(player1, player2))

        round_name = f"Round {tournament.current_round + 1}"
        new_round = Round(name=round_name)
        new_round.matches = matches
        tournament.add_round(new_round)
        self.save_tournaments()
        return new_round
