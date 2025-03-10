import time
import hmac
import hashlib
import tkinter as tk
from tkinter import messagebox

# Clé secrète utilisée pour générer et vérifier les OTP
CLE_SECRETE = "KOFFITSE_ET_VICTOIRE"

# Compteur d'échecs d'authentification et autres variables
tentatives = 0
dernier_otp = ""  # Dernier OTP généré pour la période précédente
temps_ecoule = False  # Indicateur si 60 secondes se sont écoulées sans saisie de l'utilisateur
premier_otp_genere = False  # Indicateur si l'OTP a déjà été généré
dernier_otp_precedent = ""  # Dernier OTP précédemment généré à afficher
derniere_saisie = time.time()  # Enregistrer le moment de la dernière saisie
premiere_generation_otp = None  # Variable pour stocker l'heure de la première génération de l'OTP

# Fonction pour générer un OTP basé sur le temps actuel
def generer_otp():
    """
    Génère un OTP unique basé sur l'heure actuelle et une clé secrète.
    L'OTP est valide pour 60 secondes.
    """
    horodatage = int(time.time()) // 60  # Convertit l'heure actuelle en période de 60 secondes
    hachage = hmac.new(CLE_SECRETE.encode(), str(horodatage).encode(), hashlib.sha256).hexdigest()
    return str(int(hachage, 16))[-8:]  # Retourne les 8 derniers chiffres de l'empreinte

# Fonction pour valider l'OTP entré par l'utilisateur
def valider_otp():
    """
    Vérifie si l'OTP entré par l'utilisateur est correct.
    En cas d'échec, l'utilisateur a 5 tentatives avant la fermeture de l'application.
    """
    global tentatives  # Utilisation de la variable globale
    otp_utilisateur = champ_saisie.get()  # Récupération de l'OTP entré par l'utilisateur

    if otp_utilisateur == dernier_otp:
        messagebox.showinfo("Validation", "Accès confirmé !")  # Affiche un message de succès
        champ_saisie.delete(0, tk.END)  # Efface l'entrée après validation
        racine.destroy()    # Ferme l'application après validation
    else:
        tentatives += 1  # Incrémente le compteur d'échecs
        messagebox.showerror("Erreur", f"Accès refusé ! ({tentatives}/5)")  # Affiche un message d'erreur
        champ_saisie.delete(0, tk.END)  # Efface l'entrée après validation
        if tentatives >= 5:
            racine.destroy()  # Ferme l'application après 5 tentatives

# Fonction pour mettre à jour l'OTP à afficher
def mettre_a_jour_otp():
    """
    Met à jour l'OTP à afficher et garde une trace du dernier OTP.
    """
    global dernier_otp  # Utilisation de la variable globale dernier_otp
    global dernier_otp_precedent  # Pour stocker l'OTP précédent
    global premiere_generation_otp  # Utilisation de la variable globale premiere_generation_otp

# Vérifier si c'est la première génération
    if premiere_generation_otp is None:
        premiere_generation_otp = time.time()  # Enregistrer l'heure de la première génération
        dernier_otp = generer_otp()
    # Conserver l'OTP actuel avant de générer un nouveau OTP
   
    dernier_otp_precedent = dernier_otp  # Conserver l'OTP précédent dans une variable temporaire

# Vérifier si 60 secondes se sont écoulées depuis la première génération de l'OTP
    if time.time() - premiere_generation_otp >= 60:
        dernier_otp = generer_otp()  # Générer un nouvel OTP uniquement après 60 secondes depuis la première génération
        premiere_generation_otp = time.time()  # Réinitialiser l'heure de la génération pour la prochaine vérification de 60 secondes
# Fonction pour démarrer le processus de génération et de vérification
def demarrer_compte_a_rebours():
    """
    Démarre le compte à rebours toutes les 60 secondes.
    """
    global tentatives  # Déclare la variable tentatives comme globale
    global derniere_saisie  # Accéder à la dernière saisie de l'utilisateur
    global temps_ecoule
    global premier_otp_genere  # Vérifier si le premier OTP a été généré
    # Vérifier si le temps est écoulé sans saisie
    if premiere_generation_otp is not None and time.time() - premiere_generation_otp >= 60:
        mettre_a_jour_otp()
        messagebox.showwarning("Temps écoulé", f"Temps écoulé, accès refusé ! ")
        

    # Mettre à jour l'OTP toutes les 60 secondes
   
# Afficher l'OTP précédent après la mise à jour (si le premier OTP a déjà été généré)
    if premier_otp_genere:
        etiquette_ancien_otp.config(text=f"Dernier OTP valide : {dernier_otp_precedent}")  # Afficher l'OTP précédent
    else:
        premier_otp_genere = True  # Marquer que le premier OTP a été généré

    # Redémarrer le processus après 60 secondes
    racine.after(60000, demarrer_compte_a_rebours)

# Fonction pour détecter la saisie de l'utilisateur
def detecter_saisie(event=None):
    """
    Fonction qui est appelée à chaque modification de la saisie de l'utilisateur.
    """
    global derniere_saisie
    derniere_saisie = time.time()  # Mettre à jour le temps de la dernière saisie

# Création de la fenêtre principale de l'interface graphique
racine = tk.Tk()
racine.title("Serveur OTP")  # Titre de la fenêtre
racine.geometry("400x300")  # Dimensions de la fenêtre
racine.configure(bg="#2C3E50")  # Couleur de fond

# Création d'un cadre pour organiser les widgets
cadre = tk.Frame(racine, bg="#34495E", padx=20, pady=20)
cadre.pack(pady=30, padx=30, fill="both", expand=True)

# Création d'un label pour afficher l'OTP précédent (celui de la dernière minute)
etiquette_ancien_otp = tk.Label(cadre, font=("Arial", 14), fg="white", bg="#34495E")
etiquette_ancien_otp.pack(pady=10)

# Création d'un label pour demander l'OTP
etiquette = tk.Label(cadre, text="Entrez le OTP :", font=("Arial", 18), fg="white", bg="#34495E")
etiquette.pack(pady=10)

# Champ de saisie pour entrer l'OTP
champ_saisie = tk.Entry(cadre, font=("Arial", 18), justify="center")
champ_saisie.pack(pady=10)

# Ajouter un binding pour détecter la saisie de l'utilisateur
champ_saisie.bind("<Key>", detecter_saisie)

# Bouton de validation pour vérifier l'OTP
bouton_valider = tk.Button(cadre, text="Valider", command=valider_otp, font=("Arial", 18), fg="white", bg="#E74C3C", relief="flat")
bouton_valider.pack(pady=10)

# Lancer la mise à jour de l'OTP et le compte à rebours dès le début
mettre_a_jour_otp()  # On appelle la fonction avant de démarrer le compte à rebours pour avoir l'OTP précédent dès le départ
demarrer_compte_a_rebours()

# Lancement de la boucle principale de l'interface graphique
racine.mainloop()
