from datetime import datetime
from match import Match

class Round:
    def __init__(self, name, round_number, matches=None, start_date=None, end_date=None):
        self.name = name
        self.round_number = round_number
        self.start_date = start_date if start_date else datetime.now().replace(microsecond=0)
        self.end_date = end_date
        self.matches = matches if matches else []

    def to_dict(self):
        """Convert the round instance to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "round_number": self.round_number,
            "matches": [match.to_dict() for match in self.matches],
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Round instance from a dictionary."""
        return cls(
            name=data["name"],
            round_number=data["round_number"],
            matches=[Match.from_dict(match) for match in data["matches"]],
            start_date=datetime.fromisoformat(data["start_date"]) if data.get("start_date") else None,
            end_date=datetime.fromisoformat(data["end_date"]) if data.get("end_date") else None
        )
