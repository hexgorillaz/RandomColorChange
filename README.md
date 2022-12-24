# RandomColorChange
Python GUI Random Color Change
This Python app displays a square image on the screen and allows the user to change the color of the image by clicking a button. The color of the image is randomly generated using hexadecimal color codes.

## Setup
To set up and run this app, you will need to have Python 3 installed on your computer. You will also need to install the tkinter library, which provides a set of functions for creating GUI (graphical user interface) elements such as windows, buttons, and labels.

1. First, open a terminal window and navigate to the directory where you want to store the app.
2. Install the tkinter library by running the following command:

`
pip install tkinter
`
3. Next, create a new file called main.py and copy the following code into the file:

`
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
`
4. Finally, run the app by entering the following command in the terminal:
`
python main.py
`
The app should now open a window with a square image and a button. When you click the button, the color of the image will change to a randomly generated hexadecimal color.
