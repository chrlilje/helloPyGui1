import serial
import serial.tools.list_ports
import time

BAUD_RATE = 9600
TARGET_ID = "FOOT_PEDAL"

def run_test():
    print("--- Serial Troubleshooting Tool ---")
    ports = list(serial.tools.list_ports.comports())
    
    if not ports:
        print("Error: No serial ports detected at all. Check USB connection.")
        return

    for p in ports:
        print(f"\nTesting Port: {p.device}")
        print(f"Description: {p.description}")
        
        try:
            # Open with a 2-second timeout
            with serial.Serial(p.device, BAUD_RATE, timeout=2) as ser:
                print(f"Successfully opened {p.device}. Waiting for data...")
                
                # Give the Arduino 2 seconds to reboot after opening the port
                time.sleep(2)
                
                # Try to read 5 lines to see what's coming in
                for i in range(5):
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        print(f"  [READ {i+1}]: {line}")
                        if TARGET_ID in line:
                            print(f"  >>> SUCCESS: Found ID '{TARGET_ID}' on {p.device}!")
                    else:
                        print(f"  [READ {i+1}]: ...silence (no data)...")
                
        except Exception as e:
            print(f"  [ERROR]: Could not open port: {e}")

if __name__ == "__main__":
    run_test()