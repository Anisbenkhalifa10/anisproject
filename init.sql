-- Création de la base de données
CREATE DATABASE IF NOT EXISTS mydatabase;

-- Utilisation de la base de données
USE mydatabase;

-- Création d'une table
CREATE TABLE IF NOT EXISTS mytable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insertion de données initiales
INSERT INTO mytable (name) VALUES ('Première entrée'), ('Deuxième entrée');
