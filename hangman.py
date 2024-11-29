#########################################################
## File Name: hangman.py                               ##
## Description: Starter for Hangman project - ICS3U    ##
#########################################################
import pygame
import random

pygame.init()
winHeight = 600
winWidth = 800
win=pygame.display.set_mode((winWidth,winHeight))
#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
BLACK = (0,0, 0)
WHITE = (255,255,255)

# Load the custom font
btn_font = pygame.font.Font("resources/font/o1.ttf", 20)
guess_font = pygame.font.Font("resources/font/o1.ttf", 24)
lost_font = pygame.font.Font("resources/font/o1.ttf", 45)

word = ''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('resources/hangman/1.png'), 
               pygame.image.load('resources/hangman/2.png'), 
               pygame.image.load('resources/hangman/3.png'), 
               pygame.image.load('resources/hangman/4.png'), 
               pygame.image.load('resources/hangman/5.png'), 
               pygame.image.load('resources/hangman/6.png'),
               pygame.image.load('resources/hangman/7.png')
               ]

limbs = 0


def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    
    # Draw hangman image scaled to fill the window
    pic = hangmanPics[limbs]
    pic = pygame.transform.scale(pic, (winWidth, winHeight))  # Scale the image to fill the window
    win.blit(pic, (0, 0))  # Draw the scaled image at the top-left corner

    # Draw the blank word on top of the hangman image
    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1, (winWidth / 2 - length / 2, 50))  # Center the blank word

    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    pygame.display.update()


def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            

def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None


def end(winner=False):
    global limbs
    win.fill(WHITE)  # Set background color to white

    if winner:
        # Display "YOU WIN" message
        win_label = lost_font.render('YOU WIN', 1, BLACK)  # Create the win label
        win.blit(win_label, (winWidth / 2 - win_label.get_width() / 2, winHeight / 2 - win_label.get_height() / 2))  # Center the label
        pygame.display.update()  # Update the display to show the label
        pygame.time.delay(3000)  # Wait for 3 seconds before showing buttons
    else:
        pic = hangmanPics[6]  # Use hangman6 image for losing
        pic = pygame.transform.scale(pic, (winWidth, winHeight))  # Scale the image to fill the window
        win.blit(pic, (0, 0))  # Draw the scaled image at the top-left corner
        pygame.display.update()  # Update the display to show the image
        pygame.time.delay(5000)  # Wait for 5 seconds

    # Clear the screen and prepare to display buttons
    win.fill(WHITE)  # Clear the screen

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))

    # New button dimensions
    button_width = 200  # Adjusted width for better fit
    button_height = 50

    # Draw buttons without the button image
    play_again_button = pygame.Rect(winWidth / 4 - button_width / 2, winHeight - 100, button_width, button_height)  # Centered on the left
    quit_button = pygame.Rect(winWidth * 3 / 4 - button_width / 2, winHeight - 100, button_width, button_height)  # Centered on the right

    # Draw the buttons as rectangles
    pygame.draw.rect(win, BLACK, play_again_button)  # Draw Play Again button
    pygame.draw.rect(win, BLACK, quit_button)  # Draw Quit Game button

    play_again_label = lost_font.render('Play Again', 1, WHITE)
    quit_label = lost_font.render('Quit Game', 1, WHITE)

    win.blit(play_again_label, (play_again_button.x + (play_again_button.width / 2 - play_again_label.get_width() / 2), 
                                 play_again_button.y + (play_again_button.height / 2 - play_again_label.get_height() / 2)))
    win.blit(quit_label, (quit_button.x + (quit_button.width / 2 - quit_label.get_width() / 2), 
                           quit_button.y + (quit_button.height / 2 - quit_label.get_height() / 2)))

    pygame.display.update()  # Update the display to show the buttons

    # Button handling
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the function after quitting
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    again = False
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    return  # Exit the function after quitting
    reset()


def reset():
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()

#MAINLINE


# Setup buttons
increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = winHeight - 85
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = winHeight - 40
    buttons.append([WHITE, x, y, 20, True, 65 + i])
    # buttons.append([color, x_pos, y_pos, radius, visible, char])

word = randomWord()
inPlay = True

while inPlay:
    redraw_game_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
            if letter != None:
                guessed.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    if limbs != 5:
                        limbs += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()

# always quit pygame when done!
