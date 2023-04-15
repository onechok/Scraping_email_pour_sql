# Projet de scraping d'e-mails

Ce projet vise à extraire les e-mails à partir d'une URL donnée et à les stocker dans une base de données MariaDB. Le projet est divisé en plusieurs fichiers pour faciliter la lecture et la modification du code.

## Fichiers et structure du projet

- `main.py` : Le point d'entrée du projet, contient le code principal pour exécuter le script.
- `config.py` : Contient les paramètres de configuration pour la connexion à la base de données MariaDB.
- `database.py` : Contient les fonctions liées à la gestion de la base de données, comme la connexion, la création de la table, l'insertion des données et la récupération des données.
- `html_processing.py` : Contient les fonctions pour récupérer le contenu HTML d'une URL et extraire les e-mails à partir du contenu HTML.
- `requirements.txt` : Liste des dépendances Python nécessaires pour exécuter le projet.

## Dépendances du projet

Les dépendances du projet sont les suivantes :

- Python 3.7 ou ultérieur
- pymysql
- beautifulsoup4

Vous pouvez installer ces dépendances en utilisant le fichier `requirements.txt` :

## Comment exécuter le projet

1. Clonez le dépôt et naviguez vers le répertoire du projet.
2. Installez les dépendances en utilisant `pip install -r requirements.txt`.
3. Assurez-vous que les informations de connexion à la base de données dans `config.py` sont correctes.
4. Exécutez `main.py` pour lancer le script.

## Dépannage courant

Si vous rencontrez des problèmes lors de l'exécution du projet, voici quelques solutions possibles :

1. Vérifiez que toutes les dépendances sont correctement installées.
2. Assurez-vous que les informations de connexion à la base de données dans `config.py` sont correctes.
3. Si vous rencontrez des problèmes avec l'encodage des caractères, vérifiez que la base de données utilise l'encodage UTF-8.

Si vous avez besoin d'aide supplémentaire, n'hésitez pas à ouvrir une issue sur la plateforme de gestion du projet (GitHub, GitLab, etc.) ou à demander de l'aide sur les forums appropriés.

## Contribution au projet

Les contributions au projet sont les bienvenues ! Si vous souhaitez ajouter de nouvelles fonctionnalités, résoudre des problèmes ou améliorer la documentation, veuillez suivre ces étapes :

1. Forkez le dépôt et créez une nouvelle branche pour vos modifications.
2. Assurez-vous de suivre les directives de style de code et de documenter clairement toutes les modifications.
3. Testez votre code avant de soumettre une pull request.
4. Décrivez clairement les changements effectués dans la description de la pull request et les problèmes résolus, le cas échéant.

## Licence et crédits

Ce projet est distribué sous la licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer en respectant les termes de cette licence.

Nous tenons à remercier les développeer des bibliothèques utilisées dans ce projet, ainsi que toutes les personnes qui ont contribué à son élaboration et à son amélioration.

## Explication des fonctions du code

Chaque fichier du projet contient les fonctions suivantes :

- `main.py` :
  - `main()` : Fonction principale qui orchestre l'ensemble du processus de scraping et de stockage des e-mails.

- `config.py` :
  - `db_config` : Dictionnaire contenant les paramètres de configuration pour la connexion à la base de données MariaDB.

- `database.py` :
  - `connect_to_db()` : Établit la connexion à la base de données MariaDB et retourne l'objet de connexion.
  - `create_table(connection)` : Crée la table `emails` dans la base de données si elle n'existe pas.
  - `store_emails(connection, titre, mails, url)` : Enregistre les e-mails, le titre et l'URL dans la table `emails`.
  - `display_data(connection, url)` : Affiche les données stockées dans la base de données pour une URL donnée.
  - `close_db_connection(connection)` : Ferme la connexion à la base de données MariaDB.

- `html_processing.py` :
  - `fetch_html(url)` : Récupère le contenu HTML de l'URL spécifiée.
  - `extract_emails(html_content)` : Extrait les adresses e-mail du contenu HTML et retourne le titre du site et les e-mails trouvés.

Ces fonctions peuvent être modifiées ou étendues pour adapter le projet à vos besoins spécifiques. Le fichier README.md sert de guide pour comprendre le projet et faciliter les modifications ultérieures.

