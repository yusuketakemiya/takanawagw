# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from models import TwitterModel
import json

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

twittermodel = TwitterModel()

# @app.route('/login', methods=['GET', 'POST'])
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

# localhost:8080/twitteroauthurl
@app.route('/twitteroauthurl', methods=['GET'])
def twitteroauthurl():
    print('twitteroauthurl call')
    url = twittermodel.oauth_url()
    print('twitteroauthurl return:' + url)
    json_obj = {}
    json_obj["url"] = url
    response = json.dumps(json_obj, ensure_ascii=False)
    result = app.response_class(
        response=response,
        mimetype='application/json'
    )
    result.headers['Access-Control-Allow-Origin'] = '*' #デバッグ用クロスドメイン
    print(result)
    return result

# localhost:8080/twittercallback
@app.route('/twittercallback', methods=['GET'])
def twittercallback():
    # GETパラメータの取得(oauth_token, oauth_verifier)
    print("oauth_token:" + request.query.oauth_token)
    print("oauth_verifier:" + request.query.oauth_verifier)
    oauth_token = request.query.oauth_token
    oauth_verifier = request.query.oauth_verifier
    return twittermodel.oaut_token(oauth_verifier)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8081, debug=True)
# [END gae_python37_app]
