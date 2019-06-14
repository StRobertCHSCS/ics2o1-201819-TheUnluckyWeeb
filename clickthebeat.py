import arcade


'''
Screen resolution
'''
WIDTH = 1920
HEIGHT = 1080


'''
The following is used to declare all booleans necessary for the code to run.
'''

#If the game started
game_start = False

#If the left key is pressed
left_pressed = False

#If the down key is pressed
down_pressed = False

#If the right key is pressed
right_pressed = False

#If the left noteblock is generated
lineone = False

#If the right noteblock is generated
linetwo = False

#If the right noteblock is generated
linethree = False

#If the 10th combo is reached
nice = False

#If the sound effect for 10th combo is played
play_comboten_sound = False

#If the user failed the game yet
death = False

#If the sound effect for failing is played
play_failsound = False


'''
The following will load all textures required for the code.
'''

#Texture for endscreen
failscreen = arcade.load_texture("textures/failscreen.jpg")

#Textures for the three different backgrounds
background = arcade.load_texture("textures/background.jpg")
backgroundtwo = arcade.load_texture("textures/backgroundtwo.jpg")
backgroundthree = arcade.load_texture("textures/backgroundthree.png")

#Loads the unique coloring for the maplines and hitboxes
mapline = arcade.load_texture("textures/maplines.jpg")

#Texture for key indicators (arrow signs)
leftarrow = arcade.load_texture("textures/left.png")
downarrow = arcade.load_texture("textures/down.png")
rightarrow = arcade.load_texture("textures/right.png")

#Texture and information for tenth combo animation
comboten = arcade.load_texture("textures/comboten.png")
comboten_width = 500
comboten_height = 740
comboten_x = 0 - comboten_width/2
comboten_y = comboten_height/2
comboten_axis = 25
excellent = arcade.load_texture("textures/excellent.png")
excellent_width = 490
excellent_height = 80

#Texture and information for triangle on exit and restart button
exitbutton = arcade.load_texture("textures/exitbutton.png")
exitbutton_width = 200
exitbutton_height = 200


'''
The following will load all sound effects in the code.
'''

#Sound effect for each hit
hitsound = arcade.load_sound("effects/hitsound.mp3")

#Sound effect for ever 10 combo
comboten_sound = arcade.load_sound("effects/holycow.mp3")

#Sound effect for failing
failsound = arcade.load_sound("effects/failsound.mp3")


'''
The following will provide the positional information for each object in the code
'''

#Hitline placement combined with hitbox declaration
hitbox_horizontal = 960
hitbox_top = 300
hitbox_bottom = 100

#Beat lines, where the 3 noteblocks will be centered on the x axis
left = 320
middle = 960
right = 1600

#Vertical beat locations, which will change as the game progresses
hitline_origin = HEIGHT + 50
hitline_one = hitline_origin
hitline_two = hitline_origin
hitline_three = hitline_origin

#Initial approach rate, or speed of beat movement
approach_rate = 5

#Indicates positional information of exit button hitboxes
exitbutton_hitbox = [WIDTH*(1/3) - 100, HEIGHT/6 - 100, 200, 200]
exitbutton_hitbox_two = [WIDTH*(2/3) - 100, HEIGHT/6 - 100, 200, 200]


'''
The following will calculate the score.
'''

#Initial hit counter
counter = 0

#Initial score
score = 0

#Initial score increase per hit
scoreincrease = 1

#Displayed score
scoremeter = 0

#Displayed measurement for score
scoremeasure = "Bytes"



'''
This is similar to a loop, which repeats ever sixtieth of a second.
'''

