import subprocess

# Lancer les deux scripts en parallèle
process_serveur = subprocess.Popen(["python", "c:/Users/amouz/OneDrive/Bureau/SERVEUR.py"])
process_client = subprocess.Popen(["python", "c:/Users/amouz/OneDrive/Bureau/client.py"])

# Attendre la fin des processus (optionnel)
process_serveur.wait()
process_client.wait()
