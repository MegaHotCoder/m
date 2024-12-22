# trump 사진 overlay 하기

from PIL import Image
import requests
from io import BytesIO

url_1 = "https://hangang.seoul.go.kr/www/file/smEditorImage.do?fileDay=202306&fileName=202306232154518c9ef2d3d70e4c37987c1172b03e1887.jpg"
url_2 = "https://clipart.info/images/ccovers/1495816051donald-trump-png-tumb-up-clipart.png"

response_1 = requests.get(url_1)
background = Image.open(BytesIO(response_1.content)).convert("RGBA")

response_2 = requests.get(url_2)
overlay = Image.open(BytesIO(response_2.content)).convert("RGBA")

overlay = overlay.resize((int(background.size[0]*0.8), int(background.size[1]*0.8)))
# 오버레이 이미지에 투명도 적용
overlay.putalpha(200)

# 배경에 오버레이 이미지 붙이기
background.paste(overlay, (background.size[0]//2 - overlay.size[0]//2, background.size[1]//2 - overlay.size[1]//2), overlay)

# 결과 저장
background = background.convert("RGB")
background.show()