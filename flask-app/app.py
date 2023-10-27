from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from listennotes import podcast_api
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins='http://127.0.0.1:5500')



 
@app.route('/podcasts', methods=['GET'])
def  get_podcast():
    api_key = ''

    client = podcast_api.Client(api_key=api_key)      

    response = client.fetch_best_podcasts(
        genre_id='133',
        page=2,
        region='us',
        sort='listen_score',
        safe_mode=0,
        )
                
    return(response.json())


if __name__ == '__main__':
    app.run(debug=True) 