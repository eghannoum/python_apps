import numpy
import matplotlib.pyplot as plt


def plot_mandelbrot(x, X, y, Y):
    delta = (X-x)/3000

    real, image = numpy.mgrid[x:X:delta, y:Y:delta]
    c = (real + 1j*image).reshape(image.shape[0], -1).T

    z = numpy.zeros_like(c, dtype=numpy.float64)
    escape = numpy.zeros_like(numpy.absolute(c), dtype=numpy.float64)

    for i in range(500):
        print(f'itter: {i}')
        z = z*z + c
        idx = (numpy.absolute(z) > 4) & (escape == 0)
        escape[idx] = i
    plt.imshow(escape, extent=(x, X, y, Y), cmap='CMRmap')


def plot_at(x, y, D):
    return plot_mandelbrot(x-D, x+D, y-D, y+D)


zoom = 0.5
plot_at(-0.725, -0.26, zoom)

plt.show()
