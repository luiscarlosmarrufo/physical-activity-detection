#------------------------------------------------------------------------------------------------------------------
#   Communication test for receiving sensor data from a mobile device
#------------------------------------------------------------------------------------------------------------------
import requests
import time

# IP address and command for the mobile device running Phyphox
IP_ADDRESS = '10.43.98.215'         # Replace with your device's IP address
COMMAND_ACC = 'accX&accY&accZ&acc_time'     # Command to fetch acceleration data
COMMAND_GYRO = 'gyroX&gyroY&gyroZ&gyro_time' # Command to fetch gyroscope data
ACC_URL = "http://{}/get?{}".format(IP_ADDRESS, COMMAND_ACC)
GYRO_URL = "http://{}/get?{}".format(IP_ADDRESS, COMMAND_GYRO)

# Function to fetch sensor data from the mobile device
def get_sensor_data():
    try:
        response = requests.get(ACC_URL, timeout=1)
        response.raise_for_status()
        data_a = response.json()
        
        response = requests.get(GYRO_URL, timeout=1)
        response.raise_for_status()
        data_g = response.json()

        accX = data_a["buffer"]["accX"]["buffer"][0]
        accY = data_a["buffer"]["accY"]["buffer"][0]
        accZ = data_a["buffer"]["accZ"]["buffer"][0]
        timestamp_a = data_a["buffer"]["acc_time"]["buffer"][0]
        
        gyroX = data_g["buffer"]["gyroX"]["buffer"][0]
        gyroY = data_g["buffer"]["gyroY"]["buffer"][0]
        gyroZ = data_g["buffer"]["gyroZ"]["buffer"][0]
        timestamp_g = data_g["buffer"]["gyro_time"]["buffer"][0]

        return {
            "time_a": timestamp_a,
            "x_a": accX,
            "y_a": accY,
            "z_a": accZ,
            "time_g": timestamp_g,
            "x_g": gyroX,
            "y_g": gyroY,
            "z_g": gyroZ
        }

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Main loop to continuously fetch and print sensor data
samp_rate = 5000
print("Reading real-time data from Phyphox...\nPress Ctrl+C to stop.")
try:
    while True:
        data = get_sensor_data()
        if data and data['time_a'] and data['time_g']:
            print(f"t_a = {data['time_a']:.3f}s | accX = {data['x_a']:.4f}, accY = {data['y_a']:.4f}, accZ = {data['z_a']:.4f}")
            print(f"t_g = {data['time_b']:.3f}s | gyroX = {data['x_g']:.4f}, gyroY = {data['y_g']:.4f}, gyroZ = {data['z_g']:.4f}")        
        time.sleep(1./samp_rate) 
except KeyboardInterrupt:
    print("\nReading stopped by user.")

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------