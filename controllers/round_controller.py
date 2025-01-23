from models.round import Round
from models.match import Match
from views.report import Report
import random

class RoundController:
    def __init__(self):
        self.rounds = []  # Stocker les rounds si nécessaire

    def create_round(self, tournament):
        """Créer un nouveau round de façon dynamique."""
        if tournament.current_round >= tournament.num_rounds:
            print("Le tournoi est terminé.")
            return None

        # Vérifie qu'il y a assez de joueurs
        if len(tournament.players) < 8:
            print("Il faut au moins 8 joueurs pour créer un round.")
            return None

        # Mélanger les joueurs aléatoirement avant de créer le premier round
        if tournament.current_round == 0:  # Si c'est le premier round
            print("\nMélange des joueurs pour le premier round...")
            random.shuffle(tournament.players)

        # Trier les joueurs par points totaux (du plus haut au plus bas)
        players = sorted(tournament.players, key=lambda p: p.points, reverse=True)
        round_name = f"Round {tournament.current_round + 1}"
        print(f"\nCréation de {round_name}.")

        new_round = Round(name=round_name, round_number=tournament.current_round + 1)
        paired_players = set()

        # Générer les paires de joueurs
        while players:
            player_1 = players.pop(0)  # Premier joueur de la liste
            for i, player_2 in enumerate(players):
                if (player_1.chess_id, player_2.chess_id) not in tournament.played_matches:
                    match = Match(player_1, player_2)
                    new_round.matches.append(match)

                    # Ajouter cette paire aux matchs joués
                    tournament.played_matches.add((player_1.chess_id, player_2.chess_id))
                    tournament.played_matches.add((player_2.chess_id, player_1.chess_id))

                    # Retirer player_2 de la liste et marquer les deux joueurs comme appariés
                    players.pop(i)
                    paired_players.add(player_1.chess_id)
                    paired_players.add(player_2.chess_id)
                    print(f"Match ajouté : {player_1.first_name} {player_1.last_name} vs {player_2.first_name} {player_2.last_name}")
                    break
            else:
                # Si aucun adversaire n'est trouvé, on sort de la boucle
                print(f"Impossible d'apparier {player_1.first_name} {player_1.last_name}.")
                break

        # Ajouter le round au tournoi et passer au prochain round
        tournament.add_round(new_round)
        tournament.current_round += 1
        return new_round



    def list_rounds(self):
        """Liste les rounds créés jusqu'à présent."""
        if not self.rounds:
            print("No rounds have been created yet.")
        else:
            print("Rounds:")
            for round_ in self.rounds:
                print(f"{round_.round_number}. {round_.name}")

    def add_match_to_round(self, round_number, match):
        """Ajouter un match à un round existant."""
        for round_ in self.rounds:
            if round_.round_number == round_number:
                round_.matches.append(match)
                print(f"Match added to round {round_.name}.")
                return round_
        print(f"Round {round_number} not found.")
        return None

    
    def enter_match_results(self, tournament, round_number):
        round_ = next((r for r in tournament.rounds if r.round_number == round_number), None)
        if not round_:
            print(f"Round {round_number} introuvable.")
            return

        for match in round_.matches:
            print(f"{match.player_1.first_name} vs {match.player_2.first_name}")
            result = input("Résultat (1: P1 gagne, 2: P2 gagne, 3: nul) : ")
            if result == "1":
                match.score_1, match.score_2 = 1.0, 0.0
            elif result == "2":
                match.score_1, match.score_2 = 0.0, 1.0
            elif result == "3":
                match.score_1, match.score_2 = 0.5, 0.5