import tkinter as tk
import requests
import tldextract


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
    # Clear the results text box
    results_text.delete('1.0', tk.END)

    # Get the URLs from the input text box
    urls = input_text.get('1.0', tk.END).strip().split("\n")

    # Loop through the URLs
    for url in urls:
        # Check the URL
        is_safe, domain = is_link_safe(url)

        # Display the results
        results_text.insert(tk.END, "***************************\n")
        results_text.insert(tk.END, f"URL: {url}\n")
        results_text.insert(tk.END, f"Domain: {domain}\n")

        if is_safe:
            results_text.insert(tk.END, "Status: Safe\n", "safe")
        else:
            results_text.insert(tk.END, "Status: NOT Safe\n", "unsafe")
        results_text.insert(tk.END, "\n")

    # Set the focus back to the input text box
    input_text.focus_set()


# Create the main window
root = tk.Tk()
root.title("URL Safety Checker")

# Create the input label and text box
input_label = tk.Label(root, text="Enter the URLs to check, separated by a new line:")
input_label.pack()
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Bind the paste action to the Ctrl+V shortcut
input_text.bind("<Control-v>", lambda event: input_text.insert(tk.INSERT, root.clipboard_get()))

# Create the check button
check_button = tk.Button(root, text="Check URLs", command=check_urls)
check_button.pack()

# Create the results label and text box
results_label = tk.Label(root, text="Results:")
results_label.pack()
results_text = tk.Text(root, height=10, width=50)
results_text.tag_configure("safe", foreground="green")
results_text.tag_configure("unsafe", foreground="red")
results_text.pack()

# Set the focus to the input text box
input_text.focus_set()
# Run the main loop
root.mainloop()
