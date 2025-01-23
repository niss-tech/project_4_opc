from models.player import Player 
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController 
from views.report import Report
from views.menu import Menu
from controllers.round_controller import RoundController 

def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()
    round_controller = RoundController()

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
                    print(players)  # Vérifie si la liste est vide
                    Report.display_players(players)
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
                        print(f"\nAjout d'un joueur au tournoi '{tournament_name}'.")

                        # Affiche les joueurs déjà inscrits
                        print("\nJoueurs déjà inscrits dans ce tournoi :")
                        for player in tournament.players:
                            print(f"- {player.first_name} {player.last_name} ({player.chess_id})")
                        
                        # Demande uniquement le chess_id pour ajouter un joueur existant
                        chess_id = input("Identifiant national d'échecs du joueur à ajouter : ")
                        player = next((p for p in player_controller.players if p.chess_id == chess_id), None)
                        
                        if player:
                            # Vérifie si le joueur est déjà dans le tournoi
                            if player in tournament.players:
                                print(f"Le joueur {player.first_name} {player.last_name} ({chess_id}) est déjà inscrit dans ce tournoi.")
                            else:
                                # Ajout du joueur au tournoi
                                tournament_controller.add_player_to_tournament(tournament, player)
                                tournament_controller.save_tournaments()
                                print(f"Le joueur {player.first_name} {player.last_name} a été ajouté au tournoi '{tournament_name}'.")
                        else:
                            print(f"Aucun joueur avec l'identifiant {chess_id} n'a été trouvé dans la base de données.")
                    else:
                        print(f"Tournoi '{tournament_name}' introuvable. Vérifiez le nom et réessayez.")

                elif tournament_choice == "3":  # Générer un round
                    tournament_name = input("Nom du tournoi : ")
                    tournament = next((t for t in tournament_controller.tournaments if t.name == tournament_name), None)
                    if tournament:
                        print(f"Création d'un nouveau round pour le tournoi '{tournament.name}'.")
                        tournament_controller.generate_round(tournament, round_controller)

                    else:
                        print("Tournoi introuvable.")

                elif tournament_choice == "4":  # Saisir les résultats des matchs
                    tournament_name = input("Nom du tournoi : ")
                    tournament = next((t for t in tournament_controller.tournaments if t.name == tournament_name), None)
                    if tournament:
                        round_number = int(input("Numéro du round auquel saisir les résultats des matchs : "))
                        round_instance = next((r for r in tournament.rounds if r.round_number == round_number), None)
                        
                        if round_instance and round_instance.matches:
                            print(f"\n=== Résultats des matchs pour le Round {round_number} ===")
                            
                            # Afficher les matchs existants
                            for idx, match in enumerate(round_instance.matches, start=1):
                                print(f"{idx}. {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name} (Scores : {match.score_1} - {match.score_2})")
                            
                            while True:
                                try:
                                    match_index = int(input("\nSélectionnez le numéro du match pour saisir le résultat : ")) - 1
                                    if match_index < 0 or match_index >= len(round_instance.matches):
                                        print("Numéro de match invalide. Veuillez réessayer.")
                                        continue
                                    
                                    match = round_instance.matches[match_index]
                                    print(f"Match sélectionné : {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name}")
                                    
                                    # Saisie des scores
                                    result = input(f"Entrez le résultat (1 - {match.player_1.first_name} gagne, 2 - {match.player_2.first_name} gagne, 3 - Match nul) : ")
                                    
                                    if result == "1":
                                        match.score_1 = 1.0
                                        match.score_2 = 0.0
                                    elif result == "2":
                                        match.score_1 = 0.0
                                        match.score_2 = 1.0
                                    elif result == "3":
                                        match.score_1 = 0.5
                                        match.score_2 = 0.5
                                    else:
                                        print("Résultat invalide. Veuillez réessayer.")
                                        continue
                                    
                                    print(f"Résultat enregistré : {match.player_1.first_name} {match.score_1} - {match.score_2} {match.player_2.first_name}")
                                    
                                    # Sauvegarder les modifications
                                    tournament_controller.save_tournaments()
                                    
                                    another = input("Saisir un autre résultat ? (o/n) : ")
                                    if another.lower() != "o":
                                        break
                                except ValueError:
                                    print("Veuillez entrer un numéro valide.")
                        else:
                            print("Aucun match trouvé pour ce round.")
                    else:
                        print("Tournoi introuvable.")


                elif tournament_choice == "5":  # Retour
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

                elif report_choice == "4": 
                    break

        elif choice == "4":  # Quitter
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()