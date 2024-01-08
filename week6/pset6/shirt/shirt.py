import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        extensions = ['.jpg', '.jpeg', '.png']
        ex1 = os.path.splitext(sys.argv[1])
        ex2 = os.path.splitext(sys.argv[2])
        if ex1[1] == ex2[1] and ex1[1] in extensions:
            try:
                im = Image.open(sys.argv[1])
                shirt = Image.open('shirt.png')
                im = ImageOps.fit(im, size=shirt.size)
                im.paste(shirt, shirt)
                im.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit('Input does not exist')
        elif ex2[1] not in extensions:
            sys.exit('Invalid output')
        else:
            sys.exit('Input and output have different extensions')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

if __name__ == '__main__':
    main()
