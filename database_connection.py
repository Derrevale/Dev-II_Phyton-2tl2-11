import mysql.connector

from phase_1_position_bateau import afficher_tableau

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="tableau_des_scores"
)
cursor = connection.cursor()


def envoi_score(joueur1: object, joueur2: object):
    mon_insertion = connection.cursor()
    mon_insertion.execute(
        "INSERT INTO score_joueur (Score_Partie,Pseudo_joueur) VALUES (%s,%s)",
        (joueur1.score, joueur1.nom_joueur))
    mon_insertion.execute(
        "INSERT INTO score_joueur (Score_Partie,Pseudo_joueur) VALUES (%s,%s)",
        (joueur2.score, joueur2.nom_joueur))
    connection.commit()


def afficher_score(joueur1: object, joueur2: object):
    compteur = 0
    cursor.execute("SELECT Score_Partie,Pseudo_joueur from score_joueur order by Score_Partie DESC")
    tableau_score = cursor.fetchall()
    for elements in tableau_score:
        compteur = compteur + 1
        if compteur <= 5:
            print(compteur, ":", elements[1], " score: ", elements[0])
    print("Le score du joueur:", joueur1.nom_joueur, " est de :", joueur1.score)
    print("Le score du joueur:", joueur2.nom_joueur, " est de :", joueur2.score)
