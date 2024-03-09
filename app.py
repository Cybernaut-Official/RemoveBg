from flask import Flask, request, render_template, send_file
from rembg import remove
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return render_template('index.html', error='No image provided')
    
    file = request.files['image']
    if file.filename == '':
        return render_template('index.html', error='No selected file')

    # Read the image file
    image_data = file.read()

    try:
        # Remove background using rembg
        result_image = remove(image_data)


        temp_image = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_image.write(result_image)
        temp_image.close()

        # Send the file as a response with the appropriate headers
        return send_file(temp_image.name, as_attachment=True)
    except Exception as e:
        # Handle any errors
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
