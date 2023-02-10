# Here we are just extracting RGB colors from images
# We use colorgram module here
# Just outputting a list of tuples containing the rgb values of the colors in the picture

from colorgram import extract

colors = extract('image.jpg', 100)
color_codes = []

for i in colors:
    rgb = i.rgb
    color_tuple = (rgb[0], rgb[1], rgb[2])
    color_codes.append(color_tuple)

print(color_codes)