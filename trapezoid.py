
import multiprocessing
import random as rd
import time
import threading

# Generating parameters for 10000 trapezoid: big base, small base and height
trapecoids = [[rd.randint(1, 200), rd.randint(
    1, 200), rd.randint(1, 200)] for i in range(10000)]

# Generating parameters for 10000 rectangles: width and height
rectangles = [[rd.randint(1, 200), rd.randint(1, 200)] for i in range(10000)]

# Generating parameters for 10000 squars
squars = [rd.randint(1, 200) for i in range(10000)]


# creating trapezoid class
class Trapezoid:

    def __init__(self, trap=[0, 0, 0]):
        self.a = min(trap)
        self.b = max(trap)
        self.h = sum(trap) - self.a - self.b

    def __str__(self):
        return 'ტოლფერდა ტრაპეციის დიდი ფუძეა -> {}, პატარა ფუძეა -> {}, ხოლო სიმაღლეა ->{}'.format(self.b, self.a, self.h)

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def area(self):
        return (self.a + self.b)/2 * self.h


# creating rectangle class which is child of trapezoid
class Rectangle(Trapezoid):
    def __init__(self, re=[0, 0]):
        super().__init__()
        self.x = re[0]
        self.y = re[1]

    def __str__(self):
        return "მართკუთხედის სიმაღლეა -> {}, ხოლო სიგანე -> {}".format(self.x, self.y)

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def area(self):
        return (self.x * self.y)


# creating square class which is child of rectangle
class Square(Rectangle):
    def __init__(self, c):
        super().__init__()
        self.c = c

    def __str__(self):
        return "კვადრატის გვერდია -> {}".format(self.c)

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def area(self):
        return (self.c * self.c)


# functions to calculate generate areas
def trapezoid_area():
    for i in range(10000):
        T = Trapezoid(trapecoids[i])
        # you can print here parameters if you want
        # print(T, T.area())


def rectangle_area():
    for i in range(10000):
        R = Rectangle(rectangles[i])
        # you can print here parameters if you want
        # print(R, R.area())


def square_area():
    for i in range(10000):
        S = Square(squars[i])
        # you can print here parameters if you want
        # print(S, S.area())


# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square in general without threads or processes
def regular():

    start = time.perf_counter()

    trapezoid_area()
    rectangle_area()
    square_area()

    finish = time.perf_counter()

    print('in general Finished in: ', round(finish - start, 2), 'second(s)')

# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square using threads


def threads():

    start1 = time.perf_counter()

    t1 = threading.Thread(target=trapezoid_area)
    t1.start()
    t2 = threading.Thread(target=rectangle_area)
    t2.start()
    t3 = threading.Thread(target=square_area)
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    finish1 = time.perf_counter()
    print('with threads Finished in: ', round(
        finish1 - start1, 2), 'second(s)')


# this function is used to calculate time to compute areas of 10000 trapezoid, rectangle and square using processes
def multiprocess():

    start2 = time.perf_counter()

    p1 = multiprocessing.Process(target=trapezoid_area())
    p2 = multiprocessing.Process(target=rectangle_area())
    p3 = multiprocessing.Process(target=square_area())

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    finish2 = time.perf_counter()
    print('with pools Finished in: ', round(finish2 - start2, 2), 'second(s)')


if __name__ == '__main__':
    regular()
    threads()
    multiprocess()
