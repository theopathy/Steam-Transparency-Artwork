from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("upload.html")
    
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    for upload in request.files.getlist("file"):
        print("LOG: filename: {}".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("LOG: Accept incoming file:", filename)
        print ("LOG: Save it to:", destination)
        upload.save(destination)

    return render_template("display_image.html", image_name=filename)
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

