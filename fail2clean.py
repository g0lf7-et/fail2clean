import os
import shutil
import time
import psutil

PASSWORD = "d4rknet-access"
TARGET_DIR = "sensitive_data"

# Fonction pour effacer les données sensibles si un accès non autorisé est détecté
def wipe_data(path):
    if os.path.exists(path):
        print("[!] Protocole de suppression activé...")
        shutil.rmtree(path)  # Suppression du dossier contenant les données sensibles
        print("[✓] Données effacées.")
    else:
        print("[i] Aucune donnée à effacer.")

# Fonction pour détecter un périphérique externe connecté
def monitor_external_devices():
    print("[i] Vérification des périphériques externes...")
    mounted_devices = [part.device for part in psutil.disk_partitions()]
    
    for device in mounted_devices:
        # Si un périphérique externe est monté, on lance l'effacement complet
        if "/media" in device or "/run/media" in device or "/Volumes" in device:
            print(f"[!] Périphérique externe détecté : {device}")
            trigger_full_wipe()
            break

# Fonction pour lancer le processus d'effacement complet
def trigger_full_wipe():
    print("!!! ALERTE INTRUSION - PROTOCOLE FINAL ACTIVÉ !!!")
    time.sleep(1)  # Petite pause pour simuler le temps de réaction
    print("[X] Suppression complète en cours...")
    print("[✓] Toutes les données sensibles sont effacées.")

def main():
    print("=== Accès sécurisé ===")
    pwd = input("Entrez le mot de passe : ")

    # Vérification du mot de passe
    if pwd == PASSWORD:
        print("Accès autorisé.")
    else:
        print("Mot de passe incorrect.")
        time.sleep(1)
        wipe_data(TARGET_DIR)  # Effacer les données si le mot de passe est incorrect

    # Vérification des périphériques externes connectés
    monitor_external_devices()

if __name__ == "__main__":
    main()
