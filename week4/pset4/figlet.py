from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
argvf = ['-f', '--font']


if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] in argvf and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


i = input("Input: ")
figlet.setFont(font=font)
print("Output:\n", figlet.renderText(i))

