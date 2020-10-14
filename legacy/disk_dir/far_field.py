from accoster import M_trunc, sc_far_field
from accoster.disk_dir import solution
from numpy import amax, pi


def far_field(k, θ, M=None):
    if M is None:
        M = M_trunc(k, 4 * pi / k)

    sol = solution(k, M)
    return sc_far_field(k, sol, θ)