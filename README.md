# App Management & Android System Info API

## 📌 Overview  
This project is a **Flask-based REST API** that manages app details and collects system information from an **Android Emulator**. It integrates with an SQLite database and supports both HTTP and TCP connections for data transmission.  

## 🚀 Features  
- 📱 **App Management**: Add, retrieve, and delete app details.  
- 📡 **Android System Info**: Collects device ID, OS version, memory, and storage details from a virtual Android device.  
- 🔌 **TCP & HTTP Communication**: Receives data from the emulator and stores it in the database.  
- 🗃️ **SQLite Integration**: Lightweight and efficient database for storing app and device data.  

## 🛠️ Setup Instructions  
### 1️⃣ Install Dependencies  
```sh
pip install flask requests
```  
### 2️⃣ Initialize Database  
```sh
sqlite3 app.db < app.sql
```  
### 3️⃣ Start the API Server  
```sh
python app.py
```  
Server runs at `http://127.0.0.1:5000`  

### 4️⃣ Launch Emulator & Send Data  
Run the script to start the emulator, install an APK, and send system info:  
```sh
python emulator_script.py
```  

## 🔗 API Endpoints  
### 📥 Add an App  
**POST** `/add-app`  
```json
{
  "app_name": "TestApp",
  "version": "1.0",
  "description": "Sample app"
}
```  

### 📤 Get App Details  
**GET** `/get-app/{id}`  

### 🗑️ Delete an App  
**DELETE** `/delete-app/{id}`  

### 📡 Send System Info  
**POST** `/send-system-info`  

## 📌 Notes  
- Ensure **Android Emulator & ADB** are installed for system info collection.  
- Feedback is welcome! Let me know if anything can be improved.  

---  
💡 *Built for learning & exploration. Contributions and suggestions are welcome!* 🚀

