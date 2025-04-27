import os
import shutil
import time

# Mot de passe attendu
PASSWORD = "d4rknet-access"

# Dossier à "nettoyer"
TARGET_DIR = "sensitive_data"

# Fonction de suppression
def wipe_data(path):
    if os.path.exists(path):
        print("[!] Protocole de suppression activé...")
        shutil.rmtree(path)
        print("[✓] Données effacées avec succès.")
    else:
        print("[i] Aucun dossier sensible détecté.")

def main():
    print("=== Accès sécurisé ===")
    pwd = input("Entrez le mot de passe : ")

    if pwd == PASSWORD:
        print("Accès autorisé.")
    else:
        print("Mot de passe incorrect.")
        time.sleep(1)
        wipe_data(TARGET_DIR)

if __name__ == "__main__":
    main()
