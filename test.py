class Tournament:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

# Test
tournament = Tournament()
tournament.add_player("Joueur 1")
print(tournament.players)  # Devrait afficher : ['Joueur 1']
