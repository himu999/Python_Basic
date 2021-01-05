"""
Global variable can be use in local scope by using "global" :keyword
"""


def function():

    global a
    print(a+10)


a = 97


function()
