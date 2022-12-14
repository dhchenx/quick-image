## Quick-Image: A simple image processing toolkit. 

### Installation

```
    pip install quick-image
```

## Examples

1. Basic Usage

```python
from quick_image import *

# quick_download_image(
# pic_url='https://pixnio.com/free-images/2022/07/21/2022-07-21-08-38-18-1350x900.jpg',
# save_path='flower.jpg')

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

quick_remove_pix_color_by_range("flower.jpg",lower_color= np.array([100, 150, 0]),
                                upper_color=np.array([140, 255, 255]),show=True)

```

2. Remove noise

```python

from quick_image import *
from quick_image.quick_image_similarity_measures import *

quick_remove_noise1(image_path="flower.jpg",save_path="test4/output1.jpg")

# quick_remove_noise2(image_path="flower.jpg",save_path="test4/output2.jpg",min_size=5)
score_ssim = ssim('flower.jpg', 'test4/output1.jpg')
score_dvsim = dvsim('flower.jpg', 'test4/output1.jpg')
print(score_ssim)
print(score_dvsim)

```

3. Estimate color similarity
```python
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
```

4. Edge detection

```python
from quick_image.quick_image_processing import *
import time
time_cost={}
if __name__=="__main__":
    image_path="flower.jpg"

    # coords = load_polygon_file(f'datasets/areas/{gender}/{body_part}_polygon_area.pickle')
    file_name="flower.jpg"

    start=time.time()
    # Using Canny algorithm (86)
    detect_edges(img_path=image_path,save_path='test3_output/'+file_name)
    time1=time.time()
    # Using Canny algorithm with polygons
    detect_edges_with_polygon(img_path=image_path, save_path='test3_output/' + file_name)
    time2=time.time()
    # Using single-color isolate algorithm
    isolate_image(image_path=image_path,save_path='test3_output/'+file_name)
    time3=time.time()
    # Using multi-color isolate algorithm
    isolate_image2(image_path=image_path, save_main_color='test3_output/' + file_name, 
                   save_path='test3_output/' + file_name)
    time4=time.time()
    time_cost["canny"]=time1-start
    time_cost["canny_polygon"]=time2-time1
    time_cost["isolate1"]=time3-time2
    time_cost["isolate2"]=time4-time3
    print("Method\tTime cost")
    for k in time_cost:
        print(f"{k}\t{round(time_cost[k],4)}")

```

### License

The `quick-image` toolkit is provided by [Donghua Chen](https://github.com/dhchenx) with MIT License.

