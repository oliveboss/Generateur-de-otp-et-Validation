import time
import hmac
import hashlib
import tkinter as tk
from tkinter import ttk

# 🔹 Clé secrète partagée entre le client et le serveur
CLE_SECRETE = "KOFFITSE_ET_VICTOIRE"

def generer_otp():
    """
    Génère un OTP basé sur l'horodatage et la clé secrète.
    L'OTP change toutes les 60 secondes.
    """
    horodatage = int(time.time()) // 60  # Diviser le temps actuel par 60 pour un renouvellement toutes les minutes
    hachage = hmac.new(CLE_SECRETE.encode(), str(horodatage).encode(), hashlib.sha256).hexdigest()
    return str(int(hachage, 16))[-8:]  # Prendre les 8 derniers chiffres hexadécimaux comme OTP

def mettre_a_jour_otp():
    """
    Met à jour l'OTP affiché sur l'interface utilisateur et démarre le compte à rebours.
    """
    nouvel_otp = generer_otp()
    etiquette_otp.config(text=nouvel_otp)
    etiquette_temps.config(text="Temps restant : 60s")
    demarrer_compte_a_rebours(60)

def demarrer_compte_a_rebours(secondes):
    """
    Affiche un compte à rebours avant la mise à jour du prochain OTP.
    """
    if secondes >= 0:
        etiquette_temps.config(text=f"Temps restant : {secondes}s")
        fenetre_principale.after(1000, demarrer_compte_a_rebours, secondes - 1)
    else:
        mettre_a_jour_otp()

# 🔹 Création de la fenêtre principale
fenetre_principale = tk.Tk()
fenetre_principale.title("Client OTP")
fenetre_principale.geometry("400x300")
fenetre_principale.configure(bg="#2C3E50")  # Couleur de fond

# 🔹 Cadre principal pour contenir les éléments
cadre = tk.Frame(fenetre_principale, bg="#34495E", padx=20, pady=20)
cadre.pack(pady=20, padx=20, fill="both", expand=True)

# 🔹 Label pour afficher le titre
titre = tk.Label(cadre, text="🔐 Votre OTP", font=("Arial", 18, "bold"), fg="white", bg="#34495E")
titre.pack(pady=5)

# 🔹 Label pour afficher l'OTP
etiquette_otp = tk.Label(cadre, text=generer_otp(), font=("Arial", 28, "bold"), fg="#E74C3C", bg="#34495E")
etiquette_otp.pack(pady=10)

# 🔹 Label pour afficher le temps restant
etiquette_temps = tk.Label(cadre, text="Temps restant : 60s", font=("Arial", 14), fg="white", bg="#34495E")
etiquette_temps.pack(pady=5)


# 🔹 Lancement du premier OTP et du compte à rebours
mettre_a_jour_otp()

# 🔹 Exécution de l'interface graphique
fenetre_principale.mainloop()
