from flask import Flask, render_template, request
import os
# import reazonspeech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if not file:
      return 'No file uploaded'

    if file.filename == '':
        return 'No selected file'

    file.save(os.path.join('uploads', file.filename))  # uploadsフォルダに保存
    return 'File saved successfully'

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
