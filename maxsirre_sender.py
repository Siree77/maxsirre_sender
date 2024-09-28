import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import json
import os
import sys
import time
import getpass
import socket
from colorama import Fore, Style, init
import random

# Initialize colorama to filter ANSI codes on Windows and reset styles
init(autoreset=True)

# Matrix-style animation
def matrix_animation(duration=5):
    os.system('cls' if os.name == 'nt' else 'clear')
    columns = os.get_terminal_size().columns
    end_time = time.time() + duration
    chars = ['0', '1']
    while time.time() < end_time:
        row = ''.join([random.choice(chars) for _ in range(columns)])
        print(Fore.GREEN + row)
        time.sleep(0.05)

# Function to display enhanced ASCII art design with colors for MAXSIR
def print_design():
    print(Fore.CYAN + Style.BRIGHT + "███╗░░░███╗" + Fore.RED + "██████╗░" + Fore.GREEN + "██╗░░░██╗" + Fore.YELLOW + "░█████╗░" + Fore.BLUE + "██████╗░")
    print(Fore.CYAN + "████╗░████║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "██║░░░██║" + Fore.YELLOW + "██╔══██╗" + Fore.BLUE + "██╔══██╗")
    print(Fore.CYAN + "██╔████╔██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "███████║" + Fore.YELLOW + "██║░░██║" + Fore.BLUE + "██╔═██╗░")
    print(Fore.CYAN + "██║╚██╔╝██║" + Fore.RED + "██╔══██╗" + Fore.GREEN + "╚════██║" + Fore.YELLOW + "╚█████╔╝" + Fore.BLUE + "██║░╚██╗")
    print(Fore.CYAN + "██║░╚═╝░██║" + Fore.RED + "██████╦╝" + Fore.GREEN + "░░░░██║" + Fore.YELLOW + "░╚═╝░░░" + Fore.BLUE + "╚██████╔╝")
    print(Fore.CYAN + "╚═╝░░░░░╚═╝" + Fore.RED + "╚═════╝░" + Fore.GREEN + "░░░░╚═╝" + Fore.YELLOW + "░░░░╚═╝" + Fore.BLUE + "░╚═════╝░")
    print(Fore.YELLOW + Style.BRIGHT + "Application: " + Fore.GREEN + "MAXSIR\n" + Style.RESET_ALL)

# Function to simulate loading animations
def loading_animation(message="Loading", duration=2):
    print(Fore.CYAN + message, end="", flush=True)
    for _ in range(duration * 5):
        time.sleep(0.1)
        print(Fore.CYAN + ".", end="", flush=True)
    print(Fore.CYAN + " Done!")

# Function to simulate a more advanced progress bar for sending emails
def progress_bar(total_emails):
    print(Fore.GREEN + "\nSending emails...")
    for i in range(total_emails):
        time.sleep(0.2)  # Simulate email sending delay
        percentage = int(((i + 1) / total_emails) * 100)
        sys.stdout.write(Fore.RED + f'█ {percentage}%')
        sys.stdout.flush()
        sys.stdout.write('\r')
    print(Fore.GREEN + "\n\nAll emails sent successfully!\n")

# Load SMTP configuration from a JSON file with loading animation
def load_config(config_path="config.json"):
    loading_animation("Loading configuration")
    if not os.path.exists(config_path):
        print(Fore.RED + f"Configuration file '{config_path}' not found.")
        exit(1)
    with open(config_path, "r") as file:
        config = json.load(file)
    return config

# Display real-time SMTP connection log and speed
def smtp_connection_log(smtp_server, port, start_time):
    try:
        # Resolve the SMTP server address to get the IP
        server_ip = socket.gethostbyname(smtp_server)
        connection_time = time.time() - start_time
        print(Fore.CYAN + f"Connected to SMTP server: {smtp_server} [{server_ip}]")
        print(Fore.GREEN + f"Connection established in {connection_time:.2f} seconds.")
    except socket.error as err:
        print(Fore.RED + f"Failed to resolve SMTP server {smtp_server}: {err}")

# Function to send emails based on user-selected format
def send_email(config, emails, message, content_type):
    smtp_server = config['smtp_server']
    port = config['port']
    from_email = config['from_email']
    username = config.get('username')
    password = config.get('password')
    use_tls = config['use_tls']
    
    try:
        start_time = time.time()
        print(Fore.CYAN + f"\nConnecting to SMTP server ({smtp_server})...")
        
        # Connect to the SMTP server
        server = smtplib.SMTP_SSL(smtp_server, port) if use_tls else smtplib.SMTP(smtp_server, port)
        smtp_connection_log(smtp_server, port, start_time)

        # Log in to the server
        server.login(username, password)
        print(Fore.CYAN + f"Logged in as {username}\n")
        
        # Send each email and log the results in real-time
        success_count = 0
        fail_count = 0
        for i, to_email in enumerate(emails, start=1):
            try:
                msg = MIMEMultipart("alternative")
                msg['Subject'] = config.get("subject", "No Subject")
                msg['From'] = from_email
                msg['To'] = to_email
                msg.attach(MIMEText(message, content_type))
                
                send_start = time.time()
                server.send_message(msg)
                send_time = time.time() - send_start
                print(Fore.GREEN + f"({i}/{len(emails)}) Email sent to {to_email} in {send_time:.2f} seconds.")
                success_count += 1
            except Exception as e:
                print(Fore.RED + f"Failed to send email to {to_email}: {str(e)}")
                fail_count += 1

        server.quit()
    except Exception as e:
        print(Fore.RED + f"Failed to connect to SMTP server: {str(e)}")
        return

    print(Fore.GREEN + f"\nTotal emails sent successfully: {success_count}")
    if fail_count:
        print(Fore.RED + f"Failed to send {fail_count} emails.")


def main_menu():
    while True:
        print(Fore.YELLOW + "\nMain Menu")
        print(Fore.GREEN + "1. Send Emails")
        print(Fore.RED + "2. Exit")
        choice = input(Fore.CYAN + "\nChoose an option: ")
        
        if choice == '1':
            main()
        elif choice == '2':
            print(Fore.YELLOW + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            

def main():
    matrix_animation()  # Show matrix animation when starting
    print_design()

    config = load_config()

    if not config.get("password"):
        config["password"] = getpass.getpass(prompt=Fore.YELLOW + "Enter your SMTP password: ")

    emails_file = "emails.txt"
    loading_animation("Reading email list")
    if not os.path.exists(emails_file):
        print(Fore.RED + "Emails file not found.")
        exit(1)
    with open(emails_file, "r") as file:
        emails = [email.strip() for email in file if email.strip()]

    print(Fore.YELLOW + Style.BRIGHT + "Choose the format for sending emails:")
    print(Fore.GREEN + "1. Send HTML email")
    print(Fore.CYAN + "2. Send Plain Text email")
    choice = input(Fore.YELLOW + "Enter your choice (1/2): ")

    if choice == '1':
        loading_animation("Loading HTML message")
        with open('message.html', 'r') as html_file:
            message = html_file.read()
        content_type = 'html'
    elif choice == '2':
        message = config.get("message", "")
        content_type = 'plain'
    else:
        print(Fore.RED + "Invalid choice, returning to main menu.")
        return

    send_email(config, emails, message, content_type)
    # Add this instruction to display after the emails are sent:
    print(Fore.YELLOW + "\nPress CTRL + C to cancel or close the terminal.")

    print(Fore.YELLOW + "\nReturning to Main Menu...")
    time.sleep(2)
    main_menu()

if __name__ == "__main__":
    main_menu()
