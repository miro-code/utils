"""
Gives arguments of shell command as python list for use in vs code launch.json
"""

while(True):
    x = input("command: ")

    x = x.replace(" ", "\", \"")

    print(f"[\"{x}\"]")
