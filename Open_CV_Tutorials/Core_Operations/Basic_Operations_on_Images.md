# Basic Operations on Images

## Goal


* Access pixel values and modify them
* Access image properties
* Setting Region of Image (ROI)
* Splitting and Merging images

Almost all the operations in this section is mainly related to Numpy rather than OpenCV. A good knowledge of Numpy is required to write better optimized code with OpenCV.


## Accessing and Modifying pixel values

Let’s load a color image first:

```python
>>> import cv2
>>> import numpy as np

>>> img = cv2.imread('messi5.jpg')
```

You can access a pixel value by its row and column coordinates. 

* For BGR image, it returns an array of Blue, Green, Red values. 

* For grayscale image, just corresponding intensity is returned.

```python
>>> px = img[100,100]
>>> print px
[157 166 200]

# accessing only blue pixel
>>> blue = img[100,100,0]
>>> print blue
157

```

**Note**- Above mentioned method is normally used for selecting a region of array, say first 5 rows and last 3 columns like that. 

For individual pixel access, Numpy array methods, `array.item()` and `array.itemset()` is considered to be better. But it always returns a scalar. 

So if you want to access all B,G,R values, you need to call `array.item()` separately for all.


Better pixel accessing and editing method :

```python
# accessing RED value
>>> img.item(10,10,2)
59

# modifying RED value
>>> img.itemset((10,10,2),100)
>>> img.item(10,10,2)
100
```

## Accessing Image Properties

Image properties include number of rows, columns and channels, type of image data, number of pixels etc.


Shape of image is accessed by `img.shape`. It returns a tuple of number of rows, columns and channels (if image is color):

```python
>>> print img.shape
(342, 548, 3)
```

**Note** - If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to check if loaded image is grayscale or color image.

Total number of pixels is accessed by `img.size`:

```python
>>> print img.size
562248
```

Image datatype is obtained by `img.dtype`:

```python
>>> print img.dtype
uint8
```









