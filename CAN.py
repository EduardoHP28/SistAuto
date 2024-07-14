import can
import struct
from pyvesc import VESCMessage, GetValues

def read_can_messages(channel):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')

    while True:
        message = bus.recv()
        if message.arbitration_id == 0x0001:  # Replace with your specific CAN ID
            data = message.data
            print(f"Received CAN message with ID: {message.arbitration_id} Data: {data}")

            # Decode data if necessary, for example:
            decoded_message = VESCMessage.decode(data)
            if isinstance(decoded_message, GetValues):
                print(f"Temperature: {decoded_message.temp_mos1}")
                print(f"RPM: {decoded_message.rpm}")
                print(f"Current: {decoded_message.current_in}")

# Replace 'can0' with your specific CAN interface
read_can_messages('can0')
