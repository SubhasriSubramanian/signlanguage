import requests
from PIL import Image
from io import BytesIO

image_urls = [
    'https://raw.githubusercontent.com/username/repo/main/images/A.png',
    'https://raw.githubusercontent.com/username/repo/main/images/B.png',
    'https://raw.githubusercontent.com/username/repo/main/images/C.png'
]

for url in image_urls:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
