import qrcode
import requests

def check_url_exists(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        response = requests.get(url, allow_redirects=True, timeout=5, headers=headers)
        print(f"{url} status: {response.status_code}")
        return response.status_code < 400
    except requests.RequestException:
        return False
        
def find_working_url(base_name):
    base_name = base_name.lower().strip()
    tlds = ['.co.uk', '.com', '.net', '.org', '.uk', '.gov', '.io']

    if base_name.startswith('http://') or base_name.startswith('https://'):
        if check_url_exists(base_name):
            return base_name

    for tld in tlds:
        if base_name.endswith(tld):
            url = 'https://www.' + base_name
            if check_url_exists(url):
                return url

    for tld in tlds:
        url = 'https://www.' + base_name + tld
        if check_url_exists(url):
            return url

    return None

source = input("Enter website name or URL: ")
website_link = find_working_url(source)
print(f"Website link found: {website_link}")
if website_link:
    import os
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(website_link)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    # Sanitize filename
    base_name = source
    if check_url_exists(source):
        base_name = source.split('.')[1]
    base_name = base_name.strip()
    if not base_name:
        base_name = 'qr_code'
    filename = f"{base_name}.png"
    counter = 1
    while os.path.exists(filename):
        filename = f"{base_name}({counter}).png"
        counter += 1
    img.save(filename)
    print(f"QR code saved as {filename}")
else:
    print("No valid website link found. QR code not generated.")