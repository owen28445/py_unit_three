#
#Owen Feng
# 7/11/2022
# unit 3 project, it is to make a rectangle.
def rectangle(number1, number2):
    return int(number1 * number2)

def instructure():
    print("the purpose of this program is to calculate the width, length and height")

def prism(h, w, l):
    '''
    this fuction can help to calculate the height, width and the length for the rectangle.
    :param h:height
    :param w:width
    :param l:length
    :return:
    '''
    top = int(rectangle(h, w))
    bottom = int(rectangle(h, w))

    front = int(rectangle(l, w))
    back = int(rectangle(l, w))

    leftside = int(rectangle(l, h))
    rightside = int(rectangle(l, h))

    total = top+bottom+front+back+leftside+rightside
    return total

def howbig():
    width = int((input("Please enter the width")))
    return width
def howlong():
    length = int((input("please enter the length")))
    return length
def howtall():
    height = int((input("please enter the height")))
    return height



def main():
    instructure()
    width = howbig()
    length = howlong()
    height = howtall()
    total = prism(width, length, height)
    print("The total is", total)



main()








