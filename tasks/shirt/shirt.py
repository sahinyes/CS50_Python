from PIL import Image, ImageOps
import sys

if len(sys.argv) == 3:
    a = sys.argv[1].split(".")[1]
    b = sys.argv[2].split(".")[1]
    if a == b:
        if b in ["jpg", "jpeg", "png"]:
            try:
                image = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Input does not exist")
            shirt = Image.open("shirt.png")
            size = shirt.size
            puppet = ImageOps.fit(image, size)
            puppet.paste(shirt, shirt)
            puppet.save(sys.argv[2])
        else:
            sys.exit("Invalid Output")
    else:
        sys.exit("Input and output have different extensions")

elif len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
