# Utilisation de l'image Python officielle en tant que base
FROM python:3.8-slim

# Copie des dépendances de l'application
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ajout du reste de l'application
COPY . .

# Exécution de l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.x

# Reste de votre Dockerfile


# Utilisation d'une image PostgreSQL officielle
FROM mariadb:latest

# Copie du fichier init.sql dans le conteneur
COPY init.sql /docker-entrypoint-initdb.d/

# Exécution des scripts SQL au démarrage
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=mydatabase

# Commande par défaut pour démarrer MariaDB
CMD ["mysqld"]

# Exposer le port PostgreSQL par défaut (5432)
EXPOSE 5432
FROM postgres:13

# Copy the SQL file into the Docker container
COPY init.sql /docker-entrypoint-initdb.d/


