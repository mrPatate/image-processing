from PIL import Image, ImageFont, ImageDraw
import textwrap

"""a program that decode lsb value of a png image (for the red channel)"""
def decode_image_lsb(file_location="encoded_sample.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
 
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
 
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
 
    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0,0,0)
    decoded_image.save("decoded_image_lsb.png")


"""a program that decode the msb value of a png image (for the red channel)"""
def decode_image_msb(file_location="encoded_sample.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
 
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
 
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
 
    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[2] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0,0,0)
    decoded_image.save("decoded_image_msb.png")

if __name__ == '__main__':
    decode_image_lsb()
    decode_image_msb()
