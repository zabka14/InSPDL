#Installations Sportives Pays de la Loire 
========

L'objectif est de développer une application manipulants des données relatives aux installations sportives de la région Pays de la Loire.

Les données sont issues de [http://data.paysdelaloire.fr](http://data.paysdelaloire.fr).

## Architecture

![architecture.png](images/architecture.png)

## Fonctionnement basique

Le fichier interactionsBD.py regroupe plusieurs fonctions.
Certaines permettent de créer/mettre à jour une base de donnée en se basant sur des fichiers .csv récupérer sur le site [http://data.paysdelaloire.fr](http://data.paysdelaloire.fr).
Une fois cette base de donnée en place, le serveur (rest-example.py) permet, à travers une interface web (utilisant Bottle) d'aller chercher des informations relatives aux données stockés dans la base de données.

## Utilisation de l'interface web

### Utilisation standard

Sur la page d'accueil, un formulaire est disponible. Il est possible de : 

- Chercher toutes les installations sportives d'une ville propre à un sport donné
	En entrant une ville dans le champ ville et un sport dans le champ sport
- Chercher toutes les villes de la région ou il est possible de pratiquer un sport
	En entrant uniquement un sport dans le champ sport
- Chercher toutes les installations sportives disponibles dans une ville
	En entrant uniquement une ville dans le champ ville

Dans le cas ou uniquement le champ sport est entré, une liste des villes ou il est possible de pratiquer le sport s'affiche. Cliquer sur le nom d'une ville affiche la liste des installations disponible pour ce sport dans cette ville.

### Utilisations avancée

Il est possible en cliquant sur la checkbox prévue à cet effet d'afficher des options avancées.
Ces dernières restreignent la recherche dans la base de données selon certains critères.
