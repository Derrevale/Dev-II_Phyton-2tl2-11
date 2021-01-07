import mysql.connector

# Connection à la database tableau_des_scores
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="tableau_des_scores"
)
cursor = connection.cursor()



def envoi_score(joueur1: object, joueur2: object):
    """Methode d'envois du score des joueurs vers Database

    PRE :
        - joueur1 = objet de classe JOUEUR
        - joueur2 = objet de classe JOUEUR
    POST :
        - mon_insertion = connection DB
        - mon_insertion.execute = "INSERT INTO score_joueur (Score_Partie,Pseudo_joueur) VALUES (%s,%s)
        - connection.commit
    """
    mon_insertion = connection.cursor()
    mon_insertion.execute(
        "INSERT INTO score_joueur (Score_Partie,Pseudo_joueur) VALUES (%s,%s)",
        (joueur1.score, joueur1.nom_joueur))
    mon_insertion.execute(
        "INSERT INTO score_joueur (Score_Partie,Pseudo_joueur) VALUES (%s,%s)",
        (joueur2.score, joueur2.nom_joueur))
    connection.commit()


def afficher_score(joueur1: object, joueur2: object):
    """Methode qui récupère les scores dans la DB ,trie les scores et les affiches

    PRE :
        - joueur1 = objet de classe Joueur
        - joueur2 = objet de classe Joueur
    POST :
        - cursor.execute("SELECT Score_Partie,Pseudo_joueur from score_joueur order by Score_Partie DESC")
        - tableau_score = cursor.fetchall
        - score_total = lambda x+y
        - boucle chaque elements dans tableau_score
        - print(compteur, ":", elements[1], " score: ", elements[0]) si compteur <=5
        - print("Le score du joueur:", joueur1.nom_joueur, " est de :", joueur1.score)
        - print("Le score du joueur:", joueur2.nom_joueur, " est de :", joueur2.score)
        - print("le score total pour la partie est de", score_total(joueur1.score, joueur2.score))
    """
    compteur = 0
    cursor.execute("SELECT Score_Partie,Pseudo_joueur from score_joueur order by Score_Partie DESC")
    tableau_score = cursor.fetchall()
    score_total = lambda x, y: x + y

    for elements in tableau_score:
        compteur = compteur + 1
        if compteur <= 5:
            print(compteur, ":", elements[1], " score: ", elements[0])
    print("Le score du joueur:", joueur1.nom_joueur, " est de :", joueur1.score)
    print("Le score du joueur:", joueur2.nom_joueur, " est de :", joueur2.score)
    print("le score total pour la partie est de", score_total(joueur1.score, joueur2.score))
