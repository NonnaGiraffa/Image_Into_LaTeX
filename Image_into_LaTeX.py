from PIL import Image
import glob
import os

def make_box(c):
    return "\\color{" + str(c) + "}{" + PIXEL + "}" 

def make_color_packet(r, g, b, c):
    return "\\definecolor{" + str(c) + "}{RGB}{" + f"{r},{g},{b}" + "}"


path = input("Path of image: ")
pixel_width = int(input("Ouput width (pixels): "))
pixel_height = int(input("Ouput height (pixels): "))

image_list = []
for filename in glob.glob(path):
    im = Image.open(filename)
    image_list.append(im)
rgb_im = im.convert('RGB')

image_width, image_height = im.size


PIXEL = "@·"
colors = {}
art = "\n"


try:
    for dy in range(1, image_height, image_height //  pixel_height):
        for dx in range(1, image_width, image_width //  pixel_width):
            r, g, b = rgb_im.getpixel((dx, dy))
            if (r, g, b) not in colors.keys():
                colors.update({(r, g, b): len(colors)})
            art += make_box(colors[(r, g, b)])
        art += "\\\\\n"
except IndexError:
    pass #;P

color_declaration = ""

for r, g, b in colors.keys():
    color_declaration += make_color_packet(r, g, b, colors[(r, g, b)])

msg = color_declaration + art
os.system('cls' if os.name == 'nt' else 'clear')
print(msg, "\n\n")