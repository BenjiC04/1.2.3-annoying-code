import turtle as trtl

apple_image = "apple.gif"
screen_width = 400
screen_height = 400
apple_letters = []
apple_list = []
current_letter = "."
letter_list = ["a", "b", "c", "d"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)

wn.bgpic("background.gif")
wn.tracer(False)

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = (length_of_list - 1)
    active_apple.goto(0,0)
    current_letter = letter_list.pop(index)
    draw_apple(active_apple, current_letter)
    apple_letters.append(current_letter)


def write_letter(active_apple, letter):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() - 25 ,active_apple.ycor() - 50)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)


def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  write_letter(active_apple, letter)
  wn.update()


for i in range(0, 5):
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  reset_apple(active_apple)
  apple_list.append(active_apple)

def fall(letter):
  wn.tracer(True)
  index = apple_letters.index(letter)
  apple_letters.pop(index)
  active_apple = apple_list.pop(index)
  active_apple.goto(active_apple.xcor(), -200)
  active_apple.clear()
  active_apple.hideturtle()
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)


def check_apple_a():
  if ("a" in apple_letters):
    fall("a")

def check_apple_b():
  if ("b" in apple_letters):
    fall("b")

def check_apple_c():
  if ("c" in apple_letters):
    fall("c")

def check_apple_d():
  if ("d" in apple_letters):
    fall("d")



wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")


wn.listen()
trtl.mainloop()