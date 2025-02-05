class Player:
    def __init__(self, first_name, last_name, birth_date, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.points = 0.0  # Points accumulés dans un tournoi.

    def to_dict(self):
        """Convertit l'objet joueur en dictionnaire."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "points": self.points,
        }

    @classmethod
    def from_dict(cls, data):
        """Recrée un joueur à partir d'un dictionnaire."""
        player = cls(
            data["first_name"],
            data["last_name"],
            data["birth_date"],
            data["chess_id"],
        )
        player.points = data.get("points", 0.0)
        return player
