import pyautogui
import math
import time
import sys

def move_mouse_in_circle(radius=50, speed=0.01):
    """
    Moves the mouse in a circular pattern.
    
    Args:
        radius (int): Radius of the circle in pixels.
        speed (float): Delay between movements in seconds. Lower is faster/smoother.
    """
    print("Press Ctrl+C to stop.")
    try:
        # Get current position to be the center of the circle initially, 
        # or just start moving around the current position
        center_x, center_y = pyautogui.position()
        angle = 0
        
        while True:
            # Calculate new coordinates
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            # Move the mouse
            pyautogui.moveTo(x, y)
            
            # Increment angle
            angle += 0.1
            if angle >= 2 * math.pi:
                angle = 0
            
            time.sleep(speed)
            
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    # Fail-safe: moving mouse to corner will throw exception
    pyautogui.FAILSAFE = True 
    move_mouse_in_circle()