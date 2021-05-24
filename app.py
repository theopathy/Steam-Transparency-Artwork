from flask import Flask, render_template, request, redirect, url_for,send_file
import os
import io
import mimetypes
from werkzeug.utils import secure_filename

import steamtransparency
app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = "uploads/"
@app.route("/")
@app.route("/index")
def index():

    return render_template("/index.html")
@app.route('/upload', methods=['POST'])
def upload():
    print("test")
    uploaded_file = request.files['file']
    #filename = secure_filename(uploaded_file.filename)
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        steamtransparency.DumpFile(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))
        
        return_data = io.BytesIO()
        with open(file_path, 'rb') as fo:
            return_data.write(fo.read())
        # (after writing, cursor will be at last byte, so move it to start)
        return_data.seek(0)
        
        os.remove(file_path)
        print(f.filename + "HELLOOOOOOOOOOOOOOOOOOOO!")
        print(mimetypes.guess_type(f.filename))
        return send_file(return_data, mimetype=mimetypes.guess_type(f.filename)[0],
                         attachment_filename=f.filename,as_attachment=True)
        
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

