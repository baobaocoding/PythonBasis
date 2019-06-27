import random


toDoList = ['kiss David', 'hug David']


def dice(faces):
    """ this is a dice will generate number between [1, faces] """
    return random.randint(1, faces)


def toDo(number, threshold):
    """ determine what to do now when get this number (no return just print (to stdout))"""
    if number > threshold:
        print(toDoList[0])
    else:
        print(toDoList[1])


number = dice(6)
toDo(number, 3)
