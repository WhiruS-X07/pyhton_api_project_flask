import os
import subprocess
import json
import requests
import time

# Define API endpoint
API_URL = "http://127.0.0.1:5000/send-system-info"

# Path to Android Emulator
EMULATOR_PATH = "C:\\Users\\YourUsername\\AppData\\Local\\Android\\Sdk\\emulator\\emulator.exe"
AVD_NAME = "Pixel_4_API_30"  # Change to match your emulator name

# Function to launch the emulator
def launch_emulator():
    print("Launching Android Emulator...")
    try:
        subprocess.Popen([EMULATOR_PATH, "-avd", AVD_NAME], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(30)  # Wait for emulator to boot
        print("Emulator started successfully.")
    except Exception as e:
        print(f"Error starting emulator: {e}")

# Function to install an APK
def install_apk(apk_path):
    print("Installing APK...")
    try:
        subprocess.run(["adb", "install", apk_path], check=True)
        print("APK installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing APK: {e}")

# Function to retrieve system info from emulator
def get_system_info():
    print("Fetching system information...")
    try:
        # Ensure ADB server is running
        subprocess.run(["adb", "start-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        device_id = subprocess.check_output(["adb", "shell", "getprop", "ro.serialno"]).decode().strip()
        os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode().strip()
        device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()

        # Get available memory correctly using findstr for Windows
        mem_info = subprocess.check_output(["adb", "shell", "dumpsys", "meminfo"]).decode()
        available_memory = [line for line in mem_info.split("\n") if "Free RAM" in line]
        available_memory = available_memory[0].split(":")[1].strip().split(" ")[0] if available_memory else "N/A"

        # Get storage available (in MB)
        storage_output = subprocess.check_output(["adb", "shell", "df", "/data"]).decode().split("\n")[1]
        storage_available = int(storage_output.split()[3]) // 1024  # Convert KB to MB

        system_info = {
            "device_id": device_id,
            "os_version": os_version,
            "device_model": device_model,
            "available_memory": available_memory,
            "storage_available": storage_available
        }

        print("System Info Retrieved:", system_info)
        return system_info
    except Exception as e:
        print(f"Error fetching system info: {e}")
        return None

# Function to send system info to the Flask API
def send_system_info(system_info):
    print("Sending system info to server...")
    try:
        response = requests.post(API_URL, json=system_info)
        if response.status_code == 201:
            print("System info successfully sent.")
            print("Server Response:", response.json())
        else:
            print("Failed to send system info:", response.text)
    except requests.RequestException as e:
        print(f"Error sending system info: {e}")

# Main Execution
if __name__ == "__main__":
    launch_emulator()
    time.sleep(10)  # Ensure emulator is fully started

    sample_apk = "path/to/sample.apk"  # Change this to actual path
    install_apk(sample_apk)

    system_info = get_system_info()
    if system_info:
        send_system_info(system_info)