def on_update(delta_time):

    #This brings in the necessary variables from earlier to modify
    global hitline_one
    global hitline_two
    global hitline_three
    global lineone
    global linetwo
    global linethree
    global approach_rate
    global death
    global nice
    global comboten_x
    global comboten_axis
    global scoremeter
    global scoremeasure
    global play_failsound
    global play_comboten_sound

    #This first confirms that the game has started before anything happens
    if game_start:

        # Adds the failure condition
        if hitline_one < hitbox_bottom or hitline_two < hitbox_bottom or hitline_three < hitbox_bottom:
            death = True

        #Confirms that the player did not fail before displaying score
        if not(death):

            #Uses the score to determine the optimal measurement for the scoremeasure before modifying and displaying it
            if score >= 1024**5:
                scoremeter = score/(1024**5)
                scoremeasure = "Petabytes"
            elif score >= 1024**4:
                scoremeter = score/(1024**4)
                scoremeasure = "Terabytes"
            elif score >= 1024**3:
                scoremeter = score/(1024**3)
                scoremeasure = "Gigabytes"
            elif score >= 1024**2:
                scoremeter = score/(1024**2)
                scoremeasure = "Megabytes"
            elif score >= 1024:
                scoremeter = score/(1024)
                scoremeasure = "Kilobytes"
            elif score < 1024:
                scoremeter = score
                scoremeasure = "Bytes"

        #Determines which noteblock to generate
        if counter  % 3 == 0 and not(death):
            linethree = True
        elif counter % 2 == 0 and not(death):
            linetwo = True
        elif counter % 1 == 0 and not(death):
            lineone = True

        #Determines movement of noteblocks, or resets the noteblock to original position if it's not generated
        if lineone and not (death):
            hitline_one -= approach_rate
        elif not (lineone) or death:
            hitline_one = hitline_origin
        if linetwo and not (death):
            hitline_two -= approach_rate
        elif not (linetwo) or death:
            hitline_two = hitline_origin
        if linethree and not (death):
            hitline_three -= approach_rate
        elif not (linethree) or death:
            hitline_three = hitline_origin

        #Determines if the tenth hit has been reached based on division of ten, and modifies the variable
        if (counter) % 10 == 0 and counter > 0:
            nice = True
        #Once the user is past the 10th hit, the combo animations are stopped
        else:
            comboten_axis = 20
            comboten_x = 0 - comboten_width / 2
            nice = False
            play_comboten_sound = False

        #If the tenth hit has been reached, the code can then proceed to do the animation
        if nice:
            comboten_x += comboten_axis
            if comboten_x > comboten_width/5:
                comboten_axis *= -1



        #Adds the condition for playing the 10th combo sound effect
        if nice and not(play_comboten_sound):
            arcade.play_sound(comboten_sound)
            play_comboten_sound = True

        #Determines the condition for playing the fail sound effect
        if death and not(play_failsound):
            arcade.sound.play_sound(failsound)
            play_failsound = True




'''
The following contains the information for each visual element which will be used in on_draw
'''

#This draws the starting screen
def startscreen():
    arcade.draw_text("Rhythm Bytes", 470, 600, arcade.color.SILVER, font_size = 100, font_name = "Verdana")
    hitline()
    arcade.draw_text("Press space to begin", 610, 500, arcade.color.SILVER, font_size = 50, font_name = "Verdana")

#This draws the first background picture
def backgroundpicture():
    arcade.draw_texture_rectangle(960, 540, 1920, 1080, background)

#This draws the second background picture
def backgroundpicturetwo():
    arcade.draw_texture_rectangle(960, 540, 1920, 1080, backgroundtwo)

#This draws the third background picture
def backgroundpicturethree():
    arcade.draw_texture_rectangle(960, 540, 1920, 1080, backgroundthree)

#Draws left noteblock
def hitbox_one(left, hitline_one):
    arcade.draw_texture_rectangle(left, hitline_one, 640, 25, mapline)

#Draws middle noteblock
def hitbox_two(middle, hitline_two):
    arcade.draw_texture_rectangle(middle, hitline_two, 640, 25, mapline)

#Draws right noteblock
def hitbox_three(right, hitline_three):
    arcade.draw_texture_rectangle(right, hitline_three, 640, 25, mapline)


#Draws the maplines
def hitline():
    arcade.draw_texture_rectangle(hitbox_horizontal, (hitbox_top + hitbox_bottom)/2, 1920, 2, mapline)
    arcade.draw_texture_rectangle(640, 540, 2, 1080, mapline)
    arcade.draw_texture_rectangle(1280, 540, 2, 1080, mapline)

