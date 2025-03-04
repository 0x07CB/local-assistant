FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances et les installer
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du projet dans le conteneur
COPY . ./

# Rendre le script principal exécutable
RUN chmod +x local-assistant/main.py

# Définir le point d'entrée pour le conteneur
ENTRYPOINT ["./local-assistant/main.py"]

# Par défaut, afficher l'aide
CMD ["-h"]