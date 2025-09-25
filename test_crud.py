import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def get_posts():
    """Legge tutti i post"""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        posts = response.json()
        print("\n📌 Elenco dei primi 5 post:")
        for post in posts[:5]:
            print(f"ID: {post['id']} | Titolo: {post['title']}")
    else:
        print("Errore nel recupero dei post.")


def get_post(post_id):
    """Legge un post specifico"""
    response = requests.get(f"{BASE_URL}/{post_id}")
    if response.status_code == 200:
        post = response.json()
        print(f"\n📌 Post {post_id}: {post}")
    else:
        print(f"Post con id {post_id} non trovato.")


def create_post():
    """Crea un nuovo post"""
    new_post = {
        "title": "Corso Python",
        "body": "Sto imparando a usare le API con requests!",
        "userId": 1,
    }
    response = requests.post(BASE_URL, json=new_post)
    print("\n✅ Post creato:")
    print(response.json())


def update_post(post_id):
    """Aggiorna un post con PUT"""
    update_data = {
        "id": post_id,
        "title": "Titolo aggiornato",
        "body": "Contenuto aggiornato",
        "userId": 1,
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=update_data)
    print("\n✏️ Post aggiornato:")
    print(response.json())


def patch_post(post_id):
    """Aggiorna solo un campo con PATCH"""
    patch_data = {"title": "Titolo aggiornato con PATCH"}
    response = requests.patch(f"{BASE_URL}/{post_id}", json=patch_data)
    print("\n🩹 Post parzialmente aggiornato:")
    print(response.json())


def delete_post(post_id):
    """Cancella un post"""
    response = requests.delete(f"{BASE_URL}/{post_id}")
    if response.status_code in [200, 204]:
        print(f"\n❌ Post {post_id} eliminato con successo.")
    else:
        print(f"Errore durante l'eliminazione del post {post_id}.")


def main():
    while True:
        print("\n--- MENU CRUD ---")
        print("1. Leggi tutti i post")
        print("2. Leggi un post specifico")
        print("3. Crea un nuovo post")
        print("4. Aggiorna un post (PUT)")
        print("5. Aggiorna un post (PATCH)")
        print("6. Elimina un post")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            get_posts()
        elif scelta == "2":
            post_id = input("Inserisci l'ID del post: ")
            get_post(post_id)
        elif scelta == "3":
            create_post()
        elif scelta == "4":
            post_id = input("ID del post da aggiornare: ")
            update_post(post_id)
        elif scelta == "5":
            post_id = input("ID del post da aggiornare (PATCH): ")
            patch_post(post_id)
        elif scelta == "6":
            post_id = input("ID del post da eliminare: ")
            delete_post(post_id)
        elif scelta == "0":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()
