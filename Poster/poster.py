import arcade

#Declaring poster resolution
WIDTH = 1920
HEIGHT = 1080

#Declaring start coordinates for the chair, where x is x-axis and y is y-axis
x = 960
y = 360
#Declaring start coordinates for the text, where b is x-axis and c is y-axis
b = 400
c = 800

#Declaring movement of chair
vectora = 7

#Declaring movement of text, where h is horizontal and v is vertical
vectorhb = 4
vectorvb = 2

'''
Declaring image textures where:
img(x) = image
imgw(x) = original image width
imgh(x) = original image height
x = image
'''
imga = arcade.load_texture("images/trollchair.png")
imgwa = 262
imgha = 420
imgb = arcade.load_texture("images/floor.jpg")
imgwb = 294
imghb = 171
imgc = arcade.load_texture("images/setup.png")
imgwc = 671
imghc = 496
imgd = arcade.load_texture("images/wall.jpg")
imgwd = 1920
imghd = 1080
imge = arcade.load_texture("images/gamerfuel.png")
imgwe = 223
imghe = 600

#Button functions
button = [857, 535, 150, 50]
sound = False


#How the screen will refresh
def on_update(delta_time):
    #Insert the variables which will be modified
    global x
    global b
    global c
    global vectora
    global vectorhb
    global vectorvb

    #Determining horizontal movement for chair
    x += vectora
    #Determines the stop and reverse point
    if x < (imgwa / 2) or x > (WIDTH -  (imgwa / 2)):
        vectora *= -1

    #Determining horizontal movement for text
    b += vectorhb
    #Determines the stop and reverse point
    if b < 0 or b > WIDTH - 1075:
        vectorhb *= -1
    #Determining the vertical movement for text
    c += vectorvb
    #Determines the stop and reverse point
    if c < imghc + imghb + 15 or c > HEIGHT - 70:
        vectorvb *= -1


#This draws the circles in the background
def draw_circles():
    arcade.draw_circle_filled((WIDTH / 2), (imghb + 100), 30, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 4), (imghb + 800), 20, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 3), (imghb + 750), 10, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 5), (imghb + 600), 40, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 1.5), (imghb + 410), 50, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 1.2), (imghb + 300), 30, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 1.25), (imghb + 400), 20, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 2.1), (imghb + 660), 35, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 3.74), (imghb + 900), 15, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 1.8), (imghb + 360), 20, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 1.1), (imghb + 710), 10, arcade.color.WHITE)
    arcade.draw_circle_filled((WIDTH / 3.1), (imghb + 290), 60, arcade.color.WHITE)
    arcade.draw_circle_filled(200, (imghb + 100), 30, arcade.color.WHITE)

#This draws the rectangle which indicates the button hitbox
def draw_button():
    arcade.draw_xywh_rectangle_filled(button[0],
                                      button[1],
                                      button[2],
                                      button[3],
                                      arcade.color.BLUE)

#This just draws text in the button
def draw_button_text():
    arcade.draw_text("BUY NOW", 880, 550, arcade.color.WHITE, font_size = 20, font_name = "Impact", bold = True)

#This draws the chair
def draw_chair(x, y):
    arcade.draw_texture_rectangle(x, 240, imgwa, imgha, imga)

#This draws the floor
def draw_floor():
    arcade.draw_texture_rectangle((WIDTH / 2), (imghb / 2), 1920, imghb, imgb)

#This draws the gaming rig with PC in the background
def draw_rig():
    arcade.draw_texture_rectangle((WIDTH / 2), ((imghc / 2) + imghb), imgwc, imghc, imgc)

#This draws the wall
def draw_wall():
    arcade.draw_texture_rectangle((WIDTH / 2), (HEIGHT / 2), WIDTH, HEIGHT, imgd)

#This draws the can of monster energy on the table
def draw_drink():
    arcade.draw_texture_rectangle((((WIDTH / 2) + 15) - (imgwc / 2.25)), ((imghe / 10) + 375), (imgwe / 10), (imghe / 10), imge)

#This draws the moving text
def draw_text(b, c):
    arcade.draw_text("BUY THE ALL NEW TOXIC GAMING CHAIR!", b, c, arcade.color.NEON_GREEN, font_size = 50, font_name = "Impact", bold = True)

#This is the description in the lower-left corner
def draw_description():
    arcade.draw_text("Ever felt tired after a hard day of carrying? \n"
                     "Ever had back pains because of long grinding? \n"
                     "Ever felt like you lost because of bad posture? \n"
                     "Then we have the right product for you! \n"
                     "Our gaming chair has state of the art \n"
                     "ergonomics capable of supporting the most \n"
                     "demanding gamers and longest grinds.\n"
                     "Buy the all new TOXIC gaming chair for only \n"
                     "$1999.99 today, and say goodbye to back pains! \n"
                     "Our revolutionary product offers state \n"
                     "of the art variable back support, top tier \n"
                     "suspension for epic clutches, RGB lighting, \n"
                     "and built-in speakers. We also tossed \n"
                     "a back massage into the deal \n"
                     "and motors to drive your chair around!",
                     20, 666, arcade.color.PINK, font_size = 20, font_name = "Impact")

#This is the specs in the lower right corner
def draw_specs():
    arcade.draw_text("SPECS: \n"
                     "Height: 1.5 meters \n"
                     "Width: 0.6 meters \n"
                     "Length: 0.7 meters \n"
                     "Back Support: Yes \n"
                     "RGB: Yes \n"
                     "Suspension: Yes \n"
                     "Back Massage: Yes \n"
                     "Motors: Yes",
                     1320, 530, arcade.color.PINK, font_size = 25, font_name = "Impact")


#Starts to render the poster
def on_draw():
    #Positional arguments are where the stuff will move.
    arcade.start_render()
    draw_wall()
    draw_circles()
    draw_description()
    draw_specs()
    draw_text(b, c)
    draw_floor()
    draw_rig()
    draw_button()
    draw_button_text()
    draw_drink()
    draw_chair(x, y)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


#For the button
def on_mouse_press(x, y, button, modifiers):
    #Modify sound
    global sound
    #Redeclare button variables
    button_x = 857
    button_y = 535
    button_width = 150
    button_height = 50
    #Determines criteria for clicking the button, which is if the mouse lands and clicks in the button hitbox
    if (x > button_x and x < button_x + button_width and y > button_y and y < button_y + button_height):
        #Output on button click
        print("THANK YOU FOR YOUR PURCHASE.")
        print("Claim your product with the link below:")
        print("https://www.corsair.com/ca/en/gaming-chairs")
        #Plays background music once purchase is completed
        sound = True
    else:
        #If not clicked, then this shows up
        print("Are you interested in any other products?")

    #Plays the sound
    if sound:
        arcade.play_sound("sound/bgm.mp3")


def setup():
    arcade.open_window(WIDTH, HEIGHT, "The New ToXIC Gaming Chair")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

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