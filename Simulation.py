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

def update_time(dtt):
    global dt
    dt = dtt.value

def update_coe(coe):
    global inv_damping_coefficient
    inv_damping_coefficient = coe.value

def update_size(size):
    global charges_radius, side, charges
    charges_radius = size.value
    side = start_side - thk*0.5 - charges_radius
    for charge in charges:
        charge.radius = charges_radius

side = 4.0
start_side = side
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box(pos=vector(side, 0, 0), size=vector(thk+0.01, s2+0.01, s3+0.01),  color=color.gray(1), opacity=0.1)
wallL = box(pos=vector(-side, 0, 0), size=vector(thk+0.01, s2+0.01, s3+0.01),  color=color.gray(1), opacity=0.1)
wallB = box(pos=vector(0, -side, 0), size=vector(s3+0.01, thk+0.01, s3+0.01),  color=color.gray(1), opacity=0.1)
wallT = box(pos=vector(0,  side, 0), size=vector(s3+0.01, thk+0.01, s3+0.01),  color=color.gray(1), opacity=0.1)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2+0.01, s2+0.01, thk+0.01), color=color.gray(1), opacity=0.1)

charges = []
number_of_charges = 100
charges_radius = 0.4
for i in range(number_of_charges):
    r_value_1 = uniform(-1, 1)*2
    r_value_2 = uniform(-1, 1)*2
    r_value_3 = uniform(-1, 1)*2
    charges.append(sphere(color=color.green, radius=charges_radius, make_trail=False, retain=200, momentum=vector(0, 0, 0), pos=vector(r_value_1, r_value_2, r_value_3), mass=1))

side = side - thk*0.5 - charges_radius
dt = 0.01
t = 0
inv_damping_coefficient = 1

slider(min=0, max=1, value=0, step=0.01, bind=update_time, name="Time")
slider(min=0, max=1, value=0, step=0.01, bind=update_coe, name="Damping coefficient")
slider(min=0, max=1, value=0, step=0.01, bind=update_size, name="Charges size")
while (True): #general loop
    rate(100)

    for charge in charges:
        charge.force = vector(0, 0, 0)
        for product in range(number_of_charges):
            if charge != charges[product]:
                charge.force += kforce(charge, charges[product])

        charge.momentum = charge.momentum + charge.force * dt

        charge.pos = charge.pos + charge.momentum / charge.mass * dt

        if not (side > charge.pos.x > -side):
            charge.momentum.x = -charge.momentum.x * inv_damping_coefficient
            if charge.pos.x > side:
                charge.pos.x = charge.pos.x - 0.1
            if charge.pos.x < -side:
                charge.pos.x = charge.pos.x + 0.1
        if not (side > charge.pos.y > -side):
            charge.momentum.y = -charge.momentum.y * inv_damping_coefficient
            if charge.pos.y > side:
                charge.pos.y = charge.pos.y - 0.1
            if charge.pos.y < -side:
                charge.pos.y = charge.pos.y + 0.1
        if not (side > charge.pos.z > -side):
            charge.momentum.z = -charge.momentum.z * inv_damping_coefficient
            if charge.pos.z > side:
                charge.pos.z = charge.pos.z - 0.1
            if charge.pos.z < -side:
                charge.pos.z = charge.pos.z + 0.1

    t = t + dt



