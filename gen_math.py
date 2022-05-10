import math


def fun(x):
    return (0.1*x*x*x - 2*x*x + 10*math.sqrt(x))

def mkv(h, x1, e):
    xm = x1
    f0 = fun(x1 - h)
    f1 = fun(x1)
    f2 = fun(x1 + h)

    c = (f0 - 2*f1 + f2) / (2*h*h)
    b = ((-1)*f0*(2*x1 + h) + 4*f1*x1 - f2*(2*x1-h)) / (2*h*h)

    xm = (-1) * b / (2 * c)

    while ((xm - x1) < e):
        x1 = xm
        f0 = fun(x1 - h)
        f1 = fun(x1)
        f2 = fun(x1 + h)

        c = (f0 - 2*f1 + f2) / (2*h*h)
        b = ((-1)*f0*(2*x1 + h) + 4*f1*x1 - f2*(2*x1-h)) / (2*h*h)

        xm = (-1) * b / (2 * c)
    return [xm, fun(xm)]

def main():
    step = 1
    accuracy = 0.10
    x = 1

    result = mkv(step, x, accuracy)

    print(f"f({result[0]}) = {result[1]}")

main()
