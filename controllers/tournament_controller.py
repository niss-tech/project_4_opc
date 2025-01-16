import json
from models.tournament import Tournament
from models.round import Round
from models.match import Match

class TournamentController:
    def __init__(self, tournament_file="data/tournaments.json"):
        self.tournament_file = tournament_file
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        """Charge les tournois depuis un fichier JSON."""
        try:
            with open(self.tournament_file, "r") as file:
                data = json.load(file)
                return [Tournament.from_dict(tournament) for tournament in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tournaments(self):
        """Sauvegarde les tournois dans un fichier JSON."""
        with open(self.tournament_file, "w") as file:
            json.dump([tournament.to_dict() for tournament in self.tournaments], file, indent=4)

    def create_tournament(self, name, location, start_date, end_date, description=""):
        """Crée un nouveau tournoi et sauvegarde."""
        tournament = Tournament(name, location, start_date, end_date, description)
        self.tournaments.append(tournament)
        self.save_tournaments()
        return tournament

    def add_player_to_tournament(self, tournament, player):
        """Ajoute un joueur à un tournoi."""
        if player not in tournament.players:
            tournament.add_player(player)
            self.save_tournaments()  # Sauvegarde dans le fichier JSON
        else:
            print("Ce joueur est déjà inscrit au tournoi.")

    def generate_round(self, tournament):
        """Génère un round pour un tournoi et l'associe avec des matchs."""
        if tournament.current_round >= tournament.num_rounds:
            print("Le tournoi est terminé.")
            return None  # Le tournoi est terminé.

        # Tri des joueurs par score et génération des paires
        players = sorted(tournament.players, key=lambda p: -p.points)  # Tri des joueurs selon leur score
        matches = []
        
        # Création des matchs pour le round
        while players:
            player1 = players.pop(0)
            player2 = players.pop(0) if players else None
            if player2:
                match = Match(player1, player2, score_1=0.0, score_2=0.0)
                matches.append(match)

        round_name = f"Round {tournament.current_round + 1}"
        
        # Créer un round avec round_number
        new_round = Round(name=round_name, round_number=tournament.current_round + 1)
        
        # Associer les matchs au round
        new_round.matches = matches  # Associe directement les matchs ici
        
        # Ajouter le round au tournoi
        tournament.add_round(new_round)

        # Demander les résultats des matchs
        for match in matches:
            print(f"Match : {match.player_1.first_name} {match.player_1.last_name} vs {match.player_2.first_name} {match.player_2.last_name}")
            print("Choisissez le résultat du match :")
            print("1 - Player 1 gagne")
            print("2 - Player 2 gagne")
            print("3 - Match nul")
            
            result = input("Entrez votre choix (1/2/3): ")
            
            if result == "1":
                match.score_1 = 1.0  # Player 1 gagne
                match.score_2 = 0.0  # Player 2 perd
            elif result == "2":
                match.score_1 = 0.0  # Player 1 perd
                match.score_2 = 1.0  # Player 2 gagne
            elif result == "3":
                match.score_1 = 0.5  # Match nul
                match.score_2 = 0.5  # Match nul
            else:
                print("Choix invalide, score non attribué.")
                continue  # Demander à nouveau si le choix est invalide

        # Sauvegarder les changements
        self.save_tournaments()
        
        print(f"Le {round_name} a été généré avec {len(matches)} matchs.")
        return new_round
