## 09/05/2023


![Image text](https://talentportugal.com/wp-content/uploads/2022/01/mercadona_emprego_trabalho_estagio_candidatura_espontanea_talent_portugal_equipa_banner-768x368.jpeg)


## Table Content

1. Informations Générales
2. Langage et Packages
3. installation

## Informations Générales

Applicatin Marcadona Publicité

### Langage et Package

- asgiref==3.6.0
- Django==3.1.6
- django-environ==0.10.0
- psycopg2==2.9.6
- pytz==2023.3
- sqlparse==0.4.4

## Installation

---

Petite intro installation

```
cloner le repo
git clone https://github.com/seb76370/mercadona_publicite.git
$ creation d'un environnemnt virtuel
$ pyhton install -r requirements.txt
$ mise en place d'un fichier .env sous src/mercadona_publicite 
$ avec les données suivante
- SECRET_KEY=''
- DATABASE_NAME=""
- DATABASE_USER=""
- DATABASE_PASS=""
- DATABASE_HOST=""
- DATABASE_PORT="5432"
```

## Running the app

```bash
# development
$ cd src
$ python manage.py runserver
```
