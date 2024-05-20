from PIL import Image
import os

image = Image.open(f"{os.path.dirname(__file__)}\\img.png")

pixels = image.load()

width, height = image.size

txt = ""

mode = image.mode
print(f"Image mode: {mode}")

for y in range(height):
    for x in range(width):
        if mode == 'RGB':
            r, g, b = pixels[x, y]
        elif mode == 'RGBA':
            r, g, b, a = pixels[x, y]
        elif mode == 'L':
            gray = pixels[x, y]
        else:
            print(f"Unsupported mode: {mode}")

        brightness = 0.299 * r + 0.587 * g + 0.114 * b

        if (brightness <= 25):
            txt += "&"
        elif (brightness > 25 and brightness <= 50):
            txt += "\\"
        elif (brightness > 50 and brightness <= 75):
            txt += "?"
        elif (brightness > 75 and brightness <= 100):
            txt += "["
        elif (brightness > 100 and brightness <= 125):
            txt += "="
        elif (brightness > 125 and brightness <= 150):
            txt += "$"
        elif (brightness > 150 and brightness <= 175):
            txt += "*"
        elif (brightness > 175 and brightness <= 200):
            txt += "<"
        elif (brightness > 200 and brightness <= 225):
            txt += "@"
        elif (brightness > 225 and brightness <= 255):
            txt += "+"
    txt += "\n"

with open(f"{os.path.dirname(__file__)}\\ascii.txt", mode='w') as f:
    f.write(txt)