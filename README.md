# local-assistant
> llm agent for local assistant with vocal ( STT not include )

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Auteurs](#auteurs)
- [Remerciements](#remerciements)

## Introduction
Dans un monde où les assistants vocaux dominants comme Alexa, Google Assistant et Siri semblent souvent déconnectés des besoins quotidiens et des scénarios uniques que nous envisageons, il est temps de réimaginer ce qu'un assistant vocal peut être. Ce projet est né d'une vision : créer un assistant vocal qui soit véritablement local, un outil qui s'intègre harmonieusement avec nos autres projets, qu'il s'agisse de reconnaissance vocale, de synthèse vocale, ou de bien d'autres innovations.

Plutôt que de chercher à surpasser les géants, l'objectif est de faire les choses correctement. Car, comme le dit le proverbe, "le mieux est l'ennemi du bien". Cet assistant est conçu pour être un allié fidèle, capable d'exécuter des appels de fonctions en utilisant les ressources locales de l'utilisateur, tout en respectant la simplicité et l'efficacité. C'est une invitation à redécouvrir la puissance de la technologie locale, façonnée par et pour ses utilisateurs.

## Installation
Pour installer et utiliser ce projet de manière optimale, il est recommandé d'utiliser un environnement virtuel. Cela permet de gérer les dépendances de manière isolée et d'éviter les conflits avec d'autres projets.

### Installation de pyenv
1. **Installer les dépendances nécessaires** :
   ```bash
   sudo apt update
   sudo apt install -y make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
   libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
   python-openssl git
   ```

2. **Installer pyenv** :
   ```bash
   curl https://pyenv.run | bash
   ```

3. **Ajouter pyenv à votre shell** :
   Ajoutez les lignes suivantes à votre fichier `~/.bashrc` ou `~/.zshrc` :
   ```bash
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv virtualenv-init -)"
   ```

4. **Redémarrer votre terminal** ou exécuter :
   ```bash
   source ~/.bashrc
   ```

### Installation de Python 3.10.16 avec pyenv
1. **Installer Python 3.10.16** :
   ```bash
   pyenv install 3.10.16
   ```

2. **Définir la version globale de Python** :
   ```bash
   pyenv global 3.10.16
   ```

### Création d'un environnement virtuel avec virtualenv
1. **Installer virtualenv** :
   ```bash
   pip install virtualenv
   ```

2. **Créer un environnement virtuel** :
   ```bash
   virtualenv venv
   ```

3. **Activer l'environnement virtuel** :
   ```bash
   source venv/bin/activate
   ```

4. **Installer les dépendances du projet** :
   Avec l'environnement virtuel activé, installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
Exemples et instructions sur la façon d'utiliser le projet après l'installation.

## Contribuer
Instructions pour ceux qui souhaitent contribuer au projet, y compris les règles de contribution et le processus de pull request.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs
Liste des contributeurs principaux et leurs rôles.

## Remerciements
Remerciements à ceux qui ont aidé au développement du projet.

