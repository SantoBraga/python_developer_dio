# dreamFilter

Description.

The package dreamFilter is used to:

- Filter:
  - Apply the dream filter in one or two images
 

- Compare:
  - Compare if two images are equal


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dreamFilter

```bash
pip install dreamFilter
```

## Usage

```python
from dreamFilter import tools, filter

# Opening the two example pictures

img1 = tools.open_img("example_img1.jpg")
img2 = tools.open_img("example_img2.jpg")

# Comparing two images:

# 1

print("# Comparing the first image with the second:\n")
print("\t- Different") if tools.equal(img1, img2) is False else print("\t- Equal")

# 2

print("\n# Comparing the first image with herself:\n")
print("\t- Different") if tools.equal(img1, img1) is False else print("\t- Equal")

# Filter:

# 1

print("\n# Filtering first image by second:\n")
filter.dream_filter(img1, img2, 'filtered_img1+2')
print("\t- Done.")

# 2

print("\n# Filtering the first image with itself:\n")
filter.dream_filter(img1, img1, 'filtered_img1+1')
print("\t - Done.")


```

## Author
Bruno Calegari

## License
    MIT License
    
    Copyright (c) [2022] [Bruno da Costa Calegari]
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
