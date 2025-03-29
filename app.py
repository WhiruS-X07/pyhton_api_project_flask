from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

# --------------------- TASK 1: APP MANAGEMENT ---------------------

# Endpoint: Add an app to the database
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    if not all(key in data for key in ["app_name", "version", "description"]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)",
                       (data['app_name'], data['version'], data['description']))
        conn.commit()
        conn.close()
        return jsonify({"message": "App added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get app by ID
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM apps WHERE id = ?", (id,))
    app = cursor.fetchone()
    conn.close()

    if app:
        return jsonify(dict(app))
    return jsonify({"error": "App not found"}), 404

# Endpoint: Delete app by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM apps WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "App deleted successfully"})

# --------------------- TASK 4: SYSTEM INFO ---------------------

# Endpoint: Receive system info from Android Emulator
@app.route('/send-system-info', methods=['POST'])
def send_system_info():
    data = request.get_json()

    # Validate required fields
    required_fields = ["device_id", "os_version", "device_model", "available_memory", "storage_available"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Insert or update system info if device_id already exists
        cursor.execute("""
            INSERT INTO devices (device_id, os_version, device_model, available_memory, storage_available)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(device_id) DO UPDATE SET
                os_version = excluded.os_version,
                device_model = excluded.device_model,
                available_memory = excluded.available_memory,
                storage_available = excluded.storage_available
        """, (data['device_id'], data['os_version'], data['device_model'], data['available_memory'], data['storage_available']))

        conn.commit()
        conn.close()
        return jsonify({"message": "System info received successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
