import qrcode
import requests

tlds = ['.co.uk', '.com', '.net', '.org', '.uk', '.gov', '.io']  # List of common TLDs (for UK at least)

def check_url_exists(url):
    try:
        headers = {
            # Set a User Agent to avoid being blocked by some websites
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        # Send a GET request to check if the URL is reachable
        response = requests.get(url, allow_redirects=True, timeout=5, headers=headers)
        print(f"{url} status: {response.status_code}")  # Print the HTTP status code for debugging
        return response.status_code < 400  # Return True if status code is OK (less than 400)
    except requests.RequestException:
        return False
        
def find_working_url(base_name):
    base_name = base_name.lower().strip() 

    # If input looks like a full URL, check it directly
    if base_name.startswith('http://') or base_name.startswith('https://'):
        if check_url_exists(base_name):
            return base_name

    # Try adding 'www.' if input ends with a known TLD
    for tld in tlds:
        if base_name.endswith(tld):
            url = 'https://www.' + base_name
            if check_url_exists(url):
                return url

    # Try appending each TLD to the input and check if it works
    for tld in tlds:
        url = 'https://www.' + base_name + tld
        if check_url_exists(url):
            return url

    return None  # Return None if no working URL is found

source = input("Enter website name or URL: ")
website_link = find_working_url(source)
print(f"Website link found: {website_link}")

if website_link:
    import os
    qr = qrcode.QRCode(version=1, box_size=5, border=5)  # Create a QRCode object with specified settings
    qr.add_data(website_link)  # Add the working URL to the QR code
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')  # Generate the QR code image

    # Check filename has no special characters and is unique
    base_name = source
    if check_url_exists(source):  # If input is a URL, extract the domain part for the filename
        base_name = source.split('.')[1]
    # Remove TLD from base_name if present
    for tld in tlds:
        if base_name.endswith(tld):
            base_name = base_name[:-len(tld)]
            break
    base_name = base_name.strip()
    if not base_name:
        base_name = 'qr_code'  # Use a default name if base_name is empty
    filename = f"{base_name}.png"
    counter = 1
    # If file exists, append (1), (2), etc. to filename to avoid overwriting
    while os.path.exists(filename):
        filename = f"{base_name}({counter}).png"
        counter += 1
    img.save(filename)  # Save the QR code image
    print(f"QR code saved as {filename}")
else:
    print("No valid website link found. QR code not generated.")