import requests
import time
from win10toast import ToastNotifier

def check_comic4():
    url = "http://sparklecarehospital.com/comic4"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    # Send a GET request to the comic4 page
    response = requests.get(url, headers=headers)
    
    # Check if the page exists
    if response.status_code == 200:
        # Check if the page content indicates a new comic page
        if "New Comic Page" in response.text:
            # Create a notification
            toaster = ToastNotifier()
            toaster.show_toast("New Comic Page",
                               "A new comic page is available!",
                               duration=10)
            
    # Wait for 1 minute before checking again
    time.sleep(60)
    check_comic4()

# Start checking for new comic pages
check_comic4()
