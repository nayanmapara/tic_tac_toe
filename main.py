from ursina import *
from pynput.keyboard import  Key , Controller


app = Ursina()

camera.orthographic = True # This makes the objects look of standard size.
camera.fov = 4 # Zoom in or zoom out the window
camera.position = (1, 1) # camera postion coordinates
Text.default_resolution *= 2
window.title = 'Tic Tac Toe' # app title
player = Entity(name='o', color= color.rgb (192,192,192)) # object named player
cursor = Tooltip(player.name, color=player.color, origin=(0,0), scale=6, enabled=True) # mouse rules
cursor.background.color = color.clear # assigning no color to cursor background
bg = Entity(parent=scene, model='quad', texture=load_texture('images/bg_file.png'), scale=(10,6), z=10, color=color.light_gray) # background rules
mouse.visible = True # making mouse visible

# create a matrix to store the buttons in. makes it easier to check for victory
board = [[None for x in range(3)] for y in range(3)]

# Reload button reloads the code
reload_button = Button(parent=scene,color=color.white,position=(-1.4, 2),scale=(.5,.5),texture=load_texture('images/reload_image.png'))  # Colour defines colour of button on click

def reload_on_click(): # function to clear all the player input
    keyboard = Controller()
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)

reload_button.on_click = reload_on_click

for y in range(3): # creating the 3x3 grid
    for x in range(3): # creating the 3x3 grid
        b = Button(parent=scene, position=(x,y)) # creating the 3x3 grid
        board[x][y] = b # creating the 3x3 grid

        def on_click(b=b):
            b.text = player.name
            b.color = player.color
            b.collision = False # so objects overlay eachother
            check_for_victory()

            if player.name == 'o':
                player.name = 'x'
                player.color = color.rgb(218,165,32)# change to gold color
            else:
                player.name = 'o'
                player.color = color.rgb(192,192,192)# change to silver color

            cursor.text = player.name
            cursor.color = player.color

        b.on_click = on_click


def check_for_victory():
    name = player.name

    won = (
    (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or # across the bottom
    (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or # across the middle
    (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or # across the top
    (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or # down the left side
    (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or # down the middle
    (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or # down the right side
    (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or # diagonal /
    (board[0][2].text == name and board[1][1].text == name and board[2][0].text == name))   # diagonal \

    if won:
        print('Winner is: ', name)
        destroy(cursor) # for delay
        mouse.visible = True # enables to see the mouse
        Panel(z=1, scale=5, model='quad') #panel/ pop-up window details
        t = Text(f'player: {name}\nwon!', scale=3 , origin=(0,0), background=True) # details to show on pop-up window
        t.create_background(padding=(.5,.25), radius=Text.size/2)
        t.background.color = player.color.tint(-.1) # background blur of the pop-up window
        
        
app.run()
