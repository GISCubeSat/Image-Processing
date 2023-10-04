import cv2

img = cv2.imread('ORIGINAL_IMAGES/BlueEarthTest.jpeg', 0)

thresh = 35
bkgrd = 1

ret, bw_img = cv2.threshold(img, thresh, bkgrd, cv2.THRESH_BINARY_INV)

bw = cv2.threshold(img, thresh, bkgrd, cv2.THRESH_BINARY)

#print(bw_img)

cnt = 0
height = len(bw_img)
width = len(bw_img[0])
n = 25

for i in range(0, height, n):
    for j in range(0, width, n):
        cnt += bw_img[i][j]

#print(cnt)
print(cnt/(height * width / (n**2)) * 100)

# print(bw)
# cv2.imshow("Original", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("Binary", bw_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()