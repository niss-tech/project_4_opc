from models.player import Player
import json

class PlayerController:
    def __init__(self):
        self.players = []

    def create_player(self, first_name, last_name, birth_date, chess_id):
        """Créer un nouveau joueur et l'ajouter à la liste des joueurs."""
        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)
        print(f"Player {new_player.first_name} {new_player.last_name} has been created.")
        return new_player

    def list_players(self):
        """Lister tous les joueurs créés."""
        if not self.players:
            print("No players have been created yet.")
        else:
            print("Players:")
            for idx, player in enumerate(self.players, start=1):
                print(f"{idx}. {player.first_name} {player.last_name} (ID: {player.chess_id})")

    def find_player_by_id(self, chess_id):
        """Trouver un joueur par son identifiant d'échecs."""
        for player in self.players:
            if player.chess_id == chess_id:
                return player
        print(f"No player found with ID {chess_id}.")
        return None

    def update_player(self, chess_id, first_name=None, last_name=None, birth_date=None):
        """Mettre à jour les informations d'un joueur."""
        player = self.find_player_by_id(chess_id)
        if player:
            if first_name:
                player.first_name = first_name
            if last_name:
                player.last_name = last_name
            if birth_date:
                player.birth_date = birth_date
            print(f"Player {chess_id} has been updated.")
            return player
        return None

    def save_to_file(self, filename="players.json"):
            """Save players to a JSON file."""
            with open(filename, "w") as file:
                json.dump([player.to_dict() for player in self.players], file)

    def load_from_file(self, filename="players.json"):
        """Load players from a JSON file."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.players = [Player.from_dict(player) for player in data]
        except FileNotFoundError:
            print(f"No existing file named {filename} found. Starting fresh.")