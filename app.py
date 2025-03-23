from flask import Flask, render_template, request, redirect, flash
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flash messages

dic = {0 : 'Real', 1 : 'A.I.'}

model = load_model('model.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(128,128))
	i = image.img_to_array(i)/255.0
	i = np.expand_dims(i, axis=0)
	i = i.reshape(1, 128,128,3)
	p = (model.predict(i) > 0.5).astype("int32")  # Convert probability to 0 or 1
	return dic[int(p[0, 0])]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

# @app.route("/about")
# def about_page():
# 	return "Hello World!"

@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        
        # Check if a file was uploaded
        if "my_image" not in request.files or request.files["my_image"].filename == "":
            flash("⚠️ Please upload an image before submitting!")
            return redirect(request.url)

        img = request.files['my_image']
        img_path = "static/" + img.filename

        try:
            img.save(img_path)  # Save the uploaded file
            p = predict_label(img_path)  # Make prediction
        except PermissionError:
            flash("❌ Permission error! Unable to save the file.")
            return redirect(request.url)

        return render_template("index.html", prediction=p, img_path=img_path)

    return render_template("index.html")


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)