#python project - color game:
import tkinter
import random
#list of possible colors:
colors = ['blue', 'red', 'orange','pink','purple','yellow','green', 'brown','black','white','grey']
score = 0
#the game time left:
timeleft = 30
#function that will start the game:
def start_game(event = None):
    if timeleft == 30:
        #start the countdown timer:
        countdown()
    #run the next function to choose the next color:
    #choose the next color:
    next_color()
#function to choose and display the next color:
def next_color():
    #use and globally declared 'score' and play variables above:
    global score
    global timeleft
    #if a game is currently in play:
    if timeleft > 0:
        #make the text entry box active:
        e.focus_set()
        #if the color typed is equal to the color of the text:
        if e.get().lower() == colors[1].lower():
            score+= 1
        #clear the text entry box:
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        #change the color to type by changing the text_and_the color to a random color value:
        label.config(fg = str(colors[1]),text = str(colors[0]))
        #update the score:
        scoreLabel.config(text = "score:" +str(score))


#countdown timer function:
def countdown():
    global timeleft
    #if a game is in play:
    if timeleft > 0:
        #decrement the timer:
        timeleft -= 1
        #update the time left label:
        timeLabel.config(text = "Time left:" +str(timeleft))
        #run the function again after a second:
        timeLabel.after(1000, countdown)


#driver code:
#create a GUI window:
root = tkinter.Tk()
#set the title:
root.title("ColorGame")
#set the size:
root.geometry("375x200")
#add an instructions label:
instructions = tkinter.Label(root,text = "Type in the color of the word and not the word text!",
font = ('Helvetica' ,18))
instructions.pack()
#add a score label:
scoreLabel = tkinter.Label(root,text = "press enter to start", font =('Helvetica' ,18))
scoreLabel.pack()
#add a time left label:
timeLabel = tkinter.Label(root, text = "time left:" + str(timeleft), font = ('Helvetica',18))
timeLabel .pack()
#add a label for displaying the colors:
label = tkinter.Label(root,font = ('Helvetica',60))
label.pack()
#add a text entry box for typing in colors:
e =  tkinter.Entry(root)
#run the 'StartGame' function when the enter key is pressed:
root.bind('<Return>',start_game)
e.pack()
#set focus on the entry box:
e.focus_set()
#start the GUI:
root.mainloop()