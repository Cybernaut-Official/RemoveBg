# imports
from flask import Flask, request, render_template, send_file, redirect
from rembg import remove
import tempfile

#initialization of the application
app = Flask(__name__)

# this function will work when when the user opens: 127.0.0.1:8000
# this function returns index.html
@app.route('/')
def index():
    return render_template('index.html')

#when the user clicks on submit button this function will run
@app.route('/remove_bg' , methods=['POST'])
def remove_background():

    #getting the file from request.files and storing it in a variable called file
    file = request.files['image']
    
    #file.read() reads the content of the file object file and returns it as binary data. This binary data can then be processed or saved as needed.
    image_data = file.read()

    #written a condition, where first the code block in try will be executed
    try:
        #the code below basically returns removes the image backgroud using remove function and returns it as a png file as output
        result_image = remove(image_data)
        temp_image = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_image.write(result_image)
        temp_image.close()
        return send_file(temp_image.name, as_attachment=True)
    #if any error occurs in try this part will get executed
    except Exception as e:
        return str(e)
    

       
#this part helps the code to run
if __name__ == "__main__":
    app.run(debug=True)
