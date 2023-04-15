from database import connect_to_db, create_table, store_emails, display_data, close_db_connection
from scraper import fetch_html, extract_emails

# Fonction principale
def main():
    url = "https://url_du_site/"

    connection = connect_to_db()
    create_table(connection)

    html_content = fetch_html(url)
    if html_content:
        titre, mails = extract_emails(html_content)
        store_emails(connection, titre, mails, url)
        display_data(connection, url)

    close_db_connection(connection)

if __name__ == "__main__":
    main()
