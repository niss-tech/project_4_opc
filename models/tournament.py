from .round import Round
from .player import Player


class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, description: str = ""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.rounds = []
        self.players = []
        self.current_round = 0
        self.num_rounds = 4  # Default number of rounds

    def add_player(self, player: Player):
        """Add a player to the tournament."""
        self.players.append(player)

    def add_round(self, round_instance: Round):
        """Add a round to the tournament."""
        self.rounds.append(round_instance)
        self.current_round += 1

    def to_dict(self):
        """Convert the tournament instance to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "current_round": self.current_round,
            "num_rounds": self.num_rounds
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Tournament instance from a dictionary."""
        tournament_instance = cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data.get("description", "")
        )
        tournament_instance.rounds = [Round.from_dict(round_) for round_ in data["rounds"]]
        tournament_instance.players = [Player.from_dict(player) for player in data["players"]]
        tournament_instance.current_round = data["current_round"]
        tournament_instance.num_rounds = data["num_rounds"]
        return tournament_instance
