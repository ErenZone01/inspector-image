import sys
import maps
import steg as s
args = sys.argv
if args.__len__() > 1:
    match args[1]:
        case "--help" | "-h" :
            print("Welcome to inspector-image v1.0.0\n\nOPTIONS:\n    -map          Show the location\n    -steg         show the pgp key which is hidden in the image\n")
        case "-map":
            if args.__len__() != 3:
                print("Error Option")
                exit()
            image = args[2]
            if image.lower().endswith((".jpeg",".jpg", ".png", ".tif", ".wav", ".webp")) == False:
                print(image + " isn't an image !")
                exit()
            maps.extract_metadata(image)
        case "-steg":
            if args.__len__() != 3:
                print("Error Option")
                exit()
            image = args[2]
            if image.lower().endswith((".jpeg",".jpg", ".png", ".tif", ".wav", ".webp")) == False:
                print(image + " isn't an image !")
                exit()
            s.steg(image)