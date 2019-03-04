from autoaugment import ImageNetPolicy
from PIL import Image
import skimage as sk
import cv2
import os

srcpath = os.path.join(os.getcwd(), 'src')
savepath = os.path.join(os.getcwd(), 'edit')

if not os.path.isdir(savepath):
    os.makedirs(savepath)

directory = os.fsencode(srcpath)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    image = Image.open(srcpath+'/'+filename)

    for i in range(5):
        policy = ImageNetPolicy()
        transformed = policy(image)

        transformed.save(savepath + "/" + filename[:-4] + "_" + "edit" + str(i) + ".jpg")
    
