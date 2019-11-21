#Hang man game to guess words
#uses turtle
import random
import turtle
import time

wordList = ['abruptly', 'absurd', 'abyss' , 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', \
            'beekeeper', 'bikini', 'blitz', 'blizzard']


secretword = random.choice(wordList)
wrongLetters = []
correctLetters = []


#"a","e","i","o","u"

colorsList = ["Green","Red", "blue"]
randomcolor = random.choice(colorsList)
#print(wordList)
print(f"The secret word is {secretword} ")

MAXGUESSES = 13
wrongGuesses = 0
screenWord = ""

#screen setup
sWidth = 1600
sHight = 800
turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(sWidth, sHight)
#screen.bgcolor(114, 70, 233)
screen.bgcolor(randomcolor)


topFont = 70
#Setup Turtle
t = turtle.getturtle()
t.shape("turtle")
t.color(242, 242, 208)
t.width(5)
t.speed(0)
t.penup()
t.hideturtle()
# Second turtle
topScreenTurtle = turtle.Turtle()
t = turtle.getturtle()
topScreenTurtle.shape("turtle")
topScreenTurtle.color(242, 242, 208)
topScreenTurtle.width(5)
topScreenTurtle.speed(0)
topScreenTurtle.penup()
topScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.08), -1 * int(sHight/2) + -1 * int(sHight * -0.1))
topScreenTurtle.setheading(0)

#Bottom screen turtle

bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.shape("turtle")
bottomScreenTurtle.color(242, 242, 208)
bottomScreenTurtle.width(5)
bottomScreenTurtle.speed(0)
bottomScreenTurtle.penup()
bottomScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.08), -1 * int(sHight/2) + int(sHight * 0.25))
bottomScreenTurtle.setheading(0)
topScreenTurtle.hideturtle()

#Location Variables
righthandLoc= (0,0)
lefthandLoc= (0,0)
leftfootLoc = (0,0)
rightfootLoc = (0,0)
topofbody = (0,0)
def drawGallows():
    t.forward(int(sWidth * 0.125))
    t.right(90)
    t.forward(int(sHight * 0.25))
    t.left(90)
    #Draw Bottom Line
    #Fowards of line
    t.pendown()
    t.forward(int(sWidth * 0.26))
    #BAckwards line
    t.backward(int(sWidth * 0.13))
    #G0 up
    t.left(90)
    t.forward(int(sHight * 0.6))
    t.left(90)
    #Upper line
    t.forward(int(sWidth * .13))
    t.left(90)
    #Down Line
    t.forward(int(sHight*.07))



def drawHead():
    t.right(90)
    t.circle(int(sHight * 0.04))

def drawBody():
    global topofbody
    t.left(90)
    t.penup()
    t.forward(int(sHight * 0.08))
    topofbody = t.position()
    t.pendown()
    t.forward(int(sHight * 0.20))

def drawRightLeg():
    global rightfootLoc
    t.right(45)
    t.forward(int(sHight * 0.13))
    rightfootLoc = t.position()
    t.right(180)
    t.forward(int(sHight * 0.13))
    t.left(45)

def drawLeftLeg():
    global leftfootLoc
    t.right(135)
    t.forward(int(sHight * 0.13))
    leftfootLoc = t.position()
    t.left(180)
    t.forward(int(sHight * 0.13))
    t.right(45)



def gettomiddleofbody():
    t.setheading(-90)
    t.right(180)
    t.forward(int(sHight * 0.10))

def drawLeftarm():
    global lefthandLoc
    t.left(45)
    t.forward(int(sHight * 0.1))
    lefthandLoc = t.position()
    t.right(180)
    t.forward(int(sHight * 0.1))

def drawLhand():
    t.goto(righthandLoc)
    t.right(90)
    t.circle(int(sHight * 0.01))

def drawrightarm():
    global righthandLoc
    t.left(90)
    t.forward(int(sHight * 0.1))
    righthandLoc = t.position()

def drawRhand():
    t.goto(righthandLoc)
    t.right(180)
    t.circle(int(sHight * 0.01))
    t.penup()

def drawLhand():
    t.goto(lefthandLoc)
    t.right(90)
    t.pendown()
    t.circle(int(sHight * 0.01))
    t.penup()

def drawLleg():
    t.goto(leftfootLoc)
    t.right(270)
    t.pendown()
    t.circle(int(sHight * 0.02))
    t.penup()

def drawRleg():
    t.goto(rightfootLoc)
    t.left(270)
    t.pendown()
    t.circle(int(sHight * 0.02))
    t.penup()

def Leye():
    t.goto(topofbody)
    t.setheading(90)
    t.left(10)
    t.forward(int(sHight * 0.046))
    t.pendown()
    t.circle(int(sHight * 0.01))
    t.penup()

