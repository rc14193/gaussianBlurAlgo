import math
from PIL import Image

PI = math.pi
E = math.e

image_file = input("Input the aboslute path to the image to blur:\n")
im = Image.open(image_file)
im_res = im.copy()

def gauss_func(stdev, loc):
    denom = (2*PI*stdev**2)**0.5
    expon = -((loc**2)/(2*stdev**2))
    func_val = (1/denom)*E**expon
    return func_val

pix_r = input("Enter the blur radius:\n")

box_offsets = []
for i in range(-pix_r,pix_r+1):
    for j in range(-pix_r,pix_r+1):
        box_offsets.append((i,j))

sigma = input("Enter the Gaussian standard deviation:\n")
coeff = [gauss_func(sigma, x)*gauss_func(sigma, y) for x,y in box_offsets]

def is_valid_pos(max_width,max_height,pos_x,pos_y):
    return (0 < pos_x < max_width) and (0 < pos_y < max_height)

MAX_X = im.width
MAX_Y = im.height
for x_val in range(1,im.width):
    for y_val in range(1,im.height):
        tot_r = 0
        tot_b = 0
        tot_g = 0
        for idx, offset in enumerate(box_offsets):
            if is_valid_pos(MAX_X, MAX_Y, x_val + offset[0], y_val + offset[1]):
                pixel_r, pixel_b, pixel_g = im.getpixel((x_val+offset[0],y_val+offset[1]))
            else:
                pixel_r, pixel_b, pixel_g = im.getpixel((x_val,y_val))
            tot_r += (pixel_r * coeff[idx])
            tot_b += (pixel_b * coeff[idx])
            tot_g += (pixel_g * coeff[idx])
        im_res.putpixel((x_val,y_val),(int(tot_r),int(tot_b),int(tot_g)))

im_res.show()
im.close()
        
