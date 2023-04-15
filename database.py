import pymysql
from config import db_config

# Connexion à la base de données
def connect_to_db():
    try:
        connection = pymysql.connect(**db_config)
        print("Connexion à la base de données MariaDB réussie.")
    except Exception as e:
        print(f"Erreur de connexion à la base de données MariaDB : {e}")
        connection = None
    return connection

# Création de la table dans la base de données
def create_table(connection):
    if not connection:
        print("Aucune connexion à la base de données pour créer la table.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS emails (
                id INT NOT NULL AUTO_INCREMENT,
                nom VARCHAR(255) DEFAULT '',
                mail VARCHAR(255) NOT NULL,
                url VARCHAR(255) NOT NULL,
                PRIMARY KEY (id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
            connection.commit()
            print("Table 'emails' créée avec succès dans la base de données 'scrape'.")
    except Exception as e:
        print(f"Erreur de création de la table 'emails' : {e}")

# Stockage des e-mails dans la base de données
def store_emails(connection, titre, mails, url):
    if not connection:
        print("Aucune connexion à la base de données pour stocker les e-mails.")
        return

    if not titre and not mails and not url:
        print("Aucune information à stocker dans la base de données.")
        return

    mails_to_store = mails if mails else [""]
    for mail in mails_to_store:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO emails (nom, mail, url) VALUES (%s, %s, %s)"
                cursor.execute(sql, (titre, mail, url))
                connection.commit()
            print(f"Adresse e-mail enregistrée : {mail}")
        except Exception as e:
            print(f"Erreur d'enregistrement de l'adresse e-mail : {e}")

# Affichage des données stockées dans la base de données
def display_data(connection, url):
    if not connection:
        print("Aucune connexion à la base de données pour afficher les données.")
        return

    if not url:
        print("Aucune URL fournie pour récupérer les données de la base de données.")
        return

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM emails WHERE url=%s"
            cursor.execute(sql, (url,))
            results = cursor.fetchall()
            if results:
                print("Informations ajoutées à la base de données :")
                for result in results:
                    print(result['nom'], result['mail'], result['url'])
            else:
                print(f"Aucune information trouvée dans la base de données pour l'URL : {url}")
    except Exception as e:
        print(f"Erreur de récupération des informations depuis la base de données : {e}")

# Fermeture de la connexion à la base de données
def close_db_connection(connection):
    if connection:
        try:
            connection.close()
            print("Fermeture de la connexion à la base de données MariaDB réussie.")
        except Exception as e:
            print(f"Erreur de fermeture de la connexion à la base de données MariaDB : {e}")
