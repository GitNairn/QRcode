# Author(s)
GitNairn

# QRcode
## Generates a QR code (png) when given a URL, shortened URL or name of a website.

# Description
This app was built by extending a tutorial on codedex.io by Jerry Zhu 
https://www.codedex.io/projects/generate-a-qr-code-with-python
The tutorial shows how to generate a QR code when given a URL using the qrcode library and I extended it by only needing the name of a website by
testing full URLs with different TLDs to check if websites exists (and have a valid response code) then using the first available one.

# Instructions
When asked for input you can either enter the full URL (https://www.amazon.co.uk/), a shortened URL (amazon.co.uk) or just the name (amazon).
All of these would result in the same QR code being generated in the cwd
To use this app you will need pillow, requests and qrcode installed ('pip install qrcode pillow requests')