def Reye():
    t.goto(topofbody)
    t.setheading(90)
    t.right(30)
    t.forward(int(sHight * 0.046))
    t.pendown()
    t.circle(int(sHight * 0.01))
    t.penup()

def Smile():
    t.goto(topofbody)
    t.setheading(90)
    t.forward(int(sHight * 0.015))
    t.left(90)
    t.forward(int(sHight * 0.020))
    t.right(90)
    t.forward(int(sHight * 0.010))
    t.right(180)
    t.pendown()
    t.forward(int(sHight * 0.010))
    t.left(90)
    t.forward(int(sHight * 0.040))
    t.left(90)
    t.forward(int(sHight * 0.010))
    t.hideturtle()
    t.penup()

def updatedrawing():
    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawBody()
    if wrongGuesses == 3:
        drawRightLeg()
    if wrongGuesses == 4:
        drawLeftLeg()
    if wrongGuesses == 5:
        gettomiddleofbody()
        drawLeftarm()
    if wrongGuesses == 6:
        drawrightarm()
    if wrongGuesses == 7:
        drawRhand()
    if wrongGuesses == 8:
        drawLhand()
    if wrongGuesses == 9:
        drawLleg()
    if wrongGuesses == 10:
        drawRleg()
    if wrongGuesses == 11:
        Leye()
    if wrongGuesses == 12:
        Reye()
    if wrongGuesses ==13:
        Smile()

def drawWrongLetters():
    topScreenTurtle.clear()
    lString = "Wrong Letters: "
    for l in wrongLetters:
        lString = lString + l + ", "
    lString = lString[0: len(lString)-2]
    topScreenTurtle.write(lString, move=False, align="left", font=("Arial", 55, "normal"))


def drawWord():
    global screenWord
    # step 1--- save turtle info
    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomScreenTurtle.clear()
    bottomScreenTurtle.penup()
    #t.goto(-1 * int(sWidth/2) + int(sWidth * 0.08), -1 * int(sHight/2) + int(sHight * 0.25))
    bottomScreenTurtle.showturtle()
    bottomScreenTurtle.hideturtle()
    bottomScreenTurtle.setheading(0)

    screenWord = ""
    for letter in secretword:
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord +=  "_" + " "

    bottomScreenTurtle.write(screenWord, move=False, align="left", font=("Arial", 55, "normal"))
    #t.goto(currentLoc)
    #t.setheading(currentHead)
    #bottomScreenTurtle.showturtle()

def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + ", "

    boxTitle = "Letters Used:"+ badLetterString

    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word")
    return theGuess

def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align="left", font=("Arial", 55, "normal"))
    time.sleep(2)
    topScreenTurtle.clear()


def printWinOrLose(win):
    topScreenTurtle.clear()

    if win:
        topScreenTurtle.write("YOU WIN", move=False, align="left", font=("Arial", topFont, "normal"))


    else:
        topScreenTurtle.write("YOU LOST", move=False, align="left", font=("Arial", topFont, "normal"))


def getwordGuess():
    playerWordGuess= screen.textinput("Guess it","Enter your guess of the word!")

    if playerWordGuess.lower() == secretword:
        #celebrate win
        print("WIN")
        printWinOrLose(True)
        return False  #Means gamne is over
    else:
        #celbrate failure!!
        printWinOrLose(False)
        gameOn = False
        time.sleep(1)
        writeErrorMessage("The secret word is " + secretword)
        return False #Means gamne is over





## NOW play the game
gameOn = True
updatedrawing()
#Main Game Loop
while gameOn:
    drawWord()

    guess = getGuess()

    if guess == "$$":
        gameOn = getwordGuess()
    elif len(guess)!= 1:
        writeErrorMessage("I need a single letter. Guess again")
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("You need to guess a letter! Guess again")
        drawWrongLetters()
    elif guess.lower() in wrongLetters:
        writeErrorMessage("You already guessed " + guess + ". Guess Again")
        drawWrongLetters()
    elif guess.lower() in correctLetters:
        writeErrorMessage(guess + " is in the word. Guess Again")
        drawWrongLetters()
    else:
        if guess.lower() in secretword.lower():
            correctLetters.append(guess.lower())
            drawWord()

        else:
            wrongLetters.append(guess.lower())
            wrongGuesses += 1
            drawWrongLetters()
            updatedrawing()

        if(wrongGuesses>= MAXGUESSES):
            writeErrorMessage("You are out of Guesses. GAME OVER")
            gameOn = False
            writeErrorMessage("The secret word is " + secretword)

        if(" " not in screenWord):
            writeErrorMessage("YOU WIN!!!")







turtle.mainloop()


