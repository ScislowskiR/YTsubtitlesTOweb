import os
from flask import Flask, render_template, request, jsonify

app = Flask('siema')

@app.route('/')
def homepage():
    # Get the list of files in /folders
    folder_path = r'D:\pythonProject\YTsubtitlesTOweb\YTsubtitlesTOjson\folders'  # Adjust this path as needed
    folders = os.listdir(folder_path)
    # print(folders)
    # Pass the list of files to the template
    return render_template("index.html", len=len(folders), folders=folders)

@app.route('/get_files', methods=['POST'])
def get_files():
    folder = request.form.get('folder')
    folder_path = os.path.join(r'D:\pythonProject\YTsubtitlesTOweb\YTsubtitlesTOjson\folders', folder)
    files = os.listdir(folder_path)
    return jsonify(files)

@app.route('/get_file_content', methods=['POST'])
def get_file_content():
    folder = request.form.get('folder')
    file = request.form.get('file')
    file_path = os.path.join(r'D:\pythonProject\YTsubtitlesTOweb\YTsubtitlesTOjson\folders', folder, file)
    with open(file_path, 'r') as f:
        content = f.read()
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)