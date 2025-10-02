import pyautogui
import time
import os

# Safety feature: Stop script if mouse moves to screen corner
pyautogui.FAILSAFE = True

# Path to screenshot of the "Scan" button (update with your file path)
SCAN_BUTTON_IMAGE = "scan_button.png"

def click_scan_button():
    # Give time to switch to TOS Scanner tab (adjust as needed)
    print("Switch to Thinkorswim Scanner tab within seconds...")
    time.sleep(1)

    # Verify screenshot exists
    if not os.path.exists(SCAN_BUTTON_IMAGE):
        print(f"Error: Screenshot file '{SCAN_BUTTON_IMAGE}' not found.")
        return

    # Locate the Scan button on screen
    try:
        button_location = pyautogui.locateOnScreen(SCAN_BUTTON_IMAGE, confidence=0.8)
        if button_location:
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center)
            print("Scan button clicked successfully!")
        else:
            print("Scan button not found—check screenshot or TOS window.")
    except pyautogui.ImageNotFoundException:
        print("Error: Could not locate Scan button. Ensure TOS is open and screenshot matches.")

if __name__ == "__main__":
    while True:
        click_scan_button()
        time.sleep(20)  # Wait before next scan (adjust as needed)

