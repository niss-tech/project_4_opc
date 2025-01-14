import unittest
from controllers.tournament_controller import TournamentController
from models.player import Player

class TestTournamentController(unittest.TestCase):
    def setUp(self):
        self.controller = TournamentController(tournament_file="test_tournaments.json")

    def tearDown(self):
        import os
        if os.path.exists("test_tournaments.json"):
            os.remove("test_tournaments.json")

    def test_create_tournament(self):
        tournament = self.controller.create_tournament("Test Tournament", "Paris", "2025-01-01", "2025-01-05")
        self.assertEqual(tournament.name, "Test Tournament")
        self.assertEqual(tournament.location, "Paris")
        self.assertEqual(tournament.start_date, "2025-01-01")
        self.assertEqual(tournament.end_date, "2025-01-05")
        self.assertIn(tournament, self.controller.tournaments)

    def test_add_player_to_tournament(self):
        tournament = self.controller.create_tournament("Test Tournament", "Paris", "2025-01-01", "2025-01-05")
        player = Player("John", "Doe", "1990-01-01", "AB12345")
        self.controller.add_player_to_tournament(tournament, player)
        self.assertIn(player, tournament.players)
