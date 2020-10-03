import numpy as np 
from PIL import Image

# im = np.array(Image.open('image0.jpg'))

# # im_R = im.copy()
# # im_R[:, :, (1, 2)] = 0
# # im_G = im.copy()
# # im_G[:, :, (0, 2)] = 0
# # im_B = im.copy()
# # im_B[:, :, (0, 1)] = 0

# im = -im - 10 

# # im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)

# pil_img = Image.fromarray(im)
# pil_img.save('color1.jpg')


x = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
])