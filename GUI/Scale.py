
# Import the tkinter module for GUI functionality
from tkinter import *

# Create the main window of the application
window = Tk()

# Define the function that will be executed when the "submit" button is pressed
def submit():
    # Print the current value of the scale in the console
    print('The temperature is: ' + str(scale.get()) + ' degrees C')

# Create a Scale widget with a range from 100 to 0 (slider moves downward)
scale = Scale(window, from_=100, to=0)

# Add the Scale widget to the window
scale.pack()

# Create a Button widget with the label "submit" and link it to the submit function
button = Button(window, text='submit', command=submit)

# Add the Button widget to the window
button.pack()

# Start the main event loop of the application
window.mainloop()
