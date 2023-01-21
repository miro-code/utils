"""
Gives arguments of shell command as python list for use in vs code launch.json
"""

while(True):
    x = input("command: ")
    if(x == "exit" or x == "q"):
        break

    x = x.replace("\\", "/")

    print(x)
