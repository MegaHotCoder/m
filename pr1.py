from PIL import Image, ImageDraw, ImageOps, ImageEnhance, ImageFilter
import requests
from io import BytesIO

url = "https://github.com/user-attachments/assets/6ac3935d-00d3-46a0-a2ea-463daa051e27"

response = requests.get(url) # 코드 작성
image = Image.open(BytesIO(response.content)) # 코드 작성

re_img = image.filter(ImageFilter.CONTOUR)

re_img.show()