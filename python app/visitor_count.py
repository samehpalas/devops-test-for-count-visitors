from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def initialize_db():
    conn = sqlite3.connect("/app/visitors.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitor_count (
            id INTEGER PRIMARY KEY, 
            count INTEGER NOT NULL
        )
    """)
    cursor.execute("SELECT count FROM visitor_count WHERE id = 1")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO visitor_count (id, count) VALUES (1, 0)")
    conn.commit()
    conn.close()

def increment_visitor_count():
    conn = sqlite3.connect("/app/visitors.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE visitor_count SET count = count + 1 WHERE id = 1")
    conn.commit()
    conn.close()

def get_visitor_count():
    conn = sqlite3.connect("/app/visitors.db")
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM visitor_count WHERE id = 1")
    count = cursor.fetchone()[0]
    conn.close()
    return count

@app.route("/")
def index():
    increment_visitor_count()
    return jsonify({"total_visitors": get_visitor_count()})

if __name__ == "__main__":
    initialize_db()
    app.run(host="0.0.0.0", port=5000)
print("Hello, World!!")
