from models.player import Player
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu import Menu
from views.report import Report


def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    while True:
        choice = Menu.main_menu()
        if choice == "1":  # Gestion des joueurs
            while True:
                player_choice = Menu.player_menu()
                if player_choice == "1":  # Ajouter un joueur
                    first_name = input("Prénom : ")
                    last_name = input("Nom : ")
                    birth_date = input("Date de naissance (AAAA-MM-JJ) : ")
                    chess_id = input("Identifiant national d'échecs : ")
                    player_controller.add_player(first_name, last_name, birth_date, chess_id)
                    print("Joueur ajouté avec succès.")
                elif player_choice == "2":  # Liste des joueurs
                    players = player_controller.get_players_sorted()
                    for player in players:
                        print(f"{player.last_name}, {player.first_name} ({player.chess_id})")
                elif player_choice == "3":  # Retour
                    break

        elif choice == "2":  # Gestion des tournois
            while True:
                    tournament_choice = Menu.tournament_menu()
                    if tournament_choice == "1":  # Créer un tournoi
                        name = input("Nom du tournoi : ")
                        location = input("Lieu : ")
                        start_date = input("Date de début (AAAA-MM-JJ) : ")
                        end_date = input("Date de fin (AAAA-MM-JJ) : ")
                        description = input("Description : ")
                        tournament_controller.create_tournament(name, location, start_date, end_date, description)
                        print("Tournoi créé avec succès.")

                    elif tournament_choice == "2":  # Ajouter un joueur à un tournoi
                        tournament_name = input("Nom du tournoi : ")
                        tournament = next((t for t in tournament_controller.tournaments if t.name == tournament_name), None)
                        if tournament:
                            first_name = input("Prénom du joueur : ")
                            last_name = input("Nom du joueur : ")
                            birth_date = input("Date de naissance (AAAA-MM-JJ) : ")
                            chess_id = input("Identifiant national d'échecs : ")
                            player = Player(first_name, last_name, birth_date, chess_id)
                            tournament.add_player(player)
                            print(f"Le joueur {first_name} {last_name} a été ajouté au tournoi {tournament_name}.")
                        else:
                            print("Tournoi introuvable.")

                    elif tournament_choice == "4":  # Retour
                        break


        elif choice == "3":  # Afficher les rapports
            while True:
                print("\n=== Rapports ===")
                print("1. Liste de tous les joueurs (ordre alphabétique)")
                print("2. Liste de tous les tournois")
                print("3. Détails d'un tournoi")
                print("4. Retour au menu principal")
                report_choice = input("Choisissez une option : ")

                if report_choice == "1":  # Liste des joueurs
                    players = player_controller.get_players_sorted()
                    Report.display_players(players)

                elif report_choice == "2":  # Liste des tournois
                    tournaments = tournament_controller.tournaments
                    Report.display_tournaments(tournaments)

                elif report_choice == "3":  # Détails d'un tournoi
                    name = input("Entrez le nom du tournoi : ")
                    tournament = next((t for t in tournament_controller.tournaments if t.name == name), None)
                    if tournament:
                        Report.display_tournament_details(tournament)
                        Report.display_rounds(tournament)
                    else:
                        print("Tournoi introuvable.")

                elif report_choice == "4":  # Retour
                    break

        elif choice == "4":  # Quitter
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
