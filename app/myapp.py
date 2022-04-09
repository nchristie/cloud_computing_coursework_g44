from flask import Flask, jsonify
import requests

all_records = [
    {
        "name": "Radiohead",
        "albums": [
            {
                "title": "The King of Limbs",
                "songs": [],
                "description":"satisfactory"
            },
            {
                "title": "OK Computer",
                "songs": [],
                "description":"good"
            }
        ]
    },
    {
        "name": "Portishead",
        "albums": [
            {
                "title": "Dummy",
                "songs": [],
                "description":"excellent"
            },
            {

                "title": "Third",
                "songs": [],
                "description":"not bad"
            }
        ]
    }
]

app = Flask(__name__)


@app.route('/')
def hello():
    return('<h1>Welcome to music finder!</h1>')


@app.route('/records/', methods=['GET'])
def get_records():
    return jsonify(all_records)


@app.route('/records/all_bands/', methods=['GET'])
def get_bands():
    response = [item['name'] for item in all_records]
    return jsonify(response)


@app.route('/records/albums_by_band/<bandname>/', methods=['GET'])
def get_album_by_band(bandname):
    response = {bandname: 'Not Found!'}
    for item in all_records:

        if item["name"] == bandname:
            response = [x["title"] for x in item["albums"]]
            break
    return jsonify(response)


@app.route('/records/<bandname>/<album>/', methods=['GET'])
def get_description_of_album(bandname, album):
    response = {album: 'Not Found!'}
    for item in all_records:
        if item["name"] == bandname:
            for album_title in item['albums']:
                if album_title['title'] == album:
                    response = album_title['description']
                    break
    return jsonify(response)


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
