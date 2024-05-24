# 2023_wa_sz_petrik_gaflix

### Venv
- `py -3 -m venv venv`
- `source ./venv/Scripts/activate`
- `pip install -r requirements.txt`

### Server & migrations
- run server - `python manage.py runserver`
- `python manage.py makemigrations`
- `python manage.py migrate`
- admin - `python manage.py createsuperuser`

### Fixtures
- dump test data`./manage.py dumpdata --indent 2 filmy.MODELNAME > fixtures/FILENAMEOFMODEL.json`  
  UTF-8 Chars: sh - `export PYTHONIOENCODING=utf-8 && python manage.py dumpdata --indent 2 filmy.Movie > fixtures/film.json`
- load fixtures - `python manage.py loaddata fixtures/film.json`

*Last edited 24.5.2024*
