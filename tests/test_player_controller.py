import unittest
from controllers.player_controller import PlayerController

class TestPlayerController(unittest.TestCase):
    def setUp(self):
        self.controller = PlayerController(player_file="test_players.json")

    def tearDown(self):
        import os
        if os.path.exists("test_players.json"):
            os.remove("test_players.json")

    def test_add_player(self):
        player = self.controller.add_player("John", "Doe", "1990-01-01", "AB12345")
        self.assertEqual(player.first_name, "John")
        self.assertEqual(player.last_name, "Doe")
        self.assertEqual(player.birth_date, "1990-01-01")
        self.assertEqual(player.chess_id, "AB12345")
        self.assertIn(player, self.controller.players)

    def test_get_players_sorted(self):
        self.controller.add_player("Alice", "Smith", "1985-05-20", "CD67890")
        self.controller.add_player("Bob", "Brown", "1992-11-11", "EF54321")
        sorted_players = self.controller.get_players_sorted()
        self.assertEqual(sorted_players[0].last_name, "Brown")
        self.assertEqual(sorted_players[1].last_name, "Smith")
