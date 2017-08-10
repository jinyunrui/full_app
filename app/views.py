from app import app
from app import db
from flask import render_template, request, jsonify
from app.models import FileNames

#how to do search courtesy of: https://marcobonzanini.com/2015/02/02/how-to-query-elasticsearch-with-python/
@app.route('/', methods=['GET','POST'])
def index():
    files = [elem.filename for elem in FileNames.query.all()]
    return render_template('index.html', files=files)

