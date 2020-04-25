from Moves import u, uprime, r, rprime, f, fprime, d, dprime, l, lprime, b, bprime


def cross(up, right, front, down, left, back):
    """Return the moves to produce a cross on the bottom layer"""
    solution = []

    white_edges = ["D2", "D4", "D6", "D8"]
    white_slots = ["d2", "d4", "d6", "d8"]
    counter = 0
    for white_edge in white_edges:
        if white_edge in down.values():
            counter += 1
    if counter >= 1:
        correct_edges = []
        correct_edgesd = []
        correct_edgesdprime = []
        correct_edgesd2 = []
        for j in range(0, 4):
            if white_edges[j] in down[white_slots[j]]:
                correct_edges.append(white_edges[j])
        d(right, front, down, left, back)
        for j in range(0, 4):
            if white_edges[j] in down[white_slots[j]]:
                correct_edgesd.append(white_edges[j])
        dprime(right, front, down, left, back)
        dprime(right, front, down, left, back)
        for j in range(0, 4):
            if white_edges[j] in down[white_slots[j]]:
                correct_edgesdprime.append(white_edges[j])
        dprime(right, front, down, left, back)
        for j in range(0, 4):
            if white_edges[j] in down[white_slots[j]]:
                correct_edgesd2.append(white_edges[j])
        dprime(right, front, down, left, back)
        dprime(right, front, down, left, back)
        if len(correct_edgesd) > len(correct_edges):
            d(right, front, down, left, back)
            solution.append("D")
        if len(correct_edgesdprime) > len(correct_edges):
            dprime(right, front, down, left, back)
            solution.append("D'")
        if len(correct_edgesd2) > len(correct_edges):
            d(right, front, down, left, back)
            d(right, front, down, left, back)
            solution.append("D2")
    if "D2" not in down["d2"]:
        if "D2" in up.values():
            if "D2" in up["u2"]:
                    solution.append("U2")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D2" in up["u4"]:
                    solution.append("U'")
                    solution.append("F2")
                    uprime(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D2" in up["u6"]:
                    solution.append("U")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D2" in up["u8"]:
                    solution.append("F2")
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
        if "D2" in left.values():
            if "D2" in left["l2"]:
                    solution.append("L")
                    solution.append("F'")
                    solution.append("L'")
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    lprime(up, front, down, left, back)
            if "D2" in left["l4"]:
                    solution.append("L2")
                    solution.append("F'")
                    solution.append("L2")
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
            if "D2" in left["l6"]:
                    solution.append("F'")
                    fprime(up, right, front, down, left)
            if "D2" in left["l8"]:
                    solution.append("L'")
                    solution.append("F'")
                    lprime(up, front, down, left, back)
                    fprime(up, right, front, down, left)
        if "D2" in right.values():
            if "D2" in right["r2"]:
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D2" in right["r4"]:
                    solution.append("F")
                    f(up, right, front, down, left)
            if "D2" in right["r6"]:
                    solution.append("R2")
                    solution.append("F")
                    solution.append("R2")
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
            if "D2" in right["r8"]:
                    solution.append("R")
                    solution.append("F")
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
        if "D2" in front.values():
            if "D2" in front["f2"]:
                    solution.append("F")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    f(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D2" in front["f4"]:
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D2" in front["f6"]:
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D2" in front["f8"]:
                    solution.append("F'")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    fprime(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D2" in back.values():
            if "D2" in back["b2"]:
                    solution.append("U")
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    u(up, right, front, left, back)
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D2" in back["b4"]:
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D2" in back["b6"]:
                    solution.append("D'")
                    solution.append("L'")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    lprime(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D2" in back["b8"]:
                    solution.append("B")
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D2" in down.values():
            if "D2" in down["d4"]:
                    solution.append("L'")
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    lprime(up, front, down, left, back)
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D2" in down["d6"]:
                    solution.append("R")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    r(up, right, front, down, back)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D2" in down["d8"]:
                    solution.append("B")
                    solution.append("D2")
                    solution.append("B'")
                    solution.append("D2")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
                    bprime(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
    if "D4" not in down["d4"]:
        d(right, front, down, left, back)
        solution.append("D")
        if "D4" in up.values():
            if "D4" in up["u2"]:
                    solution.append("U2")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D4" in up["u4"]:
                    solution.append("U'")
                    solution.append("F2")
                    uprime(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D4" in up["u6"]:
                    solution.append("U")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D4" in up["u8"]:
                    solution.append("F2")
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
        if "D4" in left.values():
            if "D4" in left["l2"]:
                    solution.append("L")
                    solution.append("F'")
                    solution.append("L'")
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    lprime(up, front, down, left, back)
            if "D4" in left["l4"]:
                    solution.append("L2")
                    solution.append("F'")
                    solution.append("L2")
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
            if "D4" in left["l6"]:
                    solution.append("F'")
                    fprime(up, right, front, down, left)
            if "D4" in left["l8"]:
                    solution.append("L'")
                    solution.append("F'")
                    lprime(up, front, down, left, back)
                    fprime(up, right, front, down, left)
        if "D4" in right.values():
            if "D4" in right["r2"]:
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D4" in right["r4"]:
                    solution.append("F")
                    f(up, right, front, down, left)
            if "D4" in right["r6"]:
                    solution.append("R2")
                    solution.append("F")
                    solution.append("R2")
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
            if "D4" in right["r8"]:
                    solution.append("R")
                    solution.append("F")
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
        if "D4" in front.values():
            if "D4" in front["f2"]:
                    solution.append("F")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    f(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D4" in front["f4"]:
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D4" in front["f6"]:
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D4" in front["f8"]:
                    solution.append("F'")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    fprime(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D4" in back.values():
            if "D4" in back["b2"]:
                    solution.append("U")
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    u(up, right, front, left, back)
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D4" in back["b4"]:
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D4" in back["b6"]:
                    solution.append("D'")
                    solution.append("L'")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    lprime(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D4" in back["b8"]:
                    solution.append("B")
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D4" in down.values():
            if "D4" in down["d4"]:
                    solution.append("L'")
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    lprime(up, front, down, left, back)
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D4" in down["d6"]:
                    solution.append("R")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    r(up, right, front, down, back)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D4" in down["d8"]:
                    solution.append("B")
                    solution.append("D2")
                    solution.append("B'")
                    solution.append("D2")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
                    bprime(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
        dprime(right, front, down, left, back)
        solution.append("D'")
    if "D6" not in down["d6"]:
        dprime(right, front, down, left, back)
        solution.append("D'")
        if "D6" in up.values():
            if "D6" in up["u2"]:
                    solution.append("U2")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D6" in up["u4"]:
                    solution.append("U'")
                    solution.append("F2")
                    uprime(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D6" in up["u6"]:
                    solution.append("U")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D6" in up["u8"]:
                    solution.append("F2")
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
        if "D6" in left.values():
            if "D6" in left["l2"]:
                    solution.append("L")
                    solution.append("F'")
                    solution.append("L'")
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    lprime(up, front, down, left, back)
            if "D6" in left["l4"]:
                    solution.append("L2")
                    solution.append("F'")
                    solution.append("L2")
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
            if "D6" in left["l6"]:
                    solution.append("F'")
                    fprime(up, right, front, down, left)
            if "D6" in left["l8"]:
                    solution.append("L'")
                    solution.append("F'")
                    lprime(up, front, down, left, back)
                    fprime(up, right, front, down, left)
        if "D6" in right.values():
            if "D6" in right["r2"]:
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D6" in right["r4"]:
                    solution.append("F")
                    f(up, right, front, down, left)
            if "D6" in right["r6"]:
                    solution.append("R2")
                    solution.append("F")
                    solution.append("R2")
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
            if "D6" in right["r8"]:
                    solution.append("R")
                    solution.append("F")
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
        if "D6" in front.values():
            if "D6" in front["f2"]:
                    solution.append("F")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    f(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D6" in front["f4"]:
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D6" in front["f6"]:
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D6" in front["f8"]:
                    solution.append("F'")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    fprime(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D6" in back.values():
            if "D6" in back["b2"]:
                    solution.append("U")
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    u(up, right, front, left, back)
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D6" in back["b4"]:
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D6" in back["b6"]:
                    solution.append("D'")
                    solution.append("L'")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    lprime(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D6" in back["b8"]:
                    solution.append("B")
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D6" in down.values():
            if "D6" in down["d4"]:
                    solution.append("L'")
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    lprime(up, front, down, left, back)
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D6" in down["d6"]:
                    solution.append("R")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    r(up, right, front, down, back)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D6" in down["d8"]:
                    solution.append("B")
                    solution.append("D2")
                    solution.append("B'")
                    solution.append("D2")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
                    bprime(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
        d(right, front, down, left, back)
        solution.append("D")
    if "D8" not in down["d8"]:
        d(right, front, down, left, back)
        d(right, front, down, left, back)
        solution.append("D2")
        if "D8" in up.values():
            if "D8" in up["u2"]:
                    solution.append("U2")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D8" in up["u4"]:
                    solution.append("U'")
                    solution.append("F2")
                    uprime(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D8" in up["u6"]:
                    solution.append("U")
                    solution.append("F2")
                    u(up, right, front, left, back)
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
            if "D8" in up["u8"]:
                    solution.append("F2")
                    f(up, right, front, down, left)
                    f(up, right, front, down, left)
        if "D8" in left.values():
            if "D8" in left["l2"]:
                    solution.append("L")
                    solution.append("F'")
                    solution.append("L'")
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    lprime(up, front, down, left, back)
            if "D8" in left["l4"]:
                    solution.append("L2")
                    solution.append("F'")
                    solution.append("L2")
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
                    fprime(up, right, front, down, left)
                    l(up, front, down, left, back)
                    l(up, front, down, left, back)
            if "D8" in left["l6"]:
                    solution.append("F'")
                    fprime(up, right, front, down, left)
            if "D8" in left["l8"]:
                    solution.append("L'")
                    solution.append("F'")
                    lprime(up, front, down, left, back)
                    fprime(up, right, front, down, left)
        if "D8" in right.values():
            if "D8" in right["r2"]:
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D8" in right["r4"]:
                    solution.append("F")
                    f(up, right, front, down, left)
            if "D8" in right["r6"]:
                    solution.append("R2")
                    solution.append("F")
                    solution.append("R2")
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
                    r(up, right, front, down, back)
            if "D8" in right["r8"]:
                    solution.append("R")
                    solution.append("F")
                    r(up, right, front, down, back)
                    f(up, right, front, down, left)
        if "D8" in front.values():
            if "D8" in front["f2"]:
                    solution.append("F")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    f(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D8" in front["f4"]:
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D8" in front["f6"]:
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D8" in front["f8"]:
                    solution.append("F'")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    fprime(up, right, front, down, left)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D8" in back.values():
            if "D8" in back["b2"]:
                    solution.append("U")
                    solution.append("R'")
                    solution.append("F")
                    solution.append("R")
                    u(up, right, front, left, back)
                    rprime(up, right, front, down, back)
                    f(up, right, front, down, left)
                    r(up, right, front, down, back)
            if "D8" in back["b4"]:
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D8" in back["b6"]:
                    solution.append("D'")
                    solution.append("L'")
                    solution.append("D")
                    dprime(right, front, down, left, back)
                    lprime(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D8" in back["b8"]:
                    solution.append("B")
                    solution.append("D")
                    solution.append("R")
                    solution.append("D'")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    r(up, right, front, down, back)
                    dprime(right, front, down, left, back)
        if "D8" in down.values():
            if "D8" in down["d4"]:
                    solution.append("L'")
                    solution.append("D'")
                    solution.append("L")
                    solution.append("D")
                    lprime(up, front, down, left, back)
                    dprime(right, front, down, left, back)
                    l(up, front, down, left, back)
                    d(right, front, down, left, back)
            if "D8" in down["d6"]:
                    solution.append("R")
                    solution.append("D")
                    solution.append("R'")
                    solution.append("D'")
                    r(up, right, front, down, back)
                    d(right, front, down, left, back)
                    rprime(up, right, front, down, back)
                    dprime(right, front, down, left, back)
            if "D8" in down["d8"]:
                    solution.append("B")
                    solution.append("D2")
                    solution.append("B'")
                    solution.append("D2")
                    b(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
                    bprime(up, right, down, left, back)
                    d(right, front, down, left, back)
                    d(right, front, down, left, back)
        d(right, front, down, left, back)
        d(right, front, down, left, back)
        solution.append("D2")
    i = 0
    formatted_cross_list = []

    while i <= (len(solution) - 1):
        if i == len(solution) - 1:
            formatted_cross_list.append(str(solution[i]))
            break
        else:
            if "D" == solution[i]:
                if "D" == solution[i+1]:
                    formatted_cross_list.append("D2")
                    i += 2
                    continue
                if "D'" == solution[i+1]:
                    i += 2
                    continue
                if "D2" == solution[i+1]:
                    formatted_cross_list.append("D'")
                    i += 2
                    continue
                else:
                    formatted_cross_list.append(str(solution[i]))
                    i += 1
                    continue
            if "D'" == solution[i]:
                if "D" == solution[i+1]:
                    i += 2
                    continue
                if "D'" == solution[i+1]:
                    formatted_cross_list.append("D2")
                    i += 2
                    continue
                if "D2" == solution[i+1]:
                    formatted_cross_list.append("D")
                    i += 2
                    continue
                else:
                    formatted_cross_list.append(str(solution[i]))
                    i += 1
                    continue
            if "D2" == solution[i]:
                if "D" == solution[i+1]:
                    formatted_cross_list.append("D'")
                    i += 2
                    continue
                if "D'" == solution[i+1]:
                    formatted_cross_list.append("D")
                    i += 2
                    continue
                if "D2" == solution[i+1]:
                    i += 2
                    continue
                else:
                    formatted_cross_list.append(str(solution[i]))
                    i += 1
                    continue
            else:
                formatted_cross_list.append(str(solution[i]))
                i += 1
                continue
    formatted_cross = ""
    formatted_cross_list2 = []
    i = 0
    while i <= (len(formatted_cross_list)-1):
        if i == len(formatted_cross_list) - 1:
            formatted_cross_list2.append(str(formatted_cross_list[i]))
            break
        else:
            if "D" == formatted_cross_list[i]:
                if "D" == formatted_cross_list[i+1]:
                    formatted_cross_list2.append("D2")
                    i += 2
                    continue
                if "D'" == formatted_cross_list[i+1]:
                    i += 2
                    continue
                if "D2" == formatted_cross_list[i+1]:
                    formatted_cross_list2.append("D'")
                    i += 2
                    continue
                else:
                    formatted_cross_list2.append(str(formatted_cross_list[i]))
                    i += 1
                    continue
            if "D'" == formatted_cross_list[i]:
                if "D" == formatted_cross_list[i+1]:
                    i += 2
                    continue
                if "D'" == formatted_cross_list[i+1]:
                    formatted_cross_list2.append("D2")
                    i += 2
                    continue
                if "D2" == formatted_cross_list[i+1]:
                    formatted_cross_list2.append("D")
                    i += 2
                    continue
                else:
                    formatted_cross_list2.append(str(formatted_cross_list[i]))
                    i += 1
                    continue
            if "D2" == formatted_cross_list[i]:
                if "D" == formatted_cross_list[i+1]:
                    formatted_cross_list2.append("D'")
                    i += 2
                    continue
                if "D'" == formatted_cross_list[i+1]:
                    formatted_cross_list2.append("D")
                    i += 2
                    continue
                if "D2" == formatted_cross_list[i+1]:
                    i += 2
                    continue
                else:
                    formatted_cross_list2.append(str(formatted_cross_list[i]))
                    i += 1
                    continue
            else:
                formatted_cross_list2.append(str(formatted_cross_list[i]))
                i += 1
                continue
    i = 0
    while i <= (len(formatted_cross_list2) - 1):
        if i == len(formatted_cross_list2) - 1:
            formatted_cross += (str(formatted_cross_list2[i]) + " ")
            break
        else:
            if "L" == formatted_cross_list2[i]:
                if "L" == formatted_cross_list2[i + 1]:
                    formatted_cross += "L2 "
                    i += 2
                    continue
                if "L'" == formatted_cross_list2[i + 1]:
                    i += 2
                    continue
                if "L2" == formatted_cross_list2[i + 1]:
                    formatted_cross += "L' "
                    i += 2
                    continue
                else:
                    formatted_cross += (str(formatted_cross_list2[i]) + " ")
                    i += 1
                    continue
            if "L'" == formatted_cross_list2[i]:
                if "L" == formatted_cross_list2[i + 1]:
                    i += 2
                    continue
                if "L'" == formatted_cross_list2[i + 1]:
                    formatted_cross += "L2 "
                    i += 2
                    continue
                if "L2" == formatted_cross_list2[i + 1]:
                    formatted_cross += "L "
                    i += 2
                    continue
                else:
                    formatted_cross += (str(formatted_cross_list2[i]) + " ")
                    i += 1
                    continue
            if "L2" == formatted_cross_list2[i]:
                if "L" == formatted_cross_list2[i + 1]:
                    formatted_cross += "L' "
                    i += 2
                    continue
                if "L'" == formatted_cross_list2[i + 1]:
                    formatted_cross += "L "
                    i += 2
                    continue
                if "L2" == formatted_cross_list2[i + 1]:
                    i += 2
                    continue
                else:
                    formatted_cross += (str(formatted_cross_list2[i]) + " ")
                    i += 1
                    continue
            if "R" == formatted_cross_list2[i]:
                if "R" == formatted_cross_list2[i + 1]:
                    formatted_cross += "R2 "
                    i += 2
                    continue
                if "R'" == formatted_cross_list2[i + 1]:
                    i += 2
                    continue
                if "R2" == formatted_cross_list2[i + 1]:
                    formatted_cross += "R' "
                    i += 2
                    continue
                else:
                    formatted_cross += (str(formatted_cross_list2[i]) + " ")
                    i += 1
                    continue
            if "R'" == formatted_cross_list2[i]:
                if "R" == formatted_cross_list2[i + 1]:
                    i += 2
                    continue
                if "R'" == formatted_cross_list2[i + 1]:
                    formatted_cross += "R2 "
                    i += 2
                    continue
                if "R2" == formatted_cross_list2[i + 1]:
                    formatted_cross += "R "
                    i += 2
                    continue
                else:
                    formatted_cross += (str(formatted_cross_list2[i]) + " ")
                    i += 1
                    continue
            if "R2" == formatted_cross_list2[i]:
                if "R" == formatted_cross_list2[i + 1]:
                    formatted_cross += "R' "
                    i += 2
                    continue
                if "R'" == formatted_cross_list2[i + 1]:
                    formatted_cross += "R "
                    i += 2
                    continue
                if "R2" == formatted_cross_list2[i + 1]:
                    i += 2
                    continue
                else:
                    formatted_cross += (str(formatted_cross_list2[i]) + " ")
                    i += 1
                    continue
            else:
                formatted_cross += (str(formatted_cross_list2[i]) + " ")
                i += 1
                continue
    return formatted_cross
