import requests
import app

from PIL import Image
import io

response=requests.get('http://127.0.0.1:8000/plotdata')
file =io.BytesIO(response.content)
im=Image.open(file)
im.show()
