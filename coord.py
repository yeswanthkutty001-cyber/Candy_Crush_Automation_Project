import tkinter as tk
from PIL import Image, ImageTk

# Global variable to store the coordinates of the crop area
crop_coords = []

# Function to capture the click coordinates
def on_click(event):
    if len(crop_coords) < 2:
        crop_coords.append((event.x, event.y))
        print(f"Clicked at: ({event.x}, {event.y})")
        
        # If two points are captured, crop the image
        if len(crop_coords) == 2:
            print(f"Top-left: {crop_coords[0]}, Bottom-right: {crop_coords[1]}")
            # Open the image and crop it based on the selected coordinates
            img = Image.open(image_path)
            cropped_img = img.crop((crop_coords[0][0], crop_coords[0][1], crop_coords[1][0], crop_coords[1][1]))
            cropped_img.show()

# Path to the image you want to crop
image_path = 'game.jpg'

# Create the root window
root = tk.Tk()
root.title("Select Crop Area")

# Open the image
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Bind the click event to the on_click function
label.bind("<Button-1>", on_click)

# Run the Tkinter event loop
root.mainloop()
