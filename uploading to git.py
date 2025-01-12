import tkinter
import random

# List of possible colors:
colors = ['blue', 'red', 'orange', 'pink', 'purple', 'yellow', 'green', 'brown', 'black', 'white', 'grey']
score_round1 = 0
score_round2 = 0
timeleft = 30
round_number = 1

# Function to start the game:
def start_game(event=None):
    global timeleft
    if timeleft == 30:
        countdown()
    next_color()

# Function to start round 2:
def start_round2(event=None):
    global timeleft
    global round_number
    round_number = 2
    timeleft = 30
    instructions.config(text="Round 2: Type the color name", font=('Helvetica', 18))
    scoreLabel.config(text="Score: 0")
    e.config(state='normal')
    e.focus_set()
    resultLabel.config(text="")  # Clear the comment when round 2 starts
    countdown()
    next_color()

# Function to choose and display the next color:
def next_color():
    global score_round1, score_round2, timeleft, round_number
    if timeleft > 0:
        e.focus_set()
        user_input = e.get().lower()
        if round_number == 1:
            # Check if the user's input matches the color of the text
            if user_input == colors[1].lower():
                score_round1 += 1
        else:
            # Check if the user's input matches the color name displayed
            if user_input == colors[0].lower():
                score_round2 += 1
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        # Set the text color based on the round:
        text_color = colors[1] if round_number == 1 else 'black'
        label.config(fg=text_color, text=colors[0])
        current_score = score_round1 if round_number == 1 else score_round2
        scoreLabel.config(text="Score: " + str(current_score))
    else:
        if round_number == 1:
            round_number = 2
            e.config(state='disabled')
            print_comment(f"End of round 1. Your score: {score_round1}, Fantastic work! Your concentration really paid off!")
            root.after(2000, start_round2_setup)
        else:
            compare_scores()

# Function to set up round 2:
def start_round2_setup():
    instructions.config(text="Press Enter to start Round 2", font=('Helvetica', 18))
    e.config(state='normal')
    root.bind('<Return>', start_round2)

# Function to compare scores from both rounds:
def compare_scores():
    if score_round1 > score_round2:
        result = "Great job! You beat the harder round!"
    elif score_round1 < score_round2:
        result = "Good job! You played well."
    else:
        result = "Well done! You got equal scores on both rounds."
    resultLabel.config(text=result)
    print_comment(f"End of round 2. Your score: {score_round2}, well done!")
    e.config(state='disabled')

# Function to print comments after each round:
def print_comment(comment):
    resultLabel.config(text=comment)

# Countdown timer function:
def countdown():
    global timeleft
    global round_number
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    elif timeleft == 0:
        if round_number == 2:
            compare_scores()
        else:
            round_number = 2
            print_comment(f"End of round 1. Your score: {score_round1}, fantastic work! Your concentration really paid off!")
            instructions.config(text="Press Enter to start Round 2", font=('Helvetica', 18))
            e.config(state='disabled')
            root.bind('<Return>', start_round2)

# Driver code:
# Create a GUI window:
root = tkinter.Tk()
root.title("ColorGame")
root.geometry("375x200")

# Add an instructions label:
instructions = tkinter.Label(root, text="Round 1: Type in the color of the word and not the word name!",
                             font=('Helvetica', 18))
instructions.pack()

# Add a score label:
scoreLabel = tkinter.Label(root, text="Press Enter to start Round 1", font=('Helvetica', 18))
scoreLabel.pack()

# Add a time left label:
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 18))
timeLabel.pack()

# Add a label for displaying the colors:
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Add a label to display the result at the end of the game:
resultLabel = tkinter.Label(root, font=('Helvetica', 18))
resultLabel.pack()

# Add a text entry box for typing in colors:
e = tkinter.Entry(root)
root.bind('<Return>', start_game)
e.pack()
e.focus_set()

# Start the GUI:
root.mainloop()