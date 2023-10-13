from vpython import *

def kforce(p1,p2):
    k = 0.01
    r_vec = p1.pos-p2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    force_mag = k*p1.mass*p2.mass/r_mag**2
    force_vec = force_mag*r_hat
    return force_vec

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box(pos=vector(side, 0, 0), size=vector(thk, s2, s3),  color=color.red)
wallL = box(pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color=color.red)
wallB = box(pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color=color.blue)
wallT = box(pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color=color.blue)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7))

ball = sphere(color=color.green, radius=0.4, make_trail=True, retain=200, momentum=vector(0, 0, 0), pos=vector(0.1, 0.3, -0.2))
ball.mass = 1.0

ball_2 = sphere(color=color.green, radius=0.4, make_trail=True, retain=200, momentum=vector(0, 0, 0),pos=vector(-0.3, -0.1, 0.8))
ball_2.mass = 1.0

side = side - thk*0.5 - ball.radius

dt = 0.3
t = 0
while (True): #general loop
    rate(100)

    ball.force = kforce(ball, ball_2)
    ball_2.force = kforce(ball_2, ball)

    ball.momentum = ball.momentum + ball.force * dt
    ball_2.momentum = ball_2.momentum + ball_2.force * dt

    ball.pos = ball.pos + (ball.momentum / ball.mass) * dt
    ball_2.pos = ball_2.pos + (ball_2.momentum / ball_2.mass) * dt

    if not (side > ball.pos.x > -side):
        ball.momentum.x = -ball.momentum.x
    if not (side > ball.pos.y > -side):
        ball.momentum.y = -ball.momentum.y
    if not (side > ball.pos.z > -side):
        ball.momentum.z = -ball.momentum.z


    if not (side > ball_2.pos.x > -side):
        ball_2.momentum.x = -ball_2.momentum.x
    if not (side > ball_2.pos.y > -side):
        ball_2.momentum.y = -ball_2.momentum.y
    if not (side > ball_2.pos.z > -side):
        ball_2.momentum.z = -ball_2.momentum.z

    t = t + dt



