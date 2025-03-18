from flask import Flask, jsonify
import sqlite3
>>>>>>> 8f40ebdafbba60b9f29793c9b6a7e774e07c155d

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
