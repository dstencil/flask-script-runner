from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_script():
    # Check if file is uploaded
    if 'file' not in request.files:
        return render_template('index.html', message='No file uploaded.')

    file = request.files['file']

    # Check if file has a valid filename
    if file.filename == '':
        return render_template('index.html', message='No file selected.')

    # Save file to a temporary directory
    file_path = os.path.join('temp', file.filename)
    file.save(file_path)

    # Run the Python script using subprocess
    try:
        result = subprocess.check_output(['python', file_path], stderr=subprocess.STDOUT, timeout=10)
        return render_template('index.html', message='Script executed successfully:\n' + result.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        return render_template('index.html', message='Script execution failed:\n' + e.output.decode('utf-8'))
    except subprocess.TimeoutExpired:
        return render_template('index.html', message='Script execution timed out.')

if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.makedirs('temp')
    app.run(debug=True)
