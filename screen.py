from PIL import Image

# Path to the screenshot of the game window
game_window_path = 'game.jpg'

# Coordinates for the top-left and bottom-right corners of the 8x8 matrix
left = 390   # Left coordinate of the 8x8 matrix
top = 73     # Top coordinate of the 8x8 matrix
right = 1213 # Right coordinate of the 8x8 matrix
bottom = 900 # Bottom coordinate of the 8x8 matrix

# Open the image
img = Image.open(game_window_path)

# Crop the image to the defined region
cropped_img = img.crop((left, top, right, bottom))

# Save the cropped image
cropped_img.save('cropped_matrix.png')

# Optionally, show the cropped image
cropped_img.show()
