import json
from flask import Flask, send_from_directory, request, jsonify,send_file
import os
from utils.write import writetofile 
from utils.createzip import create_zip_from_folder 

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'dist')
DATA_FILE = os.path.join(BASE_DIR, 'data1.csv')

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        print(filename,FILES_DIR)
        c=  send_from_directory(FILES_DIR, filename, as_attachment=True)
        print("llll")
        return c
    except Exception as e:
        print(e)
        return jsonify({'error': 'File not found'}), 404
@app.route('/app/download/<filename>', methods=['GET'])
def appdownload_file(filename):
    try:
        zip_io = create_zip_from_folder(FILES_DIR + filename)
        return send_file(
        zip_io,
        as_attachment=True,
        download_name='folder.zip',
        mimetype='application/zip'
    )
    except Exception as e:
        print(e)
        return jsonify({'error': 'File not found'}), 404

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(FILES_DIR)
    return jsonify(files)

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        print(data)
        # writetofile([data],DATA_FILE)
        # with open(DATA_FILE, 'a') as f:
        #     f.write(json.dumps(data) + ',\n')
        return jsonify({'message': 'Data received successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
