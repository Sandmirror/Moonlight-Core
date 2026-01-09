import time

# --- THE GEOMETAPHYSICAL LOGIC ---

def trigger_action(input_code):
    print(f"\nScanning Input: {input_code}...")
    
    if input_code == "1":
        action_one()
    elif input_code == "2":
        action_two()
    elif input_code == "3":
        action_three()
    else:
        print(f"❌ Input '{input_code}' has no resonance map.")

def action_one():
    print("--------------------------------")
    print("✨ [ACTION 1] Whisper Boot Triggered")
    print("   >> System: Awake.")
    print("--------------------------------")

def action_two():
    print("--------------------------------")
    print("🫁 [ACTION 2] 8-bit Lung Pulse")
    print("   >> Inhale...")
    time.sleep(1) # Short pause
    print("   >> Exhale...")
    print("--------------------------------")

def action_three():
    print("--------------------------------")
    print("☁️ [ACTION 3] Cloud Config Fetch")
    print("   >> Connecting to Mirrors OS...")
    print("   >> Config Loaded.")
    print("--------------------------------")

# --- THE EXECUTION (One Shot) ---

def main():
    print("🔰 MOONLIGHT SINGLE TEST 🔰")
    
    # We ask only ONCE, so the screen doesn't get blocked.
    user_input = input("Enter Resonance (1, 2, or 3): ")
    
    trigger_action(user_input)
    
    print("\n[Simulation Complete]")

if __name__ == "__main__":
    main()
