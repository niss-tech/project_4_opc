from models.round import Round
from models.match import Match
import random


class RoundController:
    def __init__(self):
        self.rounds = []  # Stocker les rounds si nécessaire

    def create_round(self, tournament):
        """Créer un nouveau round de façon dynamique."""
        print(f"\n🔄 Tentative de création du Round {tournament.current_round + 1}...")

        if tournament.current_round >= tournament.num_rounds:
            print("🚫 Le tournoi est terminé.")
            return None

        if len(tournament.players) < 8:
            print("🚨 Il faut au moins 8 joueurs pour créer un round.")
            return None

        # Vérifier les scores du round précédent avant de générer un nouveau round
        if tournament.current_round > 0 and tournament.rounds:
            last_round = tournament.rounds[-1]  # Récupère le dernier round joué
            print(f"🔍 Vérification des scores du {last_round.name}...")

            for match in last_round.matches:
                if match.score_1 == 0.0 and match.score_2 == 0.0:  # Vérifie si les scores n'ont pas été modifiés
                    print(f"⚠️ Match non saisi détecté : {match.player_1.first_name} vs {match.player_2.first_name}")
                    print(f"⛔ Impossible de générer le Round {tournament.current_round + 1} tant que tous les scores ne sont pas saisis.")
                    return None  # Bloque immédiatement la génération du round

        # Mélanger les joueurs pour le premier round
        if tournament.current_round == 0:
            print("\n🎲 Mélange des joueurs pour le premier round...")
            random.shuffle(tournament.players)

        players = sorted(tournament.players, key=lambda p: p.points, reverse=True)
        round_name = f"Round {tournament.current_round + 1}"
        print(f"\n✅ Création de {round_name}.")

        new_round = Round(name=round_name, round_number=tournament.current_round + 1)

        while players:
            player_1 = players.pop(0)
            player_2 = self.find_opponent(player_1, players, tournament.played_matches)
            if player_2:
                match = Match(player_1, player_2)
                new_round.matches.append(match)
                tournament.played_matches.update({(player_1.chess_id, player_2.chess_id), (player_2.chess_id, player_1.chess_id)})
                print(f"✅ Match ajouté : {player_1.first_name} vs {player_2.first_name}")
            else:
                print(f"⚠️ Impossible d'apparier {player_1.first_name} {player_1.last_name}.")

        # Ajouter le round au tournoi et mettre à jour le current_round
        tournament.add_round(new_round)

        return new_round

    def list_rounds(self):
        """Liste les rounds créés jusqu'à présent."""
        if not self.rounds:
            print("No rounds have been created yet.")
        else:
            print("Rounds:")
            for round_ in self.rounds:
                print(f"{round_.round_number}. {round_.name}")

    def find_opponent(self, player_1, players, played_matches):
        """Trouve un adversaire pour un joueur en évitant les matchs déjà joués."""
        for i, player_2 in enumerate(players):
            if (player_1.chess_id, player_2.chess_id) not in played_matches:
                return players.pop(i)
        return None  # Aucun adversaire disponible

    def enter_match_results(self, tournament, round_number, tournament_controller):
        round_ = next((r for r in tournament.rounds if r.round_number == round_number), None)
        if not round_:
            print(f"Round {round_number} introuvable.")
            return

        while True:
            print(f"\n=== Matchs du Round {round_number} ===")
            for idx, match in enumerate(round_.matches, start=1):
                print(f"{idx}. {match.player_1.first_name} vs {match.player_2.first_name} (Scores : {match.score_1} - {match.score_2})")

            try:
                match_index = int(input("\nSélectionnez le numéro du match pour saisir/modifier le résultat : ")) - 1
                if not (0 <= match_index < len(round_.matches)):
                    print("Numéro de match invalide. Veuillez réessayer.")
                    continue

                match = round_.matches[match_index]
                print(f"Match sélectionné : {match.player_1.first_name} vs {match.player_2.first_name}")

                self.update_player_scores(match)  # Mise à jour des scores
                tournament_controller.save_tournaments()

                another = input("Voulez-vous saisir un autre score ? (o/n) : ")
                if another.lower() != "o":
                    break
            except ValueError:
                print("Veuillez entrer un numéro valide.")

    def update_player_scores(self, match):
        """Met à jour les points des joueurs après qu'un score a été enregistré ou modifié."""
        # Retirer les anciens scores avant d'assigner les nouveaux
        if match.score_1 is not None and match.score_2 is not None:
            match.player_1.points -= match.score_1
            match.player_2.points -= match.score_2

        # Demander le nouveau score à l'utilisateur
        result = input(f"Entrez le résultat (1 - {match.player_1.first_name} gagne, "f"2 - {match.player_2.first_name} gagne, 3 - Match nul) : ")

        # Mettre à jour les scores
        if result == "1":
            match.score_1, match.score_2 = 1.0, 0.0
        elif result == "2":
            match.score_1, match.score_2 = 0.0, 1.0
        elif result == "3":
            match.score_1, match.score_2 = 0.5, 0.5
        else:
            print("Résultat invalide. Veuillez réessayer.")
            return

        # Ajouter les nouveaux scores aux joueurs
        match.player_1.points += match.score_1
        match.player_2.points += match.score_2

        print(f"Points mis à jour : {match.player_1.first_name} ({match.player_1.points} points), "
            f"{match.player_2.first_name} ({match.player_2.points} points).")
