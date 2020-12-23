import mysql.connector
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="tableau_des_scores"
)
cursor = connection.cursor()
