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
class Albumsongs(db.Model):
    albumname = db.Column(db.String(255), primary_key = True, nullable = False)
    songname = db.Column(db.String(255),primary_key = True, nullable = False)


class Bandalbums(db.Model):
    bandname = db.Column(db.String(255), primary_key = True, nullable = False)
    albumname = db.Column(db.String(255), primary_key = True, nullable = False)
    description = db.Column(db.String(255),primary_key = False, nullable = True)
    releaseyear = db.Column(db.Integer,primary_key = False, nullable = True)


@app.route('/', methods = ['GET'])
def hello():
    return('<h1>Welcome to the Music Site!<h1>')
 
 
@app.route('/records/')
def view():
    # fetches all the songs in all albums
    songs = Albumsongs.query.all()
    # response list consisting albums and songs
    response = list()
 
    for song in songs:
        response.append({
            "albumname" : song.albumname,
            "songname": song.songname
        })
 
    return make_response({
        'status' : 'success',
        'message': response
    }, 200)


@app.route('/records/video/<bandname>', methods=['GET'])
def get_video(bandname):
    # takes a band name, returns URL to iTunes video if it exists
    try:
        formatted_bandname = "+".join(bandname.split())
        itunes_request = f"https://itunes.apple.com/search?term={formatted_bandname}&entity=musicVideo&limit=1"
        itunes_response_json = requests.get(itunes_request).json()
        itunes_url = itunes_response_json['results'][0]["previewUrl"]
        itunes_url_with_quotes = f'"{itunes_url}"'
        return(f"<h1>Here's a great video by {bandname}!</h1><h2><a href={itunes_url_with_quotes}>{itunes_url}</a></h2>")

    except:
        return(f"<h1>Sorry, we couldn't find a video by {bandname} for you :(</h1>")



@app.route('/addbandalbum/', methods =['POST'])
def add():
    # getting name and email
    bandname = request.form.get('bandname')
    albumname = request.form.get('albumname')
    description = request.form.get('description')
    releaseyear = request.form.get('releaseyear')

 
    try:
        # creating Bandalbums object
        bandalbum = Bandalbums(bandname = bandname, albumname = albumname, description = description, releaseyear = releaseyear)

            # adding the fields to users table
        db.session.add(bandalbum)
        db.session.commit()
            # response
        responseObject = {
            'status' : 'success',
            'message': 'Successfully Added.'
        }
 
        return make_response(responseObject, 200)
    except:
        responseObject = {
            'status' : 'fail',
            'message': 'Some error occured !!'
        }
 
        return make_response(responseObject, 400)






 
 
if __name__ == "__main__":
    # serving the app directly
    app.run(host='0.0.0.0', port =80)