#Draws the key indicators
def arrows():
    arcade.draw_texture_rectangle(320, hitbox_bottom, 100, 100, leftarrow)
    arcade.draw_texture_rectangle(960, hitbox_bottom, 100, 100, downarrow)
    arcade.draw_texture_rectangle(1600, hitbox_bottom, 100, 100, rightarrow)

#Draws the key press effects
def leftlineclick():
    arcade.draw_texture_rectangle(320, hitbox_bottom, 640, 200, mapline)
def midlineclick():
    arcade.draw_texture_rectangle(960, hitbox_bottom, 640, 200, mapline)
def rightlineclick():
    arcade.draw_texture_rectangle(1600, hitbox_bottom, 640, 200, mapline)

#Displays the score
def points():
    arcade.draw_text(str(round(scoremeter, 3)), 50, 1000, arcade.color.SILVER, font_size = 50, font_name = "Verdana")
    arcade.draw_text(scoremeasure, 375, 1000, arcade.color.SILVER, font_size = 50, font_name = "Verdana")
    arcade.draw_text(str(counter), 50, 900, arcade.color.SILVER, font_size = 50, font_name = "Verdana")
    arcade.draw_text("Hits", 370, 900, arcade.color.SILVER, font_size = 50, font_name = "Verdana")

#Draws the 10th combo effects
def combotenani(comboten_x, comboten_y):
    arcade.draw_texture_rectangle(comboten_x, comboten_y, comboten_width, comboten_height, comboten)
    arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, excellent_width, excellent_height, excellent)

