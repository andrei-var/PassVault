# 🔒 PassVault V3.0 — Modern & Secure Password Manager

**PassVault** est un gestionnaire de mots de passe de bureau privé, sécurisé et ultra-fluide développé en **Python** avec une interface graphique moderne basée sur **CustomTkinter**.

Toutes vos données sont chiffrées localement selon les normes cryptographiques de pointe (**PBKDF2 avec 600 000 itérations** et **AES-128 / Fernet**). Aucune donnée ne quitte votre machine.

---

## ✨ Fonctionnalités Principales

### 🎨 Interface Moderne & Ergonomique
* **Thème Dark Moderne (Obsidian & Purple)** : Interface graphique soignée avec contrastes élevés et typographies nettes.
* **Barre Latérale de Navigation** : Transition fluide et instantanée entre vos tableaux de bord sans rechargement de fenêtre.
* **Cartes d'Identifiants Interactives** : Visualisation par cartes avec badges de catégories, boutons de copie rapide en un clic, affichage/masquage du mot de passe et boîte de dialogue de modification.

### 🛡️ Sécurité de Niveau Militaire
* **Audit de Sécurité du Vault** : Analyse en direct de la santé de votre coffre-fort (score de sécurité global, détection des mots de passe faibles, réutilisés ou trop anciens).
* **Générateur CSPRNG Avancé** : Génération de mots de passe cryptographiquement sûrs (`secrets`) avec gestion de la longueur (8 à 64 caractères), des symboles et exclusion des caractères ambigus (`l`, `1`, `I`, `0`, `O`).
* **Verrouillage Automatique par Inactivité** : Verrouille automatiquement l'accès au coffre après 5 minutes d'inactivité.
* **Nettoyage Automatique du Presse-Papier** : Efface automatiquement les mots de passe et identifiants copiés dans le presse-papier après 30 secondes pour éviter les fuites.
* **Contrôle en Temps Réel du Mot de Passe Maître** : Exige un mot de passe fort (12+ caractères, majuscule, chiffre, symbole) dès l'initialisation.

### ⚡ Gestion & Sauvegardes
* **Recherche et Filtres par Catégorie** : Filtrage en temps réel (*Personal, Work, Social, Finance, Other*).
* **Export / Import Chiffré (JSON)** : Sauvegarde exportable entièrement chiffrée avec un mot de passe dédié pour transférer votre coffre en toute sécurité.
* **Changement de Mot de Passe Maître** : Déchiffre, re-génère un sel et re-chiffre l'intégralité du coffre automatiquement.
* **Nuclear Reset** : Possibilité de réinitialiser complètement le coffre local en cas d'oubli du mot de passe maître.

---

## 🏗️ Architecture du Projet

```
PassVault/
├── run.py                 # Point d'entrée principal avec auto-détection Tk 8.6
├── requirements.txt       # Dépendances Python testées et compatibles
├── README.md              # Documentation complète
├── assets/                # Icônes et ressources graphiques
└── src/
    ├── core/              # Moteur logique, base de données et chiffrement
    │   ├── crypto.py      # Dérivation de clé PBKDF2 (600k itérations) & Fernet AES
    │   ├── database.py    # Gestionnaire SQLite avec migrations de schéma
    │   └── security.py    # Calcul du score d'audit & analyse de complexité
    ├── ui/                # Composants d'interface utilisateur (CustomTkinter)
    │   ├── app.py         # Fenêtre principale, navigation & timers d'inactivité
    │   └── views/
    │       ├── login.py       # Écran d'initialisation / déverrouillage maître
    │       ├── home.py        # Structure principale avec barre latérale
    │       ├── dashboard.py   # Tableau de bord d'audit & score de sécurité
    │       ├── view.py        # Liste des mots de passe, recherche & filtres
    │       ├── add.py         # Formulaire d'ajout sécurisé
    │       ├── generator.py   # Générateur de mots de passe personnalisable
    │       └── settings.py    # Changement de mot de passe, exports/imports
    └── utils/
        └── helpers.py     # Générateur CSPRNG & gestionnaire de presse-papier multi-plateforme
```

---

## 🚀 Installation & Démarrage Rapide

