from .player import Player

class Match:
    def __init__(self, player_1, player_2, score_1=0.0, score_2=0.0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def to_dict(self):
        return {
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict(),
            "score_1": self.score_1,
            "score_2": self.score_2,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            player_1=Player.from_dict(data["player_1"]),
            player_2=Player.from_dict(data["player_2"]),
            score_1=data["score_1"],
            score_2=data["score_2"],
        )
