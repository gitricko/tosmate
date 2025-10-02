# tosmate

Automate Thinkorswim (ToS) Desktop actions — a small utility to automate the "Scan" button in the Thinkorswim desktop app using image-based GUI automation.

This repository contains a lightweight Python script (`tos_scan_button.py`) and a reference image (`scan_button.png`) used to locate and click the Scan button in the Thinkorswim application. It is primarily tested on macOS; Windows/Linux may work but could need adjustments (screen scaling, image replacement, permission settings).

## Features

- Image-based detection of the Scan button (uses the included `scan_button.png`).
- Simple, single-file script to run from the repository root.
- Minimal dependencies — listed in `requirements.txt`.

## Requirements

- Python 3.8+
- See `requirements.txt` for Python package dependencies (e.g., `pyautogui`, `opencv-python`, etc.).

## Installation

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the repository root:

```bash
python3 tos_scan_button.py
```

Notes:
- Make sure the Thinkorswim desktop app is open and the Scan button is visible on screen when you run the script.
- If your display uses scaling (HiDPI / Retina), the included `scan_button.png` may not match — see Troubleshooting below.

## macOS permissions (important)

On macOS you must grant the running Python process permission to control your computer and capture the screen. Open:

- System Settings → Privacy & Security → Accessibility → add your terminal or Python runtime
- System Settings → Privacy & Security → Screen Recording → add your terminal or Python runtime

After granting permissions, restart the terminal (or the Python process) and try again.

## Troubleshooting

- "Button not found": the screenshot (`scan_button.png`) may not match your UI scale or theme. Take a new screenshot of the Scan button and replace `scan_button.png`.
- Different display resolution / scaling: try running with the display set to 100% scaling or capture a fresh reference image.
- Permission errors on macOS: ensure Accessibility and Screen Recording permissions are granted as noted above.

## Development

- The script is intentionally small. If you add features, include tests and update `requirements.txt` as needed.

## Contributing

Contributions are welcome. Open an issue or a pull request with a short description of the change.

## License

This project includes a `LICENSE` file in the repository root — see that file for the license terms.
