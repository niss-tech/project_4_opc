import json
from models.player import Player


class PlayerController:
    def __init__(self, player_file="data/players.json"):
        self.player_file = player_file
        self.players = self.load_players()

    def load_players(self):
        """Charge les joueurs depuis un fichier JSON."""
        try:
            with open(self.player_file, "r") as file:
                data = json.load(file)
                return [Player.from_dict(player) for player in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_players(self):
        """Sauvegarde les joueurs dans un fichier JSON."""
        with open(self.player_file, "w") as file:
            json.dump([player.to_dict() for player in self.players], file, indent=4)

    def add_player(self, first_name, last_name, birth_date, chess_id):
        """Ajoute un joueur à la liste et sauvegarde."""
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        self.save_players()
        return new_player

    def get_players_sorted(self):
        """Renvoie les joueurs triés par ordre alphabétique."""
        return sorted(self.players, key=lambda p: (p.last_name, p.first_name))
