from PIL import Image
import readdigit

# Load the PNG file
image = Image.open("digit3.png")

# Convert the image to the expected format and pass it to the convert function
readdigit.convert(None, None, "output.csv", image.convert("L"))

def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

convert("digit3.png", "t10k-labels-idx1-ubyte",
        "mnist_test.csv", 10000)
