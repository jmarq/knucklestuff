# a flask web application for serving the knuckle tattoos
*this application has additional dependencies, listed in flask_app_requirements.txt*

## uses sqlalchemy and sqlite to store/query the tats
users can search for tattoos/scrambles that contain words that interest them

## Usage:

1. make sure you have the dependencies from flask_app_requirements.txt installed
2. make sure you have a text file from which to read the tattoo results (the default is scrabble_results.txt in the parent directory of this flask app).  If you don't, run the scramble finder code (see the readme in the parent directory)
3. run create_db.py
4. run populate_db.py (this takes a while and is resource intensive)
5. run app.py, or deploy it with gunicorn or some other wsgi server of your choice. 
6. visit the app in your web browser (http://localhost:5000 by default)


