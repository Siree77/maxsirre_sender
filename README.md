# 📧 Maxsirre Sender

![Maxsirre Sender Banner](https://github.com/Siree77/maxsirre_sender/raw/main/banner.png)

**Maxsirre Sender** is a powerful and user-friendly Python script designed to send bulk emails using SMTP. Whether you're conducting marketing campaigns, sending newsletters, or managing large-scale communications, Maxsirre Sender streamlines the process, making it efficient and secure. 🔥

---

## 🌟 Features

- **🔧 Customizable SMTP Settings**: Easily configure your SMTP server, port, and credentials.
- **📨 Bulk Email Sending**: Send emails to multiple recipients listed in a separate file.
- **🔒 Secure Password Entry**: Passwords are entered securely at runtime to ensure safety.
- **📝 Logging**: Automatically logs the status of sent and failed emails for easy tracking.
- **🎨 Custom Design**: Features a personalized ASCII art banner for a professional look.
- **📄 HTML Email Support**: Send richly formatted HTML emails using a separate `message.html` file.
- **🧠 Basic AI-like Interaction**: Interact with the script using simple commands for an enhanced user experience.
- **📱 Cross-Platform Compatibility**: Run seamlessly on Termux, WSL (Ubuntu), and standard Ubuntu environments.

---

## 📦 Project Structure

maxsirre-sender/ ├── config.json ├── emails.txt ├── maxsirre_sender.py ├── message.html ├── email_status.txt ├── incoming_messages.txt ├── README.md └── .gitignore


---

## 🛠️ Setup

### 📝 Prerequisites

- **Python 3.x** installed on your system. [Download Python](https://www.python.org/downloads/)
- **Git** installed for cloning the repository. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 🔍 Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

2. **Install Dependencies**


**To install the required dependencies, run the following command:**

```bash
pip install -r requirements.txt
```
**This script utilizes only standard Python libraries, so no additional installations are required. However, ensure your Python environment is up-to-date.**

    
    python3 --version
    

**If you don't have Python 3 installed, follow the instructions [here](https://www.python.org/downloads/).**

3. **Configure SMTP Settings**

**- Open `config.json` in your preferred text editor.**
**- Fill in your SMTP details.**
    - **Leave the `password` field empty** to be prompted securely at runtime.
    
**config.json**
```
nano config.json
```
     {
        "smtp_server": "smtp.eample.email",
        "port": 465,
        "from_email": "eample@eample.org",
        "username": "eample@eample.org",
        "password": "",
        "use_tls": true,
        "subject": "TTXV",
        "message": "TTXV text message.",
        "content_type": "html"
    }
    

4. **Prepare the Email List**

    - Open `emails.txt` and add the recipient email addresses, one per line.
```
nano emails.txt
```
    
    
    example1@example.com
    example2@example.com
    

5. **Customize the HTML Message**

    - Open `message.html` and customize the HTML content as desired.
 ```
nano message.html
```
    html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Your Subject Here</title>
        <style>
            /* Add your custom styles here */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333333;
                padding: 20px;
            }
            .container {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                text-align: center;
                padding-bottom: 20px;
            }
            .content {
                line-height: 1.6;
            }
            .footer {
                text-align: center;
                padding-top: 20px;
                font-size: 0.9em;
                color: #777777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to Maxsirre Sender</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p>This is a sample HTML email sent using <strong>Maxsirre Sender</strong>.</p>
                <p>You can customize this message by editing the <code>message.html</code> file.</p>
                <p>Best regards,<br>Maxsirre Sender Team</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Maxsirre Sender. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    

---

## 🚀 Usage

### 🖥️ Running the Script on Different Platforms

#### 📱 Termux (Android)

1. **Install Termux from [Github](https://github.com/termux/termux-app/releases) or [F-Droid](https://f-droid.org/en/packages/com.termux/).**

2. **Update and Install Python**

    ```bash
    pkg update && pkg upgrade
    pkg install python git
    ```

3. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

4. **Run the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

#### 🐧 WSL/Ubuntu

1. **Ensure WSL is Installed**: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

2. **Open Terminal**

3. **Update and Install Git & Python**

    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install git python3 python3-pip -y
    ```

4. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

5. **Run the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

### 💻 Running the Script

1. **Navigate to the Project Directory**

    ```bash
    cd maxsirre-sender
    ```

2. **Execute the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

3. **Interact with the Script**

    - **ASCII Art Banner**: Upon running, you'll see a personalized banner.
    - **Optional Contact Info**: Enter your Telegram handle or any contact information when prompted.
    - **SMTP Password Prompt**: If not set in `config.json`, you'll be prompted to enter it securely.
    - **AI-like Interaction**: Engage with simple commands to control the script.

### 🗣️ Available Commands

- **`hello`**: Greets the user.
- **`help`**: Provides assistance information.
- **`status`**: Reports system status.
- **`send emails`**: Initiates the email sending process.
- **`set smtp`**: Allows updating SMTP settings.
- **`bye`**: Bids farewell.
- **`exit` or `quit`**: Terminates the program.

### 📄 Sample Interaction

```bash
$ python3 maxsirre_sender.py

def print_design():
    print(Fore.CYAN + Style.BRIGHT + "███╗░░░███╗" + Fore.RED + "██████╗░" + Fore.GREEN + "██╗░░░██╗" + Fore.YELLOW + "░█████╗░" + Fore.BLUE + "██████╗░")
    print(Fore.CYAN + "████╗░████║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "██║░░░██║" + Fore.YELLOW + "██╔══██╗" + Fore.BLUE + "██╔══██╗")
    print(Fore.CYAN + "██╔████╔██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "███████║" + Fore.YELLOW + "██║░░██║" + Fore.BLUE + "██╔═██╗░")
    print(Fore.CYAN + "██║╚██╔╝██║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "╚════██║" + Fore.YELLOW + "╚█████╔╝" + Fore.BLUE + "██║░╚██╗")
    print(Fore.CYAN + "██║░╚═╝░██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "░░░░██║" + Fore.YELLOW + "░╚═╝░░░" + Fore.BLUE + "╚██████╔╝")
    print(Fore.CYAN + "╚═╝░░░░░╚═╝" + Fore.RED + "╚═════╝░" + Fore.GREEN + "░░░░╚═╝" + Fore.YELLOW + "░░░░╚═╝" + Fore.BLUE + "░╚═════╝░")
    print(Fore.YELLOW + Style.BRIGHT + "Application: " + Fore.GREEN + "MAXSIR\n" + Style.RESET_ALL)

Creator: Maxsirre Sender

Maxsirre Sender (Optional): @MaxsirreAI
Telegram @Maxsirre Sender: @MaxsirreAI
You: hello
Maxsirre Sender AI: Hello! How can I assist you today?
You: send emails
Sending HTML formatted emails using 'message.html'.

Emails sent successfully: 2
Emails failed to send: 0
Date and time of sending: 2024-04-27 12:34:56.789123

List of successfully sent emails:
| example1@example.com |
| example2@example.com |
List of failed emails:




---

## 🛠️ Setup

### 📝 Prerequisites

- **Python 3.x** installed on your system. [Download Python](https://www.python.org/downloads/)
- **Git** installed for cloning the repository. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 🔍 Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

2. **Install Dependencies**

    This script utilizes only standard Python libraries, so no additional installations are required. However, ensure your Python environment is up-to-date.

    ```bash
    python3 --version
    ```

    If you don't have Python 3 installed, follow the instructions [here](https://www.python.org/downloads/).

3. **Configure SMTP Settings**

    - Open `config.json` in your preferred text editor.
    - Fill in your SMTP details.
    - **Leave the `password` field empty** to be prompted securely at runtime.

    ```json
    {
        "smtp_server": "smtp.titan.email",
        "port": 465,
        "from_email": "support@calkinslawfirm.org",
        "username": "support@calkinslawfirm.org",
        "password": "",
        "use_tls": true,
        "subject": "TTXV",
        "message": "TTXV text message.",
        "content_type": "html"
    }
    ```

4. **Prepare the Email List**

    - Open `emails.txt` and add the recipient email addresses, one per line.

    ```plaintext
    # Add recipient emails, one per line
    example1@example.com
    example2@example.com
    ```

5. **Customize the HTML Message**

    - Open `message.html` and customize the HTML content as desired.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Your Subject Here</title>
        <style>
            /* Add your custom styles here */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333333;
                padding: 20px;
            }
            .container {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                text-align: center;
                padding-bottom: 20px;
            }
            .content {
                line-height: 1.6;
            }
            .footer {
                text-align: center;
                padding-top: 20px;
                font-size: 0.9em;
                color: #777777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to Maxsirre Sender</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p>This is a sample HTML email sent using <strong>Maxsirre Sender</strong>.</p>
                <p>You can customize this message by editing the <code>message.html</code> file.</p>
                <p>Best regards,<br>Maxsirre Sender Team</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Maxsirre Sender. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    ```

---

## 🚀 Usage

### 🖥️ Running the Script on Different Platforms

#### 📱 Termux (Android)

1. **Install Termux from [Github ](https://github.com/termux/termux-app/releases) or [F-Droid](https://f-droid.org/en/packages/com.termux/).**

2. **Update and Install Python**

    ```bash
    pkg update && pkg upgrade
    pkg install python git
    ```

3. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

4. **Run the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

#### 🐧 WSL/Ubuntu

1. **Ensure WSL is Installed**: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

2. **Open Terminal**

3. **Update and Install Git & Python**

    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install git python3 python3-pip -y
    ```

4. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

5. **Run the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

### 💻 Running the Script

1. **Navigate to the Project Directory**

    ```bash
    cd maxsirre-sender
    ```

2. **Execute the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

3. **Interact with the Script**

    - **ASCII Art Banner**: Upon running, you'll see a personalized banner.
    - **Optional Contact Info**: Enter your Telegram handle or any contact information when prompted.
    - **SMTP Password Prompt**: If not set in `config.json`, you'll be prompted to enter it securely.
    - **AI-like Interaction**: Engage with simple commands to control the script.

### 🗣️ Available Commands

- **`hello`**: Greets the user.
- **`help`**: Provides assistance information.
- **`status`**: Reports system status.
- **`send emails`**: Initiates the email sending process.
- **`set smtp`**: Allows updating SMTP settings.
- **`bye`**: Bids farewell.
- **`exit` or `quit`**: Terminates the program.

### 📄 Sample Interaction

```bash
$ python3 maxsirre_sender.py

def print_design():
    print(Fore.CYAN + Style.BRIGHT + "███╗░░░███╗" + Fore.RED + "██████╗░" + Fore.GREEN + "██╗░░░██╗" + Fore.YELLOW + "░█████╗░" + Fore.BLUE + "██████╗░")
    print(Fore.CYAN + "████╗░████║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "██║░░░██║" + Fore.YELLOW + "██╔══██╗" + Fore.BLUE + "██╔══██╗")
    print(Fore.CYAN + "██╔████╔██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "███████║" + Fore.YELLOW + "██║░░██║" + Fore.BLUE + "██╔═██╗░")
    print(Fore.CYAN + "██║╚██╔╝██║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "╚════██║" + Fore.YELLOW + "╚█████╔╝" + Fore.BLUE + "██║░╚██╗")
    print(Fore.CYAN + "██║░╚═╝░██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "░░░░██║" + Fore.YELLOW + "░╚═╝░░░" + Fore.BLUE + "╚██████╔╝")
    print(Fore.CYAN + "╚═╝░░░░░╚═╝" + Fore.RED + "╚═════╝░" + Fore.GREEN + "░░░░╚═╝" + Fore.YELLOW + "░░░░╚═╝" + Fore.BLUE + "░╚═════╝░")
    print(Fore.YELLOW + Style.BRIGHT + "Application: " + Fore.GREEN + "MAXSIR\n" + Style.RESET_ALL)

Creator: Maxsirre Sender

Maxsirre Sender (Optional): @MaxsirreAI
Telegram @Maxsirre Sender: @MaxsirreAI
You: hello
Maxsirre Sender AI: Hello! How can I assist you today?
You: send emails
Sending HTML formatted emails using 'message.html'.

Emails sent successfully: 2
Emails failed to send: 0
Date and time of sending: 2024-04-27 12:34:56.789123

List of successfully sent emails:
| example1@example.com |
| example2@example.com |
List of failed emails:




---

## 🛠️ Setup

### 📝 Prerequisites

- **Python 3.x** installed on your system. [Download Python](https://www.python.org/downloads/)
- **Git** installed for cloning the repository. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### 🔍 Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

2. **Install Dependencies**

    This script utilizes only standard Python libraries, so no additional installations are required. However, ensure your Python environment is up-to-date.

    ```bash
    python3 --version
    ```

    If you don't have Python 3 installed, follow the instructions [here](https://www.python.org/downloads/).

3. **Configure SMTP Settings**

    - Open `config.json` in your preferred text editor.
    - Fill in your SMTP details.
    - **Leave the `password` field empty** to be prompted securely at runtime.

    ```json
    {
        "smtp_server": "SMTP server",
        "port": 465,
        "from_email": "sameasusername enail",
        "username": "username email",
        "password": "",
        "use_tls": true,
        "subject": "TTXV",
        "message": "TTXV text message.",
        "content_type": "html"
    }
    ```

4. **Prepare the Email List**

    - Open `emails.txt` and add the recipient email addresses, one per line.

    ```plaintext
    # Add recipient emails, one per line
    example1@example.com
    example2@example.com
    ```

5. **Customize the HTML Message**

    - Open `message.html` and customize the HTML content as desired.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Your Subject Here</title>
        <style>
            /* Add your custom styles here */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333333;
                padding: 20px;
            }
            .container {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
                text-align: center;
                padding-bottom: 20px;
            }
            .content {
                line-height: 1.6;
            }
            .footer {
                text-align: center;
                padding-top: 20px;
                font-size: 0.9em;
                color: #777777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to Maxsirre Sender</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p>This is a sample HTML email sent using <strong>Maxsirre Sender</strong>.</p>
                <p>You can customize this message by editing the <code>message.html</code> file.</p>
                <p>Best regards,<br>Maxsirre Sender Team</p>
            </div>
            <div class="footer">
                <p>&copy; 2024 Maxsirre Sender. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    ```

---

## 🚀 Usage

### 🖥️ Running the Script on Different Platforms

#### 📱 Termux (Android)

1. **Install Termux from [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/en/packages/com.termux/).**

2. **Update and Install Python**

    ```bash
    pkg update && pkg upgrade
    pkg install python git
    ```

3. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

4. **Run the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

#### 🐧 WSL/Ubuntu

1. **Ensure WSL is Installed**: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

2. **Open Terminal**

3. **Update and Install Git & Python**

    ```bash
    sudo apt update && sudo apt upgrade -y
    sudo apt install git python3 python3-pip -y
    ```

4. **Clone the Repository**

    ```bash
    git clone https://github.com/Siree77/maxsirre_sender.git
    cd maxsirre-sender
    ```

5. **Run the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

### 💻 Running the Script

1. **Navigate to the Project Directory**

    ```bash
    cd maxsirre-sender
    ```

2. **Execute the Script**

    ```bash
    python3 maxsirre_sender.py
    ```

3. **Interact with the Script**

    - **ASCII Art Banner**: Upon running, you'll see a personalized banner.
    - **Optional Contact Info**: Enter your Telegram handle or any contact information when prompted.
    - **SMTP Password Prompt**: If not set in `config.json`, you'll be prompted to enter it securely.
    - **AI-like Interaction**: Engage with simple commands to control the script.

### 🗣️ Available Commands

- **`hello`**: Greets the user.
- **`help`**: Provides assistance information.
- **`status`**: Reports system status.
- **`send emails`**: Initiates the email sending process.
- **`set smtp`**: Allows updating SMTP settings.
- **`bye`**: Bids farewell.
- **`exit` or `quit`**: Terminates the program.

### 📄 Sample Interaction

```bash
$ python3 maxsirre_sender.py

def print_design():
    print(Fore.CYAN + Style.BRIGHT + "███╗░░░███╗" + Fore.RED + "██████╗░" + Fore.GREEN + "██╗░░░██╗" + Fore.YELLOW + "░█████╗░" + Fore.BLUE + "██████╗░")
    print(Fore.CYAN + "████╗░████║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "██║░░░██║" + Fore.YELLOW + "██╔══██╗" + Fore.BLUE + "██╔══██╗")
    print(Fore.CYAN + "██╔████╔██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "███████║" + Fore.YELLOW + "██║░░██║" + Fore.BLUE + "██╔═██╗░")
    print(Fore.CYAN + "██║╚██╔╝██║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "╚════██║" + Fore.YELLOW + "╚█████╔╝" + Fore.BLUE + "██║░╚██╗")
    print(Fore.CYAN + "██║░╚═╝░██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "░░░░██║" + Fore.YELLOW + "░╚═╝░░░" + Fore.BLUE + "╚██████╔╝")
    print(Fore.CYAN + "╚═╝░░░░░╚═╝" + Fore.RED + "╚═════╝░" + Fore.GREEN + "░░░░╚═╝" + Fore.YELLOW + "░░░░╚═╝" + Fore.BLUE + "░╚═════╝░")
    print(Fore.YELLOW + Style.BRIGHT + "Application: " + Fore.GREEN + "MAXSIR\n" + Style.RESET_ALL)

Creator: Maxsirre Sender

Maxsirre Sender (Optional): @MaxsirreAI
Telegram @Maxsirre Sender: @MaxsirreAI
You: hello
Maxsirre Sender AI: Hello! How can I assist you today?
You: send emails
Sending HTML formatted emails using 'message.html'.

Emails sent successfully: 2
Emails failed to send: 0
Date and time of sending: 2024-04-27 12:34:56.789123

List of successfully sent emails:
| example1@example.com |
| example2@example.com |
List of failed emails:
📂 File Descriptions
config.json: Stores SMTP configuration settings. Users can update SMTP details directly or use the in-script prompt.

{
    "smtp_server": "smtp.titan.email",
    "port": 465,
    "from_email": "support@calkinslawfirm.org",
    "username": "support@calkinslawfirm.org",
    "password": "",
    "use_tls": true,
    "subject": "TTXV",
    "message": "TTXV text message.",
    "content_type": "html"
}


emails.txt: Contains the list of recipient email addresses, one per line.

# Add recipient emails, one per line
example1@example.com
example2@example.com


maxsirre_sender.py: The main Python script responsible for sending emails. Includes advanced terminal design, HTML support, and AI-like interactions.

message.html: Contains the HTML-formatted email message. Users can customize this file with their desired HTML content.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Your Subject Here</title>
    <style>
        /* Add your custom styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333333;
            padding: 20px;
        }
        .container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        .content {
            line-height: 1.6;
        }
        .footer {
            text-align: center;
            padding-top: 20px;
            font-size: 0.9em;
            color: #777777;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Welcome to Maxsirre Sender</h1>
        </div>
        <div class="content">
            <p>Hello,</p>
            <p>This is a sample HTML email sent using <strong>Maxsirre Sender</strong>.</p>
            <p>You can customize this message by editing the <code>message.html</code> file.</p>
            <p>Best regards,<br>Maxsirre Sender Team</p>
        </div>
        <div class="footer">
            <p>&copy; 2024 Maxsirre Sender. All rights reserved.</p>
        </div>
    </div>
</body>
</html>


email_status.txt: Logs the status of sent and failed emails. Automatically updated by the script.

# Email Status Log
# All sent and failed email logs will be recorded below.


incoming_messages.txt: Logs all incoming messages and interactions with the script for auditing and tracking purposes.

# Incoming Messages Log
# All user interactions and system messages will be recorded below.


.gitignore: Ensures sensitive files are not tracked by Git.

# Ignore configuration files
config.json

# Ignore email status and incoming messages
email_status.txt
incoming_messages.txt

# Ignore HTML message file if desired
# message.html

# Ignore Python cache
__pycache__/
*.pyc

🛡️ Security Considerations
🔒 Password Handling: The SMTP password is not stored in plain text within config.json. Instead, the script prompts users to enter it securely at runtime using the getpass module.

🚫 Sensitive Files Ignored: Ensure that sensitive files like config.json, email_status.txt, and incoming_messages.txt are included in your .gitignore to prevent accidental exposure when uploading to GitHub.

📝 Contributing
Contributions are welcome! Whether it's adding new features, improving documentation, or fixing bugs, your contributions help make Maxsirre Sender better for everyone. 🙌

Fork the Repository

Create a New Branch

git checkout -b feature/YourFeatureName


Commit Your Changes


git commit -m "Add your message here"
Push to the Branch


git push origin feature/YourFeatureName
Open a Pull Request

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📞 Contact
Creator: Maxsirre Sender
Telegram: @MaxsirreAI88

Feel free to reach out for any questions, feedback, or support!

🌐 Acknowledgements
Inspired by various bulk email sending tools and Python's smtplib.
Special thanks to the open-source community for providing invaluable resources and libraries.
🛠️ Additional Enhancements
To further enhance Maxsirre Sender, consider implementing the following features:

🖥️ GUI Interface: Integrate a graphical user interface using libraries like Tkinter or PyQt for a more user-friendly experience.
📎 Attachments: Enable sending attachments with emails by extending the send_email function.
🤖 Advanced AI Features: Integrate with AI APIs (e.g., OpenAI's GPT) for more dynamic and intelligent interactions.
⏰ Scheduling: Add functionality to schedule emails to be sent at specific times.
🔍 Validation: Implement email validation to ensure that all recipient addresses are in the correct format before attempting to send.
🔗 Useful Links
Python Official Documentation
GitHub Guides
SMTP Servers and Ports
Termux Documentation
WSL Installation Guide
Thank you for choosing Maxsirre Sender! We hope this tool simplifies your bulk email sending needs and enhances your productivity. Happy emailing! 📧✨

