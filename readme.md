# Flask API for App Management & System Info

## Overview
This project provides a Flask-based REST API to manage app details and receive system information from a virtual Android device. It integrates a virtual Android system simulation to send mock device data to the backend and supports TCP/HTTP communication for system data transfer.

## Features
- Add, retrieve, and delete app details
- Receive system information from a simulated Android device
- Uses SQLite as the database
- Establishes TCP or HTTP connection with a server to send system info

## Requirements
- Python 3.x
- Flask
- SQLite3
- Android Emulator (Android Studio)
- ADB (Android Debug Bridge)

## Setup Instructions
### 1. Install Dependencies
Run the following command to install required Python packages:
```sh
pip install flask requests
```

### 2. Initialize the Database
Run the following command to create the database tables:
```sh
sqlite3 app.db < app.sql
```

### 3. Start the API Server
Run the following command:
```sh
python app.py
```
The server will start at `http://127.0.0.1:5000`

## Database Schema (app.sql)
This SQL script creates the necessary tables:
```sql
-- Create the apps table
CREATE TABLE IF NOT EXISTS apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    app_name TEXT NOT NULL,
    version TEXT NOT NULL,
    description TEXT
);

-- Create the devices table to store system information
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT UNIQUE NOT NULL,
    os_version TEXT NOT NULL,
    device_model TEXT NOT NULL,
    available_memory INTEGER NOT NULL,
    storage_available INTEGER NOT NULL
);
```

### Sample Data
```sql
-- Insert sample apps
INSERT INTO apps (app_name, version, description) VALUES
('TestApp1', '1.0', 'First sample app'),
('TestApp2', '2.1', 'Second sample app');

-- Insert sample devices
INSERT INTO devices (device_id, os_version, device_model, available_memory, storage_available) VALUES
('emulator-5554', 'Android 12', 'Pixel 4', 2048, 10000),
('emulator-5556', 'Android 11', 'Pixel 3', 1024, 5000);
```

## API Endpoints
### Add an App (Task 1)
**POST** `/add-app`
#### Request Body (JSON)
```json
{
  "app_name": "TestApp",
  "version": "1.0",
  "description": "Sample app description"
}
```
#### Response
```json
{
  "message": "App added successfully"
}
```

### Get App by ID (Task 1)
**GET** `/get-app/{id}`
#### Response Example
```json
{
  "id": 1,
  "app_name": "TestApp",
  "version": "1.0",
  "description": "Sample app description"
}
```

### Delete an App (Task 1)
**DELETE** `/delete-app/{id}`
#### Response
```json
{
  "message": "App deleted successfully"
}
```

### Send System Info from Android Emulator (Task 4)
**POST** `/send-system-info`
#### Request Body (JSON)
```json
{
  "device_id": "emulator-5554",
  "os_version": "Android 12",
  "device_model": "Pixel 4",
  "available_memory": 2048,
  "storage_available": 10000
}
```
#### Response
```json
{
  "message": "System info received successfully"
}
```

## Virtual Android System Simulation (Task 3 & 4)
This project establishes a connection between the virtual Android system (Android Emulator) and the backend API.

### Steps to Simulate Android System:
1. **Launch Emulator:**
   ```sh
   emulator -avd Pixel_4_API_30
   ```
2. **Install APK (if needed):**
   ```sh
   adb install path/to/sample.apk
   ```
3. **Fetch System Info:**
   ```sh
   adb shell getprop ro.serialno
   adb shell getprop ro.build.version.release
   adb shell getprop ro.product.model
   adb shell dumpsys meminfo | findstr "Free RAM"
   adb shell df /data
   ```
4. **Send System Info to API:**
   ```sh
   curl -X POST http://127.0.0.1:5000/send-system-info \
        -H "Content-Type: application/json" \
        -d '{"device_id": "emulator-5554", "os_version": "Android 12", "device_model": "Pixel 4", "available_memory": 2048, "storage_available": 10000}'
   ```

## Testing the API
You can test the API using `curl` or Postman.

Example:
```sh
curl -X POST http://127.0.0.1:5000/add-app \
     -H "Content-Type: application/json" \
     -d '{"app_name": "TestApp", "version": "1.0", "description": "Sample App"}'
```

## Notes
- Ensure that `app.db` is created before running the API.
- If you face issues, verify that SQLite is installed properly.
- Ensure that the Android Emulator is running before executing ADB commands.

## License
This project is for educational purposes only.

