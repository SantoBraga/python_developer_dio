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
