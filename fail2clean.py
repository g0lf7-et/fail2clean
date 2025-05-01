import os
import shutil
import time
import psutil

PASSWORD = "d4rknet-access"
TARGET_DIR = "sensitive_data"

def wipe_data(path):
    if os.path.exists(path):
        print("[!] Protocole de suppression activé...")
        shutil.rmtree(path)
        time.sleep(1)
        print("[✓] Données effacées.")
        time.sleep(1)
        print("Échec et mat.")
    else:
        print("[i] Aucune donnée à effacer.")

def monitor_external_devices():
    print("[i] Vérification des périphériques externes...")
    mounted_devices = [part.device for part in psutil.disk_partitions()]
    
    for device in mounted_devices:
        if "/media" in device or "/run/media" in device or "/Volumes" in device:
            print(f"[!] Périphérique externe détecté : {device}")
            trigger_full_wipe()
            break

def trigger_full_wipe():
    print("!!! ALERTE INTRUSION - PROTOCOLE FINAL ACTIVÉ !!!")
    time.sleep(1)
    print("[X] Suppression complète en cours...")
    wipe_data(TARGET_DIR)

def main():
    print("=== Accès sécurisé ===")
    pwd = input("Entrez le mot de passe : ")

    if pwd == PASSWORD:
        print("Accès autorisé.")
    else:
        print("Mot de passe incorrect.")
        time.sleep(1)
        wipe_data(TARGET_DIR)

    monitor_external_devices()

if __name__ == "__main__":
    main()
