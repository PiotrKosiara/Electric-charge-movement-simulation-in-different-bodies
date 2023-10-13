from vpython import *
from random import uniform

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

charges = []
number_of_charges = 1000
charges_radius = 0.05
for i in range(number_of_charges):
    r_value_1 = uniform(-1, 1)*side
    r_value_2 = uniform(-1, 1)*side
    r_value_3 = uniform(-1, 1)*side
    charges.append(sphere(color=color.green, radius=charges_radius, make_trail=False, momentum=vector(0, 0, 0), pos=vector(r_value_1, r_value_2, r_value_3), mass=1.0))

side = side - thk*0.5 - charges_radius
dt = 0.3
t = 0
while (True): #general loop
    rate(100)

    for charge in charges:
        charge.force = vector(0, 0, 0)
    for charge in charges:
        for product in range(number_of_charges):
            if charge != charges[product]:
                charge.force += kforce(charge, charges[product])

    for charge in charges:
        charge.momentum = charge.momentum + charge.force * dt

    for charge in charges:
        charge.pos = charge.pos + charge.momentum / charge.mass * dt

    for charge in charges:
        if not (side > charge.pos.x > -side):
            charge.momentum.x = -charge.momentum.x
        if not (side > charge.pos.y > -side):
            charge.momentum.y = -charge.momentum.y
        if not (side > charge.pos.z > -side):
            charge.momentum.z = -charge.momentum.z


    t = t + dt



