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

# Print header
print("***************************")
print(" URL Safety Checker v1.0 ")
print("***************************\n")

# Ask for permission to check the URLs
permission = input("Do you want to check the URLs? (yes/no): ")

if permission.lower() == "yes":
    # Ask the user for the URLs
    urls = input("Enter the URLs to check, separated by a new line: ").strip().split("\n")

    # Loop through the URLs
    for url in urls:
        # Check the URL
        is_safe, domain = is_link_safe(url)

        # Display the results
        print("***************************")
        print(f"URL: {url}")
        print(f"Domain: {domain}")

        if is_safe:
            print("Status: Safe")
        else:
            print("Status: NOT Safe")
        print("")
else:
    print("No URLs were checked.")
