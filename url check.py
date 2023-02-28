import requests
import tldextract
import tkinter as tk

def is_link_safe(url):
    try:
        # Extract the domain name from the URL
        domain_name = tldextract.extract(url).domain

        # Check if the domain name matches a known safe social media domain
        social_media_domains = ["facebook", "youtube", "twitter", "instagram", "linkedin", "pinterest", "snapchat", "tiktok", "reddit", "flickr", "myspace", "periscope", "vimeo", "dailymotion", "imgur", "telegram"]
        if domain_name in social_media_domains:
            return True, domain_name
        
        # Check if the URL contains "hacking" or "18+" keywords
        if "hacking" in url or "18+" in url:
            return False, domain_name
        
        # Send a GET request to the URL and catch any exceptions
        response = requests.get(url, timeout=5)
        
        # Check if the response code is within the 2xx range
        if 200 <= response.status_code < 300:
            return True, domain_name
        else:
            return False, domain_name
    except:
        # Return False if an exception occurred during the request
        return False, domain_name

def check_urls():
    urls = url_entry.get("1.0", tk.END).strip().split("\n")
    results.delete("1.0", tk.END)
    
    for url in urls:
        is_safe, domain = is_link_safe(url)
        
        results.insert(tk.END, "URL: {}\n".format(url))
        results.insert(tk.END, "Domain: {}\n".format(domain))
        
        if is_safe:
            results.insert(tk.END, "Status: Safe\n\n")
        else:
            results.insert(tk.END, "Status: NOT Safe\n\n")

# Create the GUI
root = tk.Tk()
root.title("URL Safety Checker")

# Create the input label and text box
url_label = tk.Label(root, text="Enter URLs to check (one per line):")
url_label.pack(side=tk.TOP, pady=(10, 5))
url_entry = tk.Text(root, height=10, width=50)
url_entry.pack(side=tk.TOP, pady=(0, 10))

# Create the check button
check_button = tk.Button(root, text="Check URLs", command=check_urls)
check_button.pack(side=tk.TOP, pady=(0, 10))

# Create the results label and text box
results_label = tk.Label(root, text="Results:")
results_label.pack(side=tk.TOP, pady=(10, 5))
results = tk.Text(root, height=10, width=50)
results.pack(side=tk.TOP)

# Start the GUI
root.mainloop()
