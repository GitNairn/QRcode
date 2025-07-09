import qrcode

import requests

def check_url_exists(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        print(url + " found")
        return response.status_code < 400
    except requests.RequestException:
        print(url + " not found")
        return False
        
def find_working_url(base_name):
    base_name = base_name.lower().strip()
    tlds = ['.co.uk', '.com', '.net', '.org', '.uk', '.gov', '.io']

    if base_name.startswith('http://') or base_name.startswith('https://'):
        if check_url_exists(base_name):
            return base_name
        else:
            return None

    for tld in tlds:
        if base_name.endswith(tld):
            url = 'https://www.' + base_name
            if check_url_exists(url):
                return url
            else:
                return None

    for tld in tlds:
        url = 'https://www.' + base_name + tld
        if check_url_exists(url):
            return url

    return None

def get_result(src):
    if len(src)<8 or src[:8] != 'https://':
        return 'https://www.'+src+".com"
    return src
    
source = input("Enter website name or URL")

website_link__ = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
website_link = find_working_url(source)

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save(f"{source}.png")