from .round import Round
from .player import Player


class Tournament:
    def __init__(self, name, location, start_date, end_date, description="", num_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.players = []
        self.rounds = []
        self.current_round = 0
        self.played_matches = set()  # Paires de joueurs ayant déjà joué

    def add_player(self, player: Player):
        """Ajoute un joueur au tournoi."""
        self.players.append(player)

    def add_round(self, round_instance: Round):
        """Ajoute un round au tournoi."""
        if not round_instance.matches:
            print(f"Le round {round_instance.name} n'a pas de matchs.")
            return
        self.rounds.append(round_instance)
        self.current_round = round_instance.round_number  # Mise à jour centralisée


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

