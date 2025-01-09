from controllers.player_controller import PlayerController

# Créer une instance unique du contrôleur
player_controller = PlayerController()

# Ajouter des joueurs
player_controller.create_player("John", "Doe", "1990-01-01", "1234")
player_controller.create_player("Jane", "Smith", "1985-05-12", "5678")

# Lister les joueurs
player_controller.list_players()

# Sauvegarder dans un fichier
player_controller.save_to_file()

# Charger depuis un fichier
player_controller.load_from_file()

