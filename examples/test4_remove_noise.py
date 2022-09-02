
from quick_image import *
from quick_image.quick_image_similarity_measures import *

quick_remove_noise1(image_path="flower.jpg",save_path="test4/output1.jpg")

# quick_remove_noise2(image_path="flower.jpg",save_path="test4/output2.jpg",min_size=5)
score_ssim = ssim('flower.jpg', 'test4/output1.jpg')
score_dvsim = dvsim('flower.jpg', 'test4/output1.jpg')
print(score_ssim)
print(score_dvsim)
