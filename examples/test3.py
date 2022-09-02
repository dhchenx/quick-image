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
    isolate_image2(image_path=image_path, save_main_color='test3_output/' + file_name, save_path='test3_output/' + file_name)
    time4=time.time()
    time_cost["canny"]=time1-start
    time_cost["canny_polygon"]=time2-time1
    time_cost["isolate1"]=time3-time2
    time_cost["isolate2"]=time4-time3
    print("Method\tTime cost")
    for k in time_cost:
        print(f"{k}\t{round(time_cost[k],4)}")



