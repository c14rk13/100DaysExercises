import turtle

image_path = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image_path)

turtle.shape(image_path)


# Function to get and print out the x, y coordinates of where the mouse is clicked
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
