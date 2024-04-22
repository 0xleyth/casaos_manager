#!/usr/bin/env python3
import argparse
import subprocess
import os

def run_command(command):
    """Executes a system command with subprocess and captures errors."""
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e.stderr.decode()}")
        return False

def update_casaos():
    """Updates CasaOS using the curl command"""
    print("Updating CasaOS...")
    if run_command('curl -fsSL https://get.casaos.io/update | sudo bash'):
        print("CasaOS updated successfully.")
    else:
        print("Failed to update CasaOS.")

def reset_username_password():
    """Resets username and password by backing up the user.db and restarting the service."""
    file_path = '/var/lib/casaos/db/user.db'
    
    if os.path.exists(file_path):
        print("Backing up user.db...")
        if run_command('sudo mv /var/lib/casaos/db/user.db /var/lib/casaos/db/user.db.backup'):
            print("user.db backed up successfully.")
            print("Restarting CasaOS user service...")
            if run_command('sudo systemctl restart casaos-user-service.service'):
                print("Service restarted successfully.")
            else:
                print("Failed to restart CasaOS user service.")
        else:
            print("Failed to backup user.db.")
    else:
        print("Error: user.db does not exist. Cannot reset username and password.")

def reinstall_casaos():
    """Reinstalls CasaOS by first uninstalling it and then installing it again"""
    print("Reinstalling CasaOS...")
    print("Uninstalling CasaOS...")
    if run_command('sudo casaos-uninstall'):
        print("CasaOS uninstalled successfully. Installing CasaOS...")
        if run_command('curl -fsSL https://get.casaos.io | sudo bash'):
            print("CasaOS installed successfully.")
        else:
            print("Failed to install CasaOS.")
    else:
        print("Failed to uninstall CasaOS.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Manage CasaOS installation.")
    parser.add_argument('action', choices=['update', 'reset-username-password', 'reinstall'], help='Action to perform on CasaOS')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.action == 'update':
        update_casaos()
    elif args.action == 'reset-username-password':
        reset_username_password()
    elif args.action == 'reinstall':
        reinstall_casaos()

if __name__ == "__main__":
    main()