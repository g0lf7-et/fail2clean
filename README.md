fail2clean 🔒🔥

Script de sécurité défensive conçu pour réagir immédiatement à un accès non autorisé.  
Si un mot de passe incorrect est saisi... tout est supprimé.

---

## 🧨 Fonctionnement

1. L'utilisateur lance le programme
2. Il entre un mot de passe
3. Si le mot de passe est **incorrect**, un script efface tous les fichiers du dossier `sensitive_data`

**Détection de périphériques externes**  
   Le programme surveille les périphériques connectés à l'ordinateur (clés USB, disques durs externes, etc.). Si un périphérique externe est détecté, une procédure de nettoyage est immédiatement déclenchée pour effacer toutes les données sensibles présentes sur le système.
   
---


## 🧪 Exemple d'utilisation

```bash
python fail2clean.py
