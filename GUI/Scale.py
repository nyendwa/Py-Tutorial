# Import the tkinter module for GUI functionality
from tkinter import *

# Create the main window of the application
window = Tk()

# Define the function that will be executed when the "submit" button is pressed
def submit():
    # Print the current value of the scale in the console
    print('The temperature is: ' + str(scale.get()) + ' degrees C')

# Create a Scale widget with customized properties
scale = Scale(
    window,                  # Parent window
    from_=0,                 # Start value of the scale
    to=100,                  # End value of the scale
    length=600,              # Length of the scale in pixels
    tickinterval=10,         # Interval for tick marks on the scale
    resolution=0.01,         # Smallest step size for the slider
    orient=HORIZONTAL,       # Orientation of the scale (horizontal)
)

# Add the Scale widget to the window
scale.pack()

# Set the initial value of the scale to 50
scale.set(50)

# Create a Button widget with the label "submit" and link it to the submit function
button = Button(window, text='submit', command=submit)

# Add the Button widget to the window
button.pack()

# Start the main event loop of the application
window.mainloop()
