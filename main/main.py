import serial
import time

# Open the serial connection
ser = serial.Serial('/dev/ttyUSB0',  9600, timeout=1)

# Define the command to create the file
command = 'echo "Hello, World!" > /Hello.txt\n'

# Send the command
ser.write(command.encode())

# Wait for the command to complete
time.sleep(1)

# Close the serial connection
ser.close()

