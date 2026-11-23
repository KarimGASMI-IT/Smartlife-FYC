# FYC SmartLife v0 — Cartographie des données

## 1. Architecture actuelle

Navigateur
    |
    v
Nginx (Web : 8080)
    |
    v
FastAPI (API : 8000 interne / 8001 sur la VM)
    |
    +----> PostgreSQL (5432 interne)
    |
    +----> MinIO (9000 interne, connexion applicative future)

Les services Docker Compose partagent le réseau smartlife-backend.

## 2. Inventaire des données

| Composant | Données actuelles | Données personnelles futures possibles |
|---|---|---|
| Web / Nginx | Page HTML, requêtes HTTP, journaux techniques | Identifiants de connexion, adresses IP |
| FastAPI | Réponses de santé, requêtes SQL de test | Profils utilisateurs, e-mails, identifiants |
| PostgreSQL | Base smartlife, requêtes de test | Comptes, profils, préférences |
| MinIO | Fichier de test sans données personnelles | Documents et fichiers utilisateurs |
| Docker / journaux | Événements techniques des conteneurs | Risque de présence accidentelle de données sensibles |

## 3. Flux et exposition

- Navigateur vers Web : HTTP, port 8080 limité à 127.0.0.1 sur la VM.
- Web vers API : HTTP sur le réseau Docker.
- API vers PostgreSQL : connexion SQL interne authentifiée.
- MinIO : API S3 sur 9000 et console sur 9001, ports limités à 127.0.0.1 sur la VM.
- API vers MinIO : pas encore implémentée.
- Une ancienne instance API autonome existe encore sur le port 8000 de la VM.

## 4. Stockage et secrets

- PostgreSQL : volume Docker postgres_data.
- MinIO : volume Docker minio_data.
- Identifiants PostgreSQL et MinIO : fichier local .env, exclu de Git.
- Le chiffrement TLS, la gestion avancée des accès et les politiques de rétention restent à mettre en place.

## 5. Risques à étudier dans les prochains modules

- S2 : exposition de données personnelles dans les logs.
- S3 : données sensibles dans les labels de métriques.
- S4 : attributs sensibles dans les traces.
- S5 : durée de conservation et suppression des données.
- S6 : segmentation des réseaux.
- S7 : authentification et autorisations.
- S8 : chiffrement des communications et protection des secrets.
- S9 : simulation et traitement d'un incident.

## 6. Situation de SmartLife v0

Les tests actuels utilisent des données techniques et un fichier de démonstration.
Aucun formulaire de collecte de données personnelles n'est encore implémenté.
Les catégories de données personnelles ci-dessus sont prospectives et devront
être actualisées lors de l'ajout de fonctionnalités.
