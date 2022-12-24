import tkinter as tk
import random

# Create the main window
window = tk.Tk()

# Create a canvas to draw the square image on
canvas = tk.Canvas(window, width=200, height=200, bg='white')
canvas.pack()

# Define the change_color function
def change_color():
  # Generate a random hexadecimal color code
  color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
  
  # Clear the canvas by deleting all existing shapes
  canvas.delete("all")
  
  # Draw a square on the canvas using the generated color
  canvas.create_rectangle(0, 0, 200, 200, fill=color)

# Create a button to trigger the color change
button = tk.Button(window, text='Change color', command=change_color)
button.pack()

# Run the main loop
window.mainloop()
