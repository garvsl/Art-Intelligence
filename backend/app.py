import json
from flask import Flask, render_template
from dotenv import load_dotenv
import os
import openai
import requests
import urllib

load_dotenv('app.env')

app = Flask(__name__, template_folder='../frontend/', static_folder='../frontend/assets/')


def generate_image(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    resp = openai.Image.create(
        prompt=prompt,
        n=1,
        size='256x256'
    )
    img_url = resp.get('data')[0]['url']
    return img_url


def list_estuary_data(limit=50, offset=0):
    url = os.getenv('ESTUARY_API_URL') + f'content/stats?limit={limit}&offset={offset}'
    headers = {
        'Authorization': f'Bearer {os.getenv("ESTUARY_API_KEY")}'
    }

    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        return False

    resp = json.loads(resp.text)

    img_urls = []
    for elem in resp:
        img_urls.append(os.getenv('ESTUARY_API_URL') + f'gw/ipfs/{elem["cid"]["/"]}')

    return img_urls


def upload_to_estuary(gen_img_url):
    # Uncomment for debugging
    # gen_img_url = generate_image('man walking')

    img_content = urllib.request.urlopen(gen_img_url).read()

    url = os.getenv('ESTUARY_UPLOAD_URL') + 'content/add'
    headers = {
        'Authorization': f'Bearer {os.getenv("ESTUARY_API_KEY")}'
    }

    files = {'data': img_content, 'filename': 'test'}
    resp = requests.post(url, files=files, headers=headers)

    if resp.status_code != 200:
        return False

    resp = json.loads(resp.text)
    return resp['retrieval_url']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get-started')
def get_started():
    return render_template('get-started.html')


@app.route('/upload', methods=['POST'])
def add(name, prompt):
    gen_img_url = generate_image(prompt)
    resp = upload_to_estuary(gen_img_url)

    if resp is not False:
        pass

    return 'upload'


if __name__ == '__main__':
    # list_estuary_data()
    # exit()
    app.run()
