# Orange Country Lettings

## Installation et utilisation en local

### Avec python

#### Prérequis

- Git
- Python 3

#### Mettre en place l'environnement

```shell
git clone https://github.com/jogubo/oc-lettings.git
cd oc-lettings
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

####  Base de données et migration

La BDD présente sur ce dépôt ne necessite aucune intervention.

Si vous souhaitez utiliser la BDD du projet original, il est nécessaire d'ignorer les migrations initiales 
pour `lettings` et `profiles`.
Si vous souhaitez créer une nouvelle BDD, vous pouvez ingorer cette étape et réaliser une
migrations normalement.
```shell
python manage.py migrate lettings 0001 --fake
python manage.py migrate profiles 0001 --fake
```

#### Définir les variables d'environnement

Une clef secrète est indispensable pour lancer le serveur, cette clef doit être définie en
variable d'environnement:
```shell
export DJANGO_SECRET_KEY='YOUR_SECRET_KEY'
```

Vous pouvez générer une clef et l'enregistrer dans un fichier en une commande:
```shell
python -c "from django.core.management.utils import get_random_secret_key; print(f'DJANGO_SECRET_KEY={get_random_secret_key()}')" > .env
cat .env
```

Par défaut, la configuration est pour une utilsation en production, le mode débogage peut être activé
avec la variable `DEBUG=1`


#### Lancer le serveur

Il est conseillé d'utiliser `gunicorn` pour une utilsation en production:
```shell
gunicorn --chdir src config.wsgi --log-file -
```

Pour du développement, la commande habituelle pour lancer le server:
```shell
python src/manage.py runserver
```


### Avec Docker

#### Prérequis

- Docker
- Git (si vous souhaitez construire votre image)

#### Récupérer une image

##### Directement depuis Docker Hub

Le tag `latest` correspond au dernier commit sur master, les autres tag correspondent
un hash du commit.
```shell
docker pull jogubo/oc-lettings:latest
```

#### Construire l´image depuis les sources

```shell
git clone https://github.com/jogubo/oc-lettings.git
cd oc-lettings
docker build -t oc-lettings .
```

#### Lancer le serveur

Pour utiliser l'image Docker, il faut spécifier une clef secrète en argument.
Il est également possible de changer le port et/ou lancer Django en mode débogage
```shell
docker run -p 80:5000 -e PORT=5000 -e DEBUG=1 -e DJANGO_SECRET_KEY='YOUR_KEY' jogubo/oc-lettings
```

Docker permet aussi d'utiliser un fichier `.env`.
```shell
docker run -d -p 80:8000 --env-file .env jogubo/oc-lettings
```
