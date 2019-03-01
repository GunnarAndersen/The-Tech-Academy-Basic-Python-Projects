

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    1st = []
    for i in color_list:
        msg = "(0) (1) (2)".format(name,mySentence,i)
        1st.append(msg)
    return 1st

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print ("You need to provide your name!")
        else:
            go = False
    1st = color_function(name)
    for i in 1st:
        print(i)

get_name()
