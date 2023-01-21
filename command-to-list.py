"""
Gives arguments of shell command as python list for use in vs code launch.json
"""

while(True):
    x = input("command: ")

    x = x.replace(" ", "\",\n \"")

    print(f"[\n\"{x}\"\n]")
