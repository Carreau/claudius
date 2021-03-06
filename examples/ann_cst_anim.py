from math import sqrt
from sys import argv

import numpy as np

import claudius
from claudius.plot import anim_field

dim = int(argv[1])
pde = argv[2]
δ = float(argv[3])
εc = float(argv[4])
μc = float(argv[5])
k = float(argv[6])
T = float(argv[7])
which = argv[8]

N = 128
C1, C2 = np.meshgrid(np.linspace(-T, T, num=N), np.linspace(-T, T, num=N))

if dim == 2:
    from claudius.Helmholtz_2d import create_problem_cst, scattered_field, total_field

    coord = claudius.to_polar(C1, C2)

if dim == 3:
    from claudius.Helmholtz_3d import create_problem_cst, scattered_field, total_field

    plan = argv[9]
    if plan == "XY":
        coord = claudius.to_spheric(C1, C2, 0)
    if plan == "XZ":
        coord = claudius.to_spheric(C1, 0, C2)

prob = create_problem_cst("Penetrable", (δ, 1), ((1, 1), (εc, μc)), k)
sol = claudius.solve_prob(prob, radius_max=sqrt(2) * T)

if which.startswith("S"):
    U = scattered_field(sol, *coord)
    type_field = "Scattered field"

if which.startswith("T"):
    U = total_field(sol, *coord)
    type_field = "Total field"

anim_field(prob, C1, C2, U, type_field)
