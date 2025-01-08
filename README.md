# Gestion Club Échec

## Description du Projet

**Gestion Club Échec** est une application permettant la gestion efficace d'un club d'échecs. Ce projet facilite l'organisation des tournois, le suivi des parties, la gestion des joueurs, et l'administration des différents rounds de tournoi.  

L'application offre une interface en ligne de commande simple pour permettre aux utilisateurs de :
- Créer, mettre à jour et consulter les informations des joueurs.
- Organiser et suivre les matchs, rounds, et tournois.
- Exporter ou importer les données sous forme sérialisée pour assurer la sauvegarde.

## Fonctionnalités Principales

1. **Gestion des Joueurs**  
   - Ajouter un joueur avec des informations telles que son prénom, nom, date de naissance, et ID d'échecs.  
   - Mettre à jour les informations des joueurs existants.  
   - Lister tous les joueurs inscrits au club.

2. **Gestion des Matchs**  
   - Créer un match entre deux joueurs en enregistrant les scores.  
   - Visualiser tous les matchs créés.  

3. **Gestion des Rounds**  
   - Créer des rounds composés de plusieurs matchs.  
   - Ajouter ou consulter les matchs d'un round existant.

4. **Gestion des Tournois**  
   - Créer et gérer des tournois incluant des joueurs, des rounds, et un nombre défini de rounds.  
   - Ajouter des joueurs ou rounds à un tournoi.  
   - Lister les détails d'un tournoi ou exporter ses données.

## Structure du Projet

Voici un aperçu des principaux dossiers et fichiers du projet :

```
gestion_club_echec/
├── controllers/
│   ├── match_controller.py
│   ├── player_controller.py
│   ├── round_controller.py
│   └── tournament_controller.py
├── models/
│   ├── __init__.py
│   ├── match.py
│   ├── player.py
│   ├── round.py
│   └── tournament.py
├── main.py
└── README.md
```

### Modules

- **`models`** : Contient les classes qui définissent les entités principales du projet (Player, Match, Round, Tournament).  
- **`controllers`** : Contient la logique métier pour gérer les entités et l'interaction avec l'utilisateur.  
- **`main.py`** : Point d'entrée du programme, permettant d'exécuter l'application via une interface en ligne de commande.

## Prérequis

Avant de commencer, assurez-vous que votre environnement répond aux exigences suivantes :

- Python 3.8 ou supérieur
- Une bonne compréhension des bases de Python (POO, modules, gestion des erreurs)

## Installation

1. Clonez le repository dans votre environnement local :
   ```bash
   git clone <URL_DU_REPOSITORY>
   cd gestion_club_echec
   ```

2. Assurez-vous d’avoir un environnement virtuel actif :
   ```bash
   python -m venv venv
   source venv/bin/activate      # Sur Linux/MacOS
   venv\Scripts\activate         # Sur Windows
   ```

3. Installez les dépendances (si applicables) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le programme en exécutant le fichier `main.py` :
   ```bash
   python main.py
   ```

2. Suivez les instructions dans la console pour interagir avec le programme.

## Exemples d'Utilisation

Voici quelques scénarios typiques pris en charge par le programme :

- **Ajouter un joueur** : Entrez ses informations (nom, prénom, ID).  
- **Créer un tournoi** : Spécifiez le lieu, le nom, et la durée, puis ajoutez des joueurs et des rounds.  
- **Lister les matchs ou rounds** : Affichez les données de manière détaillée dans la console.

## Auteurs

Ce projet a été développé par **Adamo Nisrine** dans le cadre d'un exercice visant à appliquer les concepts de programmation orientée objet et de sérialisation des données.

