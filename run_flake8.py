import subprocess
import os


def run_flake8():
    # Créer le répertoire pour le rapport s'il n'existe pas
    report_dir = "flake8_rapport"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Lancer flake8 avec l'option --format=html pour générer un rapport HTML
    result = subprocess.run(
        ['flake8', '--max-line-length=119', '--format=html', '--htmldir=flake8_rapport'],
        capture_output=True, text=True
    )

    # Afficher toute la sortie de flake8 dans la console
    print("Sortie complète de flake8 :")
    print(result.stdout)  # Affiche toute la sortie dans la console

    # Vérifier si des erreurs ont été détectées
    if result.returncode == 0:
        print("✅ Le code ne contient aucune erreur après l'analyse.")
    else:
        print("⚠️ Le code contient des erreurs.")

    # Nettoyer le répertoire et renommer le rapport
    clean_flake8_report(report_dir)


def clean_flake8_report(directory="flake8_rapport"):
    index_path = os.path.join(directory, "index.html")
    rapport_path = os.path.join(directory, "rapport.html")

    # Vérifier si le fichier rapport.html existe déjà et le supprimer si nécessaire
    if os.path.exists(rapport_path):
        os.remove(rapport_path)

    # Vérifier si index.html existe dans le répertoire
    if os.path.exists(index_path):
        os.rename(index_path, rapport_path)
        print("✅ Rapport généré : flake8_rapport/rapport.html")
    else:
        print("⚠️ Aucun fichier index.html trouvé. Vérifiez l'exécution de flake8.")


if __name__ == "__main__":
    run_flake8()
