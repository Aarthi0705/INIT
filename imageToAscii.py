from PIL import Image
import numpy as np

ASCII_chars = "@%#*+=-:. !"
def imgToAscii (image_path, width=100):
  img = Image.open(image_path).convert('L')

  aspect_ratio = img.height / img.width
  newHeight = int(width * aspect_ratio * 0.55) # adjust to fit ascii chars

  img = img.resize((width, newHeight))

  pixels = np.array(img)
  ascii_str = "\n".join(
    "".join(ASCII_chars[pixel // 32] for pixel in row ) for row in pixels
)
  return ascii_str
if __name__ == "__main__":
  image_path = "img-.png"
  ascii_art = imgToAscii(image_path, width= 100)
  print(ascii_art)
