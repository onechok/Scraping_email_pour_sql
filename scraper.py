import requests
import re
from bs4 import BeautifulSoup

# Récupération du contenu HTML
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content
        print("Récupération du contenu HTML réussie.")
    except Exception as e:
        print("Erreur de récupération du contenu HTML :", e)
        html_content = None
    return html_content

# Extraction des e-mails du contenu HTML
def extract_emails(html_content):
    if not html_content:
        print("Aucun contenu HTML fourni pour extraire les e-mails.")
        return None, set()

    soup = BeautifulSoup(html_content, 'html.parser')
    titre = soup.title.string
    if not titre:
        print("Impossible d'extraire le titre du site.")
    mails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.get_text()))

    if not mails:
        print("Aucune adresse e-mail trouvée dans le contenu HTML.")

    return titre, mails
