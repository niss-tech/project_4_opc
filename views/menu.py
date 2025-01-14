class Menu:
    @staticmethod
    def main_menu():
        """Affiche le menu principal."""
        print("\n=== Menu Principal ===")
        print("1. Gérer les joueurs")
        print("2. Gérer les tournois")
        print("3. Afficher les rapports")
        print("4. Quitter")
        return input("Choisissez une option : ")

    @staticmethod
    def player_menu():
        """Affiche le menu des joueurs."""
        print("\n=== Gestion des Joueurs ===")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs (ordre alphabétique)")
        print("3. Retour au menu principal")
        return input("Choisissez une option : ")

    @staticmethod
    def tournament_menu():
        """Affiche le menu des tournois."""
        print("\n=== Gestion des Tournois ===")
        print("1. Créer un tournoi")
        print("2. Ajouter un joueur à un tournoi")
        print("3. Générer un round")
        print("4. Retour au menu principal")
        return input("Choisissez une option : ")
