import turtle
import math

bob = turtle.Turtle()
tau = 2 * math.pi

def polygon(t, n = 4, length = 100):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r, N = 100):
    polygon(t, tau * r / N, N)

def arc(t, r, angle, N = 100):
    rad = tau * angle / 360
    n = math.floor(N * rad / tau)
    l = tau * r / N

    for _ in range(n):
        t.fd(l)
        t.lt(360/N)

def isoceles(t, angle1, length = 100):
    angle1_rad = angle1 * tau / 360
    angle2 = (180. - angle1) / 2.
    L = 2 * length * math.sin(angle1_rad / 2)
    
    t.fd(length)
    t.lt(180 - angle2)
    t.fd(L)
    t.lt(180 - angle2)
    t.fd(length)

def pie(t, N, length = 100):
    for _ in range(N):
        isoceles(t, 360/N, length)
        t.lt(180)


number = int(input())
pie(bob, number)

turtle.mainloop()

