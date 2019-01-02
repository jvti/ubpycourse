from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def userupload():
    f = request.files['pic']
    f.save(f.filename)

    r = requests.post('https://api.imagga.com/v2/uploads',
                             auth=('acc_c139eaa6a1339e4', '0cc8a6c34d773a3b4d585c68cba64721'),
                             files={'image': open(f.filename, 'rb')}).json()['result']['upload_id']

    response = requests.get('https://api.imagga.com/v2/tags',
                         auth=('acc_c139eaa6a1339e4', '0cc8a6c34d773a3b4d585c68cba64721'),
                         params={'image_upload_id':r}).json()['result']['tags'][0]['tag']['en']

    response = requests.get('http://api.giphy.com/v1/gifs/search',
                            params={'q':response,
                            'api_key': 'anAJFbecEObpxqyksfnbcard6Gm4XjBp'}).json()['data']

    return render_template('upload.html', resp = [ response[i]['images']['fixed_height']['url'] for i in range(10) ])

if __name__ == '__main__':
    app.run(debug=True)
