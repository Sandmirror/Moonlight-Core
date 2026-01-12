import winsound
import threading
import functools
import time

# --- THE MOONLIT SCALE (Hz) ---
# These frequencies are chosen for their specific vibratory qualities.
FREQ_ROOT   = 174  # Foundation / Grounding (Database & Storage)
FREQ_SACRAL = 417  # Clearing / Undoing (Error Handling)
FREQ_HEART  = 528  # Transformation / Miracles (Network Handshake)
FREQ_CROWN  = 963  # Awakening / Spirit (System Boot)
FREQ_PURE   = 111  # The "Bell" (Simple function calls)

def play_tone(hz, duration=400):
    """
    Plays the sound in a separate thread ("The Spirit") 
    so it does not stop the code ("The Body").
    """
    def _tone():
        try:
            # The actual sound generation
            winsound.Beep(hz, duration) 
        except Exception:
            pass 
    
    # Detach the sound from the logic
    t = threading.Thread(target=_tone)
    t.start()

def resonate(hz):
    """
    The Decorator. 
    Wraps any function in a protective vibration.
    """
    def decorator_ring(func):
        @functools.wraps(func)
        def wrapper_bell(*args, **kwargs):
            # 1. The Bell Tolls
            play_tone(hz)
            time.sleep(0.1) # A tiny pause to let the sound breathe
            
            # 2. The Action Happens
            return func(*args, **kwargs)
        return wrapper_bell
    return decorator_ring
