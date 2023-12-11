import winsound
import time, turtle

print("Welcome to the AeroForge Terminal.")
time.sleep(2)
print("To gain access, please answer these questions.")
print()
time.sleep(3)

def askQuestion(question, qanswer):
    answer = str(input(question)).lower()
    if answer == qanswer:
        print("Correct.")
        winsound.Beep(4000, 500)
    else:
        print("Sorry, that's incorrect.")
        winsound.Beep(1000, 1000)
        time.sleep(3)
        exit()
    time.sleep(5)


askQuestion("Enter your entrance ID here: ", "12345")
askQuestion("Enter your user ID here: ", "aayush")
print("Check for a new window!")

def on_click(x, y):
    turtle.goto(x, y)

# Set up the turtle screen
turtle.title("AeroForge Draw")
turtle.speed(1234543213531)  # Set the drawing speed

# Bind the on_click function to the screen click event
turtle.onscreenclick(on_click)

# Main loop to keep the window open
turtle.mainloop()