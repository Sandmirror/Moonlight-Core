import time
import random
import sys

class MirrorsCloudServer:
    """
    Represents the Heavy-Lifting Backend (Mirrors OS).
    It simulates the 'infinite' processing power.
    """
    def __init__(self):
        print("\n[CLOUD] Mirrors OS Kernel Initialized. Waiting for Thin-Film connection...\n")

    def execute_heavy_task(self, compressed_token):
        """
        Simulates receiving a tiny 'Log Scaled' token and expanding it 
        into a complex operation.
        """
        # 1. Expand the 'Virtual Translation Buffer'
        print(f"  [CLOUD] Received Compressed Token: '{compressed_token}'")
        print(f"  [CLOUD] Expanding protocol... (Scaling Factor: 1000x)")
        
        # 2. Simulate Heavy Processing (The part that would overheat a laptop)
        print("  [CLOUD] Allocating virtual cores...", end=" ", flush=True)
        for _ in range(3):
            time.sleep(0.5) # Simulating latency/processing time
            print(".", end=" ", flush=True)
        print(" DONE.")
        
        # 3. Generate a Result
        result_data = f"Rendered Frame Block #{random.randint(1000, 9999)}"
        print(f"  [CLOUD] Task Complete. Compressing result for transmission.\n")
        
        return result_data

class MoonlightClient:
    """
    Represents the 'Thin-Film' Device.
    It has low storage and low power.
    """
    def __init__(self, device_name):
        self.device_name = device_name
        self.battery_level = 99 # Efficiency metric
        print(f"[DEVICE] {self.device_name} powered on. Battery: {self.battery_level}%")

    def request_task(self, server, task_name):
        # 1. Zero-Point Processing: The client does NOT calculate. It only points.
        print(f"[DEVICE] User requested: {task_name}")
        
        # We use a 'Log Scaled' token (a tiny string) to represent a huge task
        protocol_token = f"CMD::{task_name[:3].upper()}::LOG_01" 
        
        print(f"[DEVICE] Transmitting lightweight token: {protocol_token}")
        
        # 2. Send to server
        start_time = time.time()
        result = server.execute_heavy_task(protocol_token)
        end_time = time.time()
        
        # 3. Receive Result
        latency = round((end_time - start_time) * 1000, 2)
        print(f"[DEVICE] Result received: '{result}' in {latency}ms")
        print(f"[DEVICE] Local Storage Used: 0KB. Battery State: Stable at {self.battery_level}%")
        print("-" * 50)

# --- THE SIMULATION ---

if __name__ == "__main__":
    # 1. Initialize the Environment
    cloud_core = MirrorsCloudServer()
    my_thin_film = MoonlightClient("Moonlight_Prototype_v1")

    # 2. Run the Protocol
    # Scenario: The user wants to render a 3D graphic (usually requires a GPU)
    my_thin_film.request_task(cloud_core, "Render_Heavy_3D_Scene")
    
    # Scenario: The user wants to compile a massive code base
    my_thin_film.request_task(cloud_core, "Compile_Linux_Kernel")
    
    print("\n[SYSTEM] Simulation Complete. Zero-Point Architecture Validated.")
