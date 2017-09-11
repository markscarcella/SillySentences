# Import Tkinter and the image packages
from Tkinter import *
from PIL import ImageTk, Image
# Import the random package
import random

# Make a function to generate a random sentance
def generateSentance(outputText):
	# define lists of adjectives, nouns, verbs, and adverbs
	adjective = ["cute","adorable","smelly"]
	noun = ["man","dog","car"]
	verb = ["runs","jumps","howls"]
	adverb = ["quickly","slowly","occasionally"]
	# construct a sentance using random words from the lists above
	sentance = "The "+random.choice(adjective)+" "+random.choice(noun)+" "+random.choice(verb)+" "+random.choice(adverb)+"."
	# take the output text widget and delete all the characters
	outputText.delete(1.0, END)
	# insert the sentance into the output text
	outputText.insert(END, sentance)

# Make your Tkinter window
window = Tk()
# Give it a title
window.title("My Silly Sentance App")
# Set it's geometry
window.geometry("480x270")
# Open an image and resize it
backgroundImage = ImageTk.PhotoImage(Image.open("./doge.jpg").resize((480,270),Image.ANTIALIAS))
# Make a background label with the image in it
background = Label(window, image=backgroundImage)
# Place the background at (0,0)
background.place(x=0, y=0, relwidth=1, relheight=1)

# Make a credits label
title = Label(window, text="Made by Curtis", background="Red", foreground="White")
# pack the label at the bottom, filling across in X
title.pack(side=BOTTOM, fill=X)

# Make a text widget to display the output
outputText = Text(window, height=2, width=60, font=("Arial",36), wrap=WORD, background="black", foreground="white")
# pack the output text widget
outputText.pack()

# Make a button to generate a sentance when you click
myButton = Button(window, text="Generate random sentance", command=lambda:generateSentance(outputText))
# pack the button widget
myButton.pack()

# Start the main loop
window.mainloop()