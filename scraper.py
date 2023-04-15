import requests
import re
from bs4 import BeautifulSoup
import lxml.html

# Récupération du contenu HTML
def fetch_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.content
        print("Récupération du contenu HTML réussie.")
    except Exception as e:
        print("Erreur de récupération du contenu HTML :", e)
        html_content = None
    return html_content

# Extraction des e-mails du contenu HTML
def extract_emails(html_content, ignore_case=True):
    if not html_content:
        print("Aucun contenu HTML fourni pour extraire les e-mails.")
        return None, set()

    soup = BeautifulSoup(html_content, 'html.parser')
    titre = soup.title.string.strip() if soup.title else None
    if not titre:
        print("Impossible d'extraire le titre du site.")

    regex_flags = re.IGNORECASE if ignore_case else 0
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    mails = set(re.findall(email_pattern, soup.get_text(), regex_flags))

    for tag in soup.find_all(True):
        for attr in ['href', 'src', 'data']:
            if tag.has_attr(attr):
                attribute_value = tag[attr]
                if isinstance(attribute_value, str):
                    mails.update(re.findall(email_pattern, attribute_value, regex_flags))

    if not mails:
        print("Aucune adresse e-mail trouvée dans le contenu HTML avec BeautifulSoup. Tentative avec lxml.")
        root = lxml.html.fromstring(html_content)
        mails = set(re.findall(email_pattern, root.text_content(), regex_flags))

        for element in root.iter():
            for attr in ['href', 'src', 'data']:
                attribute_value = element.get(attr)
                if attribute_value:
                    mails.update(re.findall(email_pattern, attribute_value, regex_flags))

        if not mails:
            print("Aucune adresse e-mail trouvée dans le contenu HTML avec lxml.")

    return titre, mails
