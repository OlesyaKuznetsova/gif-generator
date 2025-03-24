import imageio.v3 as iio

filenames = ['bunny1.png','bunny2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('bunny.gif', images, duration = 500, loop = 0)