from .round import Round
from .player import Player

class Tournament:
    def __init__(self, name, location, start_date, end_date, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.rounds = []
        self.players = []
        self.current_round = 0
        self.num_rounds = 4  # Valeur par défaut.

    def add_player(self, player: Player):
        """Ajoute un joueur au tournoi."""
        self.players.append(player)

    def add_round(self, round_instance: Round):
        """Ajoute un round au tournoi."""
        self.rounds.append(round_instance)
        self.current_round += 1

    def display_players(self):
        """Affiche la liste des joueurs inscrits dans le tournoi."""
        print(f"Joueurs inscrits dans le tournoi '{self.name}':")
        for player in self.players:
            print(f"- {player.first_name} {player.last_name} (ID: {player.chess_id})")

    def to_dict(self):
        """Convertit l'objet tournoi en dictionnaire."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "current_round": self.current_round,
            "num_rounds": self.num_rounds,
        }

    @classmethod
    def from_dict(cls, data):
        """Recrée un tournoi à partir d'un dictionnaire."""
        tournament = cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data.get("description", ""),
        )
        tournament.rounds = [Round.from_dict(round_) for round_ in data["rounds"]]
        tournament.players = [Player.from_dict(player) for player in data["players"]]
        tournament.current_round = data["current_round"]
        tournament.num_rounds = data["num_rounds"]
        return tournament
