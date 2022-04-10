# imports
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
 
# initializing Flask app
app = Flask(__name__)
 
# Google Cloud SQL (change this accordingly)
PASSWORD ="0000"
PUBLIC_IP_ADDRESS ="35.242.173.183"
DBNAME ="gcp_project"
PROJECT_ID ="animated-rope-339716"
INSTANCE_NAME ="gcp-project"
 
# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
 
db = SQLAlchemy(app)
 
# User ORM for SQLAlchemy
class albumsongs(db.Model):
    albumname = db.Column(db.String(255), primary_key = True, nullable = False)
    songname = db.Column(db.String(255),primary_key = True, nullable = False)


@app.route('/', methods = ['GET'])
def hello():
    return('<h1>Welcome to the Music Site!<h1>')
 
 
@app.route('/view/')
def view():
    # fetches all the users
    songs = albumsongs.query.all()
    # response list consisting user details
    response = list()
 
    for song in albumsongs:
        response.append({
            "albumname" : song.albumname,
            "songname": song.songname
        })
 
    return make_response({
        'status' : 'success',
        'message': response
    }, 200)
 
 
if __name__ == "__main__":
    # serving the app directly
    app.run(host='0.0.0.0', port =80)
