# Owen Feng
# 7/11/2022
# unit 3 project, it is to make a rectangle.
def rectangle(number1, number2):
    return int(number1 * number2)

def prism(h, w, l):
    top = int(rectangle(h, w))
    bottom = int(rectangle(h, w))

    front = int(rectangle(l, w))
    back = int(rectangle(l, w))

    leftside = int(rectangle(l, h))
    rightside = int(rectangle(l, h))

    total = top+bottom+front+back+leftside+rightside
    return total

def main():
    width = int((input("Please enter the width")))

    length = int((input("please enter the length")))

    height = int((input("please enter the height")))

    totalSurface = prism(width, length, height)
    print("The total is", totalSurface)


main()








