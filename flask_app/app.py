from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

# max number of results to return to the user (sending all ~2 million is too much)
result_limit = 1000


# the ORM model used to store the knuckle tattoos
class Tattoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base = db.Column(db.String(8))
    scrambled = db.Column(db.String(8))

    def __init__(self, base, scrambled):
        self.base = base
        self.scrambled = scrambled

    def __repr__(self):
        return "%s -> %s" % (self.base, self.scrambled)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    # process the user's query if there is one
    q = request.args.get("q", None)
    if q:
        like_arg = "%%%s%%" % q
        tats = Tattoo.query.filter((Tattoo.base.like(like_arg)) | (Tattoo.scrambled.like(like_arg))).limit(result_limit)
    else:
        tats = Tattoo.query.limit(result_limit).all()

    # the data passed to the jinja2 template
    template_dict = {
        "query": q,
        "tats": tats
    }

    return render_template('home.html', data=template_dict)

if __name__ == '__main__':
    app.run()
