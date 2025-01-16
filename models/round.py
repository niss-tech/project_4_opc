import datetime
from .match import Match

class Round:
    def __init__(self, name, round_number):
        self.name = name
        self.round_number = round_number
        self.matches = []
        self.start_time = datetime.datetime.now()
        self.end_time = None

    def end_round(self):
        self.end_time = datetime.datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "round_number": self.round_number,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
        }

    @classmethod
    def from_dict(cls, data):
        round_instance = cls(name=data["name"], round_number=data["round_number"])
        round_instance.matches = [Match.from_dict(match) for match in data["matches"]]
        round_instance.start_time = datetime.datetime.fromisoformat(data["start_time"])
        if data["end_time"]:
            round_instance.end_time = datetime.datetime.fromisoformat(data["end_time"])
        return round_instance
