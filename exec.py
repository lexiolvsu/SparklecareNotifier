import requests
import os
import time

# URL of the script to run
script_url = 'https://raw.githubusercontent.com/lexiolvsu/SparklecareNotifier/main/main.py'

# Path to save the script locally
script_file = 'main.py'

print("SparklecareNotifier")
print("Made by github.com/lexiolvsu")
print("-")
print("-")
# Function to download the script from the URL
def download_script():
    response = requests.get(script_url)
    if response.status_code == 200:
        with open(script_file, 'w') as file:
            file.write(response.text)
        return True
    return False

# Function to check if the script has been updated
def is_updated():
    response = requests.head(script_url)
    last_modified = response.headers.get('Last-Modified')
    if last_modified:
        if os.path.exists(script_file):
            file_stats = os.stat(script_file)
            local_modified = time.ctime(file_stats.st_mtime)
            if last_modified != local_modified:
                return True
        else:
            return True
    return False

# Main script execution loop
while True:
    if is_updated() or not os.path.exists(script_file):
        if download_script():
            print("Script updated. Restarting...")
            # Add any additional command line arguments for the script here
            os.system('python {}'.format(script_file))
        else:
            print("Failed to download the script.")
    time.sleep(60)  # Check for updates every 60 seconds
