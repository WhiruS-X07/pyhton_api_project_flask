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

-- Insert sample apps
INSERT INTO apps (app_name, version, description) VALUES
('TestApp1', '1.0', 'First sample app'),
('TestApp2', '2.1', 'Second sample app');

-- Insert sample devices
INSERT INTO devices (device_id, os_version, device_model, available_memory, storage_available) VALUES
('emulator-5554', 'Android 12', 'Pixel 4', 2048, 10000),
('emulator-5556', 'Android 11', 'Pixel 3', 1024, 5000);