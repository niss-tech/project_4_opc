from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from controllers.match_controller import MatchController


def main_menu():
    """Affiche le menu principal et gère les interactions."""
    print("\n=== Chess Tournament Manager ===")
    print("1. Gérer les tournois")
    print("2. Gérer les joueurs")
    print("3. Gérer les rounds")
    print("4. Gérer les matchs")
    print("5. Quitter")


def tournament_menu():
    """Affiche le menu des tournois."""
    print("\n=== Menu des Tournois ===")
    print("1. Créer un tournoi")
    print("2. Ajouter un joueur à un tournoi")
    print("3. Ajouter un round à un tournoi")
    print("4. Lister les tournois")
    print("5. Afficher les détails d'un tournoi")
    print("6. Retour au menu principal")


def player_menu():
    """Affiche le menu des joueurs."""
    print("\n=== Menu des Joueurs ===")
    print("1. Créer un joueur")
    print("2. Lister les joueurs")
    print("3. Mettre à jour un joueur")
    print("4. Retour au menu principal")


if __name__ == "__main__":
    # Initialiser les contrôleurs
    tournament_controller = TournamentController()
    player_controller = PlayerController()
    round_controller = RoundController()
    match_controller = MatchController()

    while True:
        main_menu()
        choice = input("\nChoisissez une option : ")

        # Menu des tournois
        if choice == "1":
            while True:
                tournament_menu()
                t_choice = input("\nChoisissez une option (tournois) : ")

                if t_choice == "1":
                    name = input("Nom du tournoi : ")
                    location = input("Lieu du tournoi : ")
                    start_date = input("Date de début (YYYY-MM-DD) : ")
                    end_date = input("Date de fin (YYYY-MM-DD) : ")
                    description = input("Description : ")
                    tournament_controller.create_tournament(name, location, start_date, end_date, description)

                elif t_choice == "2":
                    tournament_name = input("Nom du tournoi : ")
                    chess_id = input("ID du joueur à ajouter : ")
                    player = player_controller.find_player_by_id(chess_id)
                    if player:
                        tournament_controller.add_player_to_tournament(tournament_name, player)
                    else:
                        print("Joueur introuvable.")

                elif t_choice == "3":
                    tournament_name = input("Nom du tournoi : ")
                    round_name = input("Nom du round : ")
                    round_number = input("Numéro du round : ")
                    new_round = round_controller.create_round(round_name, int(round_number))
                    tournament_controller.add_round_to_tournament(tournament_name, new_round)

                elif t_choice == "4":
                    tournament_controller.list_tournaments()

                elif t_choice == "5":
                    tournament_name = input("Nom du tournoi : ")
                    tournament_controller.display_tournament_details(tournament_name)

                elif t_choice == "6":
                    break

                else:
                    print("Option invalide.")

        # Menu des joueurs
        elif choice == "2":
            while True:
                player_menu()
                p_choice = input("\nChoisissez une option (joueurs) : ")

                if p_choice == "1":
                    first_name = input("Prénom : ")
                    last_name = input("Nom : ")
                    birth_date = input("Date de naissance (YYYY-MM-DD) : ")
                    chess_id = input("ID d'échecs : ")
                    player_controller.create_player(first_name, last_name, birth_date, chess_id)

                elif p_choice == "2":
                    player_controller.list_players()

                elif p_choice == "3":
                    chess_id = input("ID du joueur à mettre à jour : ")
                    first_name = input("Nouveau prénom (laisser vide pour ne pas changer) : ")
                    last_name = input("Nouveau nom (laisser vide pour ne pas changer) : ")
                    birth_date = input("Nouvelle date de naissance (laisser vide pour ne pas changer) : ")
                    player_controller.update_player(chess_id, first_name, last_name, birth_date)

                elif p_choice == "4":
                    break

                else:
                    print("Option invalide.")

        # Quitter
        elif choice == "5":
            print("Au revoir !")
            break

        else:
            print("Option invalide.")
