import requests
from bs4 import BeautifulSoup
import hashlib
import time
from win10toast import ToastNotifier

# URL of the webpage to monitor
url = 'http://sparklecarehospital.com'

# Initialize the notification object
toaster = ToastNotifier()

# Variable to store the hash of the previous content
previous_hash = None

while True:
    # Send a request to the webpage
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the div element with class "latest"
    latest_div = soup.find('div', {'class': 'latest'})
    
    # Calculate the hash of the current content
    current_hash = hashlib.sha256(latest_div.encode()).hexdigest()
    
    # Check if the content has changed
    if current_hash != previous_hash:
        # Create a notification
        toaster.show_toast("New Sparklecare Update!",
                           "The main page now indicates a new update!",
                           duration=10)
        
        # Update the previous hash
        previous_hash = current_hash
    
    # Wait for some time before checking again (e.g., 1 hour)
    time.sleep(1000)
