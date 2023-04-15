import pymysql

# Configuration pour la connexion à la base de données
db_config = {
    "host": "192.xxx.x.xxx",
    "user": "user name",
    "password": "mot de passe",
    "db": "nom de la base",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}
