class Report:
    @staticmethod
    def display_players(players):
        """Affiche une liste des joueurs."""
        print("\n=== Liste des Joueurs ===")
        for player in players:
            print(f"{player.last_name}, {player.first_name} ({player.chess_id})")

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche une liste des tournois."""
        print("\n=== Liste des Tournois ===")
        for tournament in tournaments:
            print(f"{tournament.name} - {tournament.start_date} à {tournament.end_date}")

    @staticmethod
    def display_tournament_details(tournament):
        """Affiche les détails d'un tournoi."""
        print(f"\n=== Tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} à {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print(f"Nombre de tours : {tournament.num_rounds}")
        print("Joueurs inscrits :")
        for player in tournament.players:
            print(f"- {player.last_name}, {player.first_name} ({player.chess_id})")

    @staticmethod
    def display_rounds(tournament):
        """Affiche les rounds d'un tournoi et leurs matchs."""
        print(f"\n=== Rounds du tournoi : {tournament.name} ===")
        for round_instance in tournament.rounds:
            print(f"{round_instance.name} :")
            for match in round_instance.matches:
                player1, player2 = match.player1, match.player2
                print(f"  {player1.first_name} {player1.last_name} ({player1.points}) vs "
                      f"{player2.first_name} {player2.last_name} ({player2.points})")
