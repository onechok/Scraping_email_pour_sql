import pymysql

# Configuration pour la connexion à la base de données
db_config = {
    "host": "192.168.1.150",
    "user": "one",
    "password": "2411",
    "db": "scrape",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}
