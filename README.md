# 2023_wa_sz_petrik_gaflix

### Venv
- `python3 -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`

### Server & migrations
- run server - `python manage.py runserver`
- `python manage.py makemigrations`
- `python manage.py migrate`
- admin - `python manage.py createsuperuser`

### Fixtures
- dump test data`./manage.py dumpdata --indent 2 filmy.MODELNAME > fixtures/FILENAMEOFMODEL.json`  
  UTF-8 Chars: sh - `export PYTHONIOENCODING=utf-8 && python manage.py dumpdata --indent 2 filmy.Movie > fixtures/film.json`
- load fixtures - `python manage.py loaddata fixtures/*.json`

### Deployment cmds
- git clone `https://github.com/gyarab/2023_wa_sz_petrik_gaflix`
- show dir content  `ls`
- edit file content `nano settings.py`  ALLOWED_HOSTS = ["wa.dtcloud.cz"] 
- print file content `cat settings.py`
- show id `id` 
- run server `python manage.py runserver 0.0.0.0:8020`
  http://wa.dtcloud.cz:8020

*Last edited 14.6.2024*
