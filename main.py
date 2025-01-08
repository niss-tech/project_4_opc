from controllers.player_controller import PlayerController
from controllers.match_controller import MatchController
from controllers.round_controller import RoundController

# Initialiser les contrôleurs
player_controller = PlayerController()
match_controller = MatchController()
round_controller = RoundController()

# Exemple d'utilisation
# Créer des joueurs
player1 = player_controller.create_player("John", "Doe", "1990-01-01", "P1")
player2 = player_controller.create_player("Jane", "Smith", "1985-06-15", "P2")

# Lister les joueurs
player_controller.list_players()

# Créer un match
match = match_controller.create_match(player1, player2, 1.0, 0.5)

# Lister les matchs
match_controller.list_matches()

# Créer un round et y ajouter un match
round1 = round_controller.create_round("Round 1", 1)
round_controller.add_match_to_round(1, match)

# Lister les rounds
round_controller.list_rounds()
