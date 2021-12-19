# Example API with FastAPI

This project is a example API with FastAPI

## Installing

To install and execution the API In your local machine, you will need to:

```
a) Clone the project, and entry on folder of API:

git clone https://github.com/RicardoTurco/FastAPI_YT_complete.git && cd FastAPI_YT_complete/


b) Create and activate one "virtualenv" (SO Linux):

python3 -m venv venv
source venv/bin/activate


c) Install the dependences of project:

pip install -r requirements.txt


d) Create database:
(all times this script is executed, it will drop all tables)

python criar_tabelas.py


e) Run the project:

uvicorn main:app --reload
```

## Database

The API use SQLite database.

## Swagger

After the application goes up, open your browser on `localhost:8000/docs` to see the self-documented interactive API.

## Tests

`python -m pytest tests/`

## Files

* `.gitignore` - Lists files and directories which should not be added to git repository.
* `README.md` - Instructions and informations to run this project locally.
* `requirements.txt` - All project dependencies.
* `main.py` - The Application entrypoint.