#Draws the endscreen
def endscreen():
    arcade.draw_texture_rectangle(960, 540, 1920, 1080, failscreen)
    arcade.draw_text("Game Over", 600, 900, arcade.color.SILVER, font_size = 100, font_name = "Verdana")
    arcade.draw_text("Score:", 400, 700, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_text(str(round(scoremeter, 3)), 900, 700, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_text(scoremeasure, 1250, 700, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_text("Bytes:", 400, 500, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_text(str(round(score)), 900, 500, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_text("Hits:", 400, 300, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_text(str(counter), 900, 300, arcade.color.SILVER, font_size = 60, font_name = "Verdana")
    arcade.draw_texture_rectangle(WIDTH*(1/3), HEIGHT/6, exitbutton_width, exitbutton_height, exitbutton)
    arcade.draw_texture_rectangle(WIDTH*(2/3), HEIGHT / 6, exitbutton_width, exitbutton_height, exitbutton)
    arcade.draw_text("Exit", WIDTH*(1/3) - 20, HEIGHT/6 - 30, arcade.color.SILVER, font_size = 20, font_name = "Verdana")
    arcade.draw_text("Restart", WIDTH * (2/3) - 45, HEIGHT / 6 - 30, arcade.color.SILVER, font_size = 20, font_name="Verdana")




'''
The following will actually create the game and all visual elements
'''
def on_draw():
    arcade.start_render()

    #Determines and draws the background based on the noteblock movement speed
    if approach_rate >= 30:
        backgroundpicturethree()
    elif approach_rate >= 15:
        backgroundpicturetwo()
    else:
        backgroundpicture()

    #Draws the key indicators
    arrows()

    #Draws the start screen under the condition that the game did not start yet
    if not(game_start):
        startscreen()

    #Once the game has started, the other elements in the game can be drawn
    if game_start:

        #Draws the score meter
        points()

        #Draws the hitlines
        hitline()

        #Determines and draws each key press effect
        if left_pressed:
            leftlineclick()
        if down_pressed:
            midlineclick()
        if right_pressed:
            rightlineclick()

        #Determines and draws a noteblock
        if linethree:
            hitbox_three(right, hitline_three)
        elif linetwo:
            hitbox_two(middle, hitline_two)
        elif lineone:
            hitbox_one(left, hitline_one)

        #Draws the 10th combo animations
        if nice:
            combotenani(comboten_x, comboten_y)

        #Draws the endscreen on the condition that the user failed the game
        if death:
            endscreen()




'''
The following will do the necessary actions if a key is pressed
'''
def on_key_press(key, modifiers):

    #Imports the necessary variables to modify
    global counter
    global lineone
    global linetwo
    global linethree
    global score
    global death
    global hitline_one
    global hitline_two
    global hitline_three
    global game_start
    global approach_rate
    global left_pressed
    global down_pressed
    global right_pressed
    global scoreincrease


    #This will start the game if space key is pressed
    if key == arcade.key.SPACE and not(game_start):
        arcade.pause(1)
        game_start = True

    #This determines if left key is pressed before performing additional actions
    if key == arcade.key.LEFT and game_start and not(death):
        left_pressed = True

        #These are the conditions for a hit, and actions to follow
        if hitline_one >= hitbox_bottom and hitline_one <= hitbox_top:
            arcade.play_sound(hitsound)
            counter += 1
            score += scoreincrease
            scoreincrease *= 1.2
            lineone = False
            if approach_rate <= 30:
                approach_rate += 0.5

        #This determines if the user clicked too early or too late, and fails them if they did
        else:
            death = True
            lineone = False


    #Determines if down key is pressed before additional actions
    if key == arcade.key.DOWN and game_start and not(death):
        down_pressed = True

        #First checks if the conditions for a hit has been met before taking any additional actions
        if hitline_two >= hitbox_bottom and hitline_two <= hitbox_top:
            arcade.play_sound(hitsound)
            counter += 1
            score += scoreincrease
            scoreincrease*= 1.2
            linetwo = False
            if approach_rate <= 30:
                approach_rate += 0.5

        #If the conditions are not met, a miss will be counted and the user is failed
        else:
            death = True
            linetwo = False


    #Determines if the right key is pressed before taking any additional actions
    if key == arcade.key.RIGHT and game_start and not(death):
        right_pressed = True

        #Determines if the conditions for a hit is met, and takes the actions
        if hitline_three >= hitbox_bottom and hitline_three <= hitbox_top:
            arcade.play_sound(hitsound)
            counter += 1
            score += scoreincrease
            scoreincrease *= 1.2
            linethree = False
            if approach_rate <= 30:
                approach_rate += 0.5

        #If the conditions are not met, the user is autofailed.
        else:
            death = True
            linethree = False


def on_key_release(key, modifiers):

    #Imports the necessary variables to modify
    global left_pressed
    global down_pressed
    global right_pressed

    #Actions for left key
    if key == arcade.key.LEFT:
        left_pressed = False

    #Actions for middle key
    if key == arcade.key.DOWN:
        down_pressed = False

    #Actions for right key
    if key == arcade.key.RIGHT:
        right_pressed = False




'''
The following will take care of button click interactions
'''
def on_mouse_press(x, y, button, modifiers):

    #Imports the variables to modify
    global death
    global play_comboten_sound
    global score
    global counter
    global nice
    global lineone
    global linetwo
    global linethree
    global approach_rate
    global play_failsound
    global scoreincrease


    #Unpacks the information contained in the two variables
    exitbox_left, exitbox_bottom, exitbox_width, exitbox_height = exitbutton_hitbox
    exitbox_leftb, exitbox_bottomb, exitbox_widthb, exitbox_heightb = exitbutton_hitbox_two


    #Determines if the user clicked the exit button before performing an action
    if (x > exitbox_left and x < (exitbox_left + exitbox_width) and y > exitbox_bottom and y < exitbox_bottom + exitbox_width):
        exit("clickthebeat.py")


    #Determines if the user clicked the restart button before performing an action
    if (x > exitbox_leftb and x < (exitbox_leftb + exitbox_widthb) and y > exitbox_bottomb and y < (exitbox_bottomb + exitbox_heightb)):
        death = False
        play_failsound = False
        play_comboten_sound = False
        score = 0
        scoreincrease = 1
        counter = 1
        approach_rate = 5
        nice = False
        lineone = False
        linetwo = False
        linethree = False




def setup():
    arcade.open_window(WIDTH, HEIGHT, "Rhythm Bytes")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/240)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
