from flask import Flask, render_template, request
import get_images
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imagedownloader/')
def image_downloader():
    return render_template('R34_image_downloader.html')


@app.route('/imagedownloader/request/')
def user_request():
    user_tags = request.args.get('user_tags', None)
    user_numImage = request.args.get('user_numImage', None)
    user_score = request.args.get('user_score', None)
    rand = request.args.get('rand', None)
    get_images.get_images_script(user_tags, user_numImage, user_score)
    return render_template('request_page.html')

if __name__ == '__main__':
    app.run(debug=True)