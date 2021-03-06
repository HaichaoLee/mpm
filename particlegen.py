from math import sqrt
from numpy import random

template = "x:{},{},{} v:{},{},{} m:{},0,0\n"
text_file = open("./input/input_3d.in", "w")

# h = 0.075
# h = 0.01
# h = 0.0125
# h = 0.025
r = 0.15
start = [0.90 - r,1.0,0.3]
# start = [0.05 + r,0.5,0.3]

rho = 400;
snowvolfrac = 0.2
totParticles = 75000;
# totmass = 3.141592 * (r*r) * 0.005 * rho
totmass = 3.141592 * 4./3. * (r*r*r) * rho * snowvolfrac
# totmass = (h * 7) * (h * 7) * (h * 7) * rho 
# totmass = 3.14 * (2.5) * (2.5) * (h * 8) * rho
pos = []
# noise = 0.5;
# for i in range(-100,101):
#     for j in range(-100,101):
#         for k in range(-100,101):
#             if ( sqrt((h*i)*(h*i) + (h*j)*(h*j) + (h*k)*(h*k)) <= r ):
#                 pos.append([start[0] + h * (i + noise * (random.rand() - 1)), start[1] + h * (j + noise * (random.rand() - 1)), start[2] + h * (k + noise * (random.rand() - 1))])

while len(pos) < totParticles:

    posToAdd = (start[0] + 2 * (random.rand() - 0.5) * r, start[1] + 2 * (random.rand() - 0.5) * r, start[2] + 2 * (random.rand() - 0.5) * r)

    if sqrt( (posToAdd[0] - start[0]) * (posToAdd[0] - start[0]) +
             (posToAdd[1] - start[1]) * (posToAdd[1] - start[1]) + 
             (posToAdd[2] - start[2]) * (posToAdd[2] - start[2]) ) < r:
        pos.append(posToAdd)



# for i in range(-3,4):
#     for j in range(-3,4):
#         for k in range(10,13):
#             # if ( sqrt((h*i)*(h*i) + (h*j)*(h*j) + (h*k)*(h*k)) < r ):
#             pos.append([start[0] + h * i, start[1] + h * j, start[2] + h * k])

pmass = totmass / len(pos);

for p in pos:
    # if p[2] > 2.3 :
    #     text_file.write(template.format(p[0],p[1],p[2],
    #                                     0,0,-10.,
    #                                     pmass))
    # else:
    #     text_file.write(template.format(p[0],p[1],p[2],
    #                                     0,0,0.,
    #                                     pmass))
    text_file.write(template.format(p[0],p[1],p[2],
                                    -5,0,-1,
                                    pmass))

print("{} particles generated. total mass : {} kg".format(len(pos),totmass))

text_file.close()
