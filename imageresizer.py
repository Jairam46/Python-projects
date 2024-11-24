import cv2 as cv

img=cv.imread("img.jpg")

cv.imshow("image",img)

scale_percent=50

width=int(img.shape[1]*scale_percent/100)
height=int(img.shape[0]*scale_percent/100)
print(f"width :{width},height :{height}")
image=cv.resize(img,(width,height))
cv.imwrite("image.jpg",image)
# cv.imwrite("img.png",)

# img.resize()  
cv.waitKey(0)


# NOTE
'''here the "img.shape[1]" is used to get the current width of the image and
img.shape[0] used get the current height.
'''