### 📋 Prérequis
* **Python 3.10 ou supérieur** (recommandé : **Python 3.11**).
* **Git**.

---

### 🍏 Sur macOS (Important)

> [!IMPORTANT]
> macOS intègre par défaut un vieux Python système (3.9) équipé de **Tcl/Tk 8.5** (obsolète), ce qui peut provoquer une fenêtre vide avec CustomTkinter.
> Pour avoir une interface parfaite, installez Python 3.11 avec son support Tk 8.6 via Homebrew :

```bash
# 1. Installer Python 3.11 et Tkinter moderne
brew install python@3.11 python-tk@3.11

# 2. Cloner le dépôt et entrer dans le dossier
git clone https://github.com/android-varx/PassVault.git
cd PassVault

# 3. Créer et activer l'environnement virtuel
python3.11 -m venv venv
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
python run.py
```

---

### 🐧 Sur Linux (Ubuntu / Debian / Fedora)

```bash
# 1. Installer Tkinter système si nécessaire
sudo apt-get update && sudo apt-get install python3-tk python3-venv git

# 2. Cloner et préparer l'environnement
git clone https://github.com/android-varx/PassVault.git
cd PassVault

python3 -m venv venv
source venv/bin/activate

# 3. Installer et lancer
pip install -r requirements.txt
python run.py
```

---

### 🪟 Sur Windows

```powershell
# 1. Cloner le projet
git clone https://github.com/android-varx/PassVault.git
cd PassVault

# 2. Créer et activer l'environnement virtuel
python -m venv venv
.\venv\Scripts\activate

# 3. Installer et lancer
pip install -r requirements.txt
python run.py
```

---

## 📦 Dépendances (`requirements.txt`)

| Paquet | Version | Description |
| :--- | :--- | :--- |
| **`customtkinter`** | `>=5.2.0` | Framework d'interface graphique moderne dark mode |
| **`cryptography`** | `>=41.0.0` | Dérivation de clé PBKDF2 et chiffrement AES Fernet |
| **`Pillow`** | `>=10.0.0` | Traitement et rendu des icônes et images |
| **`pyperclip`** | `>=1.8.2` | Accès au presse-papier système sécurisé |
| **`darkdetect`** | `>=0.8.0` | Détection automatique du thème système (Dark/Light) |

---

## 🔐 Spécifications Cryptographiques

1. **Sel Cryptographique Unique** : Généré aléatoirement avec `os.urandom(16)` lors du premier lancement et stocké dans la table `config` SQLite locale.
2. **KDF (Key Derivation Function)** : `PBKDF2HMAC` avec `SHA-256`, longueur de clé 32 octets, et **600 000 itérations** (conformité aux recommandations OWASP).
3. **Chiffrement Symétrique** : `Fernet` (chiffrement AES-128 en mode CBC avec HMAC-SHA256 pour l'intégrité et l'authentification des données chiffrées).
4. **Zéro Connaissance (Zero-Knowledge)** : Le mot de passe maître n'est jamais stocké en clair, seul un jeton de validation chiffré permet de valider le déchiffrement à la volée.

---

## ❓ Dépannage & FAQ

<details>
<summary><b>1. La fenêtre s'ouvre mais reste vide ou noire sur macOS</b></summary>

Cela se produit lorsque l'application est exécutée avec le Python système (Tk 8.5) au lieu de Python 3.11 (Tk 8.6).
Exécutez :
```bash
brew install python@3.11 python-tk@3.11
python3.11 run.py
```
Le fichier [`run.py`](file:///Users/andrei/Desktop/repositories/PassVault/run.py) intègre également un auto-relais automatique vers Python 3.11 si détecté sur votre système.
</details>

<details>
<summary><b>2. J'ai oublié mon mot de passe maître</b></summary>

Conformément au principe de sécurité Zero-Knowledge, il est mathématiquement impossible de récupérer un coffre sans le mot de passe maître.
Sur l'écran de verrouillage, cliquez sur le bouton rouge **"Forgot Password? (Nuclear Reset)"** pour effacer la base locale et repartir sur un coffre neuf.
</details>

---

## 📄 Licence
Ce projet est open-source et sous licence MIT.
