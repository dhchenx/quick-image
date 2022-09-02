from quick_image import *
from skimage import io
'''
    find image color similarity
'''
# Example 1:
img_rgb = io.imread('flower.jpg')
green = [203,152,125]
s=get_pct_color(img_rgb, green, 10)
print("s=",s)


# Example 2:
base=[35,103,239]
test_color=[153,0,0]
test_color1=[0,128,255]

print(quick_color_similarity(base,test_color))
print(quick_color_similarity(base,test_color1))