from quick_image import *

# quick_download_image(pic_url='https://pixnio.com/free-images/2022/07/21/2022-07-21-08-38-18-1350x900.jpg',save_path='flower.jpg')

# quick_show_image("flower.jpg")

# quick_show_image_by_grayscale("flower.jpg")

# quick_show_image_by_grayscale2("flower.jpg")

# quick_show_image_gray("flower.jpg")

# quick_convert_12bit_gray("flower.jpg","flower_12bit.jpg")

# quick_show_canny("flower.jpg")

# quick_replace_image_color("flower.jpg",show=True)

# quick_save_edges("flower.jpg","flower_edges.jpg",t=50)

# quick_filter_by_dist("flower.jpg",max_dist=1000)

'''
list_points,list_colors=quick_pick_image_color("flower.jpg","points.csv" ,"colors.csv")
print(list_points)
print(list_colors)
'''

# quick_remove_pix_color("flower.jpg",target_color= [203,152,125],save_path='flower_removed_color.jpg')

quick_remove_pix_color_by_range("flower.jpg",lower_color= np.array([100, 150, 0]),upper_color=np.array([140, 255, 255]),show=True)



