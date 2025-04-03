from tkinter import *
import pandas

# Read the data
try:
    data = pandas.read_csv("./Day 31/data/updated_french_words.csv")
except:
    data = pandas.read_csv("./Day 31/data/french_words.csv")

# Store the current word (global variable)
current_word = {}

# Function to generate a random French word
def generate_random_word():
    global current_word
    if not data.empty:  # Check if there are still words left
        random_row = data.sample(n=1)
        current_word = {
            "French": random_row.iloc[0]["French"],
            "English": random_row.iloc[0]["English"]
        }

        # Show the French word
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=current_word["French"], fill="black")
        canvas.itemconfig(card_image, image=front_card_img)

        # Start the 3-second timer to flip the card
        window.after(3000, flip_card)
    else:
        canvas.itemconfig(title, text="No words left!", fill="red")
        canvas.itemconfig(word, text="Good job!", fill="red")

def remove_words():
    global data
    try:
        data = data[data['French'] != current_word['French']]  # Remove the current word
    except KeyError:
        print("No words left")
    data.to_csv("./Day 31/data/updated_french_words.csv", index=False)  # Saving to new CSV
    print("Updated data saved to 'updated_french_words.csv'")

    # Generate a new word after removal
    generate_random_word()

# Function to flip the card and show the English word
def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_image, image=back_card_img)

# Background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize the main window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
my_image_right = PhotoImage(file="./Day 31/images/right.png")
my_image_wrong = PhotoImage(file="./Day 31/images/wrong.png")
front_card_img = PhotoImage(file="./Day 31/images/card_front.png")
back_card_img = PhotoImage(file="./Day 31/images/card_back.png")

# Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)

# Create text
title = canvas.create_text(400, 150, text="", font=("Arial", 48, "italic"))  # Initially empty
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))  # Initially empty

# Create buttons
wrong_button = Button(image=my_image_wrong, command=generate_random_word, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button = Button(image=my_image_right, command=remove_words, highlightthickness=0)
right_button.grid(column=1, row=1)

# Start the app with a word immediately
generate_random_word()

# Start the main event loop
window.mainloop()
