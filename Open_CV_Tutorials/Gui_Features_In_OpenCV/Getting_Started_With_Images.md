# Getting Started with Images

## Goals:- 

   * Here, you will learn how to read an image, how to display it and how to save it back
   * You will learn these functions : cv2.imread(), cv2.imshow() , cv2.imwrite()
   * Optionally, you will learn how to display images with Matplotlib


## Using OpenCV

### Read an Image


* Use the function __cv2.imread()__ to read an image. The image should be in the working directory or a full path of image should be given.


* Second argument is a flag which specifies the way image should be read.

    * cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    * cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
    * cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

**Note**-  Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.


See the code below:

```python
import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)
```

Even if the image path is wrong, it won’t throw any error, but `print img` will give you `None`.


### Display an Image

Use the function **cv2.imshow()** to display an image in a window. The window automatically fits to the image size.

First argument is a window name which is a string. second argument is our image. You can create as many windows as you wish, but with different window names.

```python
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

A screenshot of the window will look like this (in Fedora-Gnome machine):


![Image](Images/opencv_screenshot.jpg)