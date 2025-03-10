# Generateur-de-otp-et-Validation
Deux logiciels avec Tkinter en Python pour la simulation de la  génération et la validation de otp 
# Système d'authentification OTP sécurisé entre Client et Serveur

Ce projet implémente un système d'authentification basé sur un jeton à usage unique (OTP), synchronisé entre un client et un serveur. Le jeton est généré de manière sécurisée à l'aide de l'algorithme HMAC-SHA256, garantissant une validation d'utilisateur fiable sans communication directe entre les deux applications.

## Technologies utilisées

- **Python** : Langage de programmation principal utilisé pour développer l'application client et serveur.
- **Tkinter** : Bibliothèque pour l'interface graphique des applications client et serveur.
- **HMAC et hashlib** : Modules pour la génération sécurisée des jetons OTP via HMAC-SHA256.
- **Time** : Module Python pour la gestion du temps et la synchronisation des jetons entre le client et le serveur.

## Fonctionnalités

### Application Client

- Génération d'un OTP toutes les 60 secondes en utilisant une clé secrète et un horodatage.
- Interface utilisateur moderne avec mise à jour automatique du code OTP et un compte à rebours.
- Le jeton change toutes les 60 secondes, rendant l'attaque par brute-force plus difficile.

### Application Serveur

- Vérification de l'OTP saisi par l'utilisateur en le comparant avec l'OTP généré via HMAC-SHA256.
- Limitation à 5 tentatives d'authentification avant la fermeture automatique de l'application.
- Gestion du temps écoulé : si aucun OTP valide n’est saisi en 60 secondes, l'accès est refusé automatiquement.

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/ton-utilisateur/otp-synchronisation.git
   ```

2. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

3. Exécutez l'application client et serveur :

   - Lancer l'application client dans un terminal :

     ```bash
     python client.py
     ```

   - Lancer l'application serveur dans un autre terminal :

     ```bash
     python server.py
     ```

## Utilisation

- Une fois les applications démarrées, l'application client générera un OTP toutes les 60 secondes.
- L'utilisateur peut saisir ce code dans l'application serveur pour valider son accès.
- L'OTP sera valide pendant 60 secondes. Après ce délai, un nouveau code sera généré.

## Résultats

Le système d'authentification est conçu pour fonctionner de manière sécurisée et fiable. Des ajustements ont été effectués pour résoudre les problèmes de synchronisation temporelle et pour garantir que les deux applications génèrent et valident le même OTP sans communication directe.

## Auteurs

- Koffitse Fiadupe Amouzou
- Abeni Victoire

## Références

- [HMAC - Wikipédia](https://fr.wikipedia.org/wiki/HMAC)
- [Documentation Python - HMAC](https://docs.python.org/3/library/hmac.html)
- [Documentation Tkinter](https://docs.python.org/3/library/tkinter.html)
- [SHA-256 - Wikipédia](https://fr.wikipedia.org/wiki/SHA-2)
- [Module Subprocess](https://docs.python.org/3/library/subprocess.html)

##
