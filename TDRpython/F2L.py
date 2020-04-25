from Moves import u, uprime, r, rprime, f, fprime, l, lprime, y, yprime, cube_scheme, lowerd, lowerdprime


def f2l(up, right, front, down, left, back):
    """Return the moves to complete the first two layers"""
    corner_slots = ["d3", "f9", "r7", "u9", "f3", "r1"]
    edge_slots = ["f6", "r4", "u2", "u4", "u6", "u8", "r2", "b2", "l2", "f2"]
    upper_corner_slots = ["u1", "l1", "b3", "u3", "r3", "b1", "u7", "l3", "f1"]
    wrong_edge_slots = ["f4", "l6", "l4", "b6", "r6", "b4"]
    wrong_corner_slots = ["f7", "d1", "l9", "l7", "d7", "b9", "r9", "b7", "d9"]
    wrong_greeno = False
    wrong_blueo = False
    wrong_bluer = False
    wrong_greenr = False
    formatted_f2l = ""
    final_f2l = ""

    # GREEN ORANGE
    for face in cube_scheme:
        if "F9" in face.values():
            greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
        else:
            continue
    for face in cube_scheme:
        if "F6" in face.values():
            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
        else:
            continue
    greeno_f2l = [greeno_corner_position, greeno_edge_position]
    # greenorg_f2l = greeno_f2l
    if greeno_corner_position in corner_slots:
        if greeno_edge_position in edge_slots:
            arg = greeno_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        else:
            if greeno_edge_position in wrong_edge_slots[0:2]:
                formatted_f2l += "F U F' "
                f(up, right, front, down, left)
                u(up, right, front, left, back)
                fprime(up, right, front, down, left)
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
            if greeno_edge_position in wrong_edge_slots[2:4]:
                formatted_f2l += "L U' L' U "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
            if greeno_edge_position in wrong_edge_slots[4:6]:
                formatted_f2l += "R' U R "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
            greeno_f2l = [greeno_corner_position, greeno_edge_position]
            arg = greeno_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if greeno_corner_position in upper_corner_slots:
        # U1
        if greeno_corner_position in upper_corner_slots[0:3]:
            formatted_f2l += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            for face in cube_scheme:
                if "F9" in face.values():
                    greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                else:
                    continue
            for face in cube_scheme:
                if "F6" in face.values():
                    greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                else:
                    continue
            greeno_f2l = [greeno_corner_position, greeno_edge_position]
            if greeno_edge_position in edge_slots:
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if greeno_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U3
        if greeno_corner_position in upper_corner_slots[3:6]:
            u(up, right, front, left, back)
            for face in cube_scheme:
                if "F9" in face.values():
                    greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                else:
                    continue
            for face in cube_scheme:
                if "F6" in face.values():
                    greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                else:
                    continue
            greeno_f2l = [greeno_corner_position, greeno_edge_position]
            if greeno_edge_position in edge_slots:
                formatted_f2l += "U "
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                formatted_f2l += "U "
                if greeno_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U7
        if greeno_corner_position in upper_corner_slots[6:9]:
            uprime(up, right, front, left, back)
            for face in cube_scheme:
                if "F9" in face.values():
                    greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                else:
                    continue
            for face in cube_scheme:
                if "F6" in face.values():
                    greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                else:
                    continue
            greeno_f2l = [greeno_corner_position, greeno_edge_position]
            if greeno_edge_position in edge_slots:
                formatted_f2l += "U' "
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                formatted_f2l += "U' "
                if greeno_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    else:
        wrong_greeno = True

    # BLUE ORANGE
    y(up, right, front, down, left, back)
    formatted_f2l += "y "
    for face in cube_scheme:
        if "R9" in face.values():
            blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
        else:
            continue
    for face in cube_scheme:
        if "R6" in face.values():
            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
        else:
            continue
    blueo_f2l = [blueo_corner_position, blueo_edge_position]
    # blueorg_f2l = blueo_f2l
    if blueo_corner_position in corner_slots:

        if blueo_edge_position in edge_slots:
            arg = blueo_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        else:
            if blueo_edge_position in wrong_edge_slots[0:2]:
                formatted_f2l += "F U F' "
                f(up, right, front, down, left)
                u(up, right, front, left, back)
                fprime(up, right, front, down, left)
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
            if blueo_edge_position in wrong_edge_slots[2:4]:
                formatted_f2l += "L U' L' U "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
            if blueo_edge_position in wrong_edge_slots[4:6]:
                formatted_f2l += "R' U R "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
            blueo_f2l = [blueo_corner_position, blueo_edge_position]
            arg = blueo_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if blueo_corner_position in upper_corner_slots:
        # U1
        if blueo_corner_position in upper_corner_slots[0:3]:
            formatted_f2l += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            for face in cube_scheme:
                if "R9" in face.values():
                    blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                else:
                    continue
            for face in cube_scheme:
                if "R6" in face.values():
                    blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                else:
                    continue
            blueo_f2l = [blueo_corner_position, blueo_edge_position]
            if blueo_edge_position in edge_slots:
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if blueo_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U3
        if blueo_corner_position in upper_corner_slots[3:6]:
            u(up, right, front, left, back)
            formatted_f2l += "U "
            for face in cube_scheme:
                if "R9" in face.values():
                    blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                else:
                    continue
            for face in cube_scheme:
                if "R6" in face.values():
                    blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                else:
                    continue
            blueo_f2l = [blueo_corner_position, blueo_edge_position]
            if blueo_edge_position in edge_slots:
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if blueo_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U7
        if blueo_corner_position in upper_corner_slots[6:9]:
            uprime(up, right, front, left, back)
            for face in cube_scheme:
                if "R9" in face.values():
                    blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                else:
                    continue
            for face in cube_scheme:
                if "R6" in face.values():
                    blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                else:
                    continue
            blueo_f2l = [blueo_corner_position, blueo_edge_position]
            if blueo_edge_position in edge_slots:
                formatted_f2l += "U' "
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                formatted_f2l += "U' "
                if blueo_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    else:
        wrong_blueo = True

    # BLUE RED
    y(up, right, front, down, left, back)
    formatted_f2l += "y "
    for face in cube_scheme:
        if "B9" in face.values():
            bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
        else:
            continue
    for face in cube_scheme:
        if "B6" in face.values():
            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
        else:
            continue
    bluer_f2l = [bluer_corner_position, bluer_edge_position]
    # bluerorg_f2l = bluer_f2l
    if bluer_corner_position in corner_slots:
        if bluer_edge_position in edge_slots:
            arg = bluer_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        else:
            if bluer_edge_position in wrong_edge_slots[0:2]:
                formatted_f2l += "F U F' "
                f(up, right, front, down, left)
                u(up, right, front, left, back)
                fprime(up, right, front, down, left)
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
            if bluer_edge_position in wrong_edge_slots[2:4]:
                formatted_f2l += "L U' L' U "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
            if bluer_edge_position in wrong_edge_slots[4:6]:
                formatted_f2l += "R' U R "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
            bluer_f2l = [bluer_corner_position, bluer_edge_position]
            arg = bluer_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if bluer_corner_position in upper_corner_slots:
        # U1
        if bluer_corner_position in upper_corner_slots[0:3]:
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            formatted_f2l += "U2 "
            for face in cube_scheme:
                if "B9" in face.values():
                    bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                else:
                    continue
            for face in cube_scheme:
                if "B6" in face.values():
                    bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                else:
                    continue
            bluer_f2l = [bluer_corner_position, bluer_edge_position]
            if bluer_edge_position in edge_slots:
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if bluer_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U3
        if bluer_corner_position in upper_corner_slots[3:6]:
            u(up, right, front, left, back)
            formatted_f2l += "U "
            for face in cube_scheme:
                if "B9" in face.values():
                    bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                else:
                    continue
            for face in cube_scheme:
                if "B6" in face.values():
                    bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                else:
                    continue
            bluer_f2l = [bluer_corner_position, bluer_edge_position]
            if bluer_edge_position in edge_slots:
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if bluer_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U7
        if bluer_corner_position in upper_corner_slots[6:9]:
            uprime(up, right, front, left, back)
            formatted_f2l += "U' "
            for face in cube_scheme:
                if "B9" in face.values():
                    bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                else:
                    continue
            for face in cube_scheme:
                if "B6" in face.values():
                    bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                else:
                    continue
            bluer_f2l = [bluer_corner_position, bluer_edge_position]
            if bluer_edge_position in edge_slots:
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if bluer_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    else:
        wrong_bluer = True

    # GREEN RED
    y(up, right, front, down, left, back)
    formatted_f2l += "y "
    for face in cube_scheme:
        if "L9" in face.values():
            greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
        else:
            continue
    for face in cube_scheme:
        if "L6" in face.values():
            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
        else:
            continue
    greenr_f2l = [greenr_corner_position, greenr_edge_position]
    # greenrorg_f2l = greenr_f2l
    if greenr_corner_position in corner_slots:
        if greenr_edge_position in edge_slots:
            arg = greenr_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        else:
            if greenr_edge_position in wrong_edge_slots[0:2]:
                formatted_f2l += "F U F' "
                f(up, right, front, down, left)
                u(up, right, front, left, back)
                fprime(up, right, front, down, left)
                for face in cube_scheme:
                    if "L6" in face.values():
                        greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                    else:
                        continue
            if greenr_edge_position in wrong_edge_slots[2:4]:
                formatted_f2l += "L U' L' U "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "L6" in face.values():
                        greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                    else:
                        continue
            if greenr_edge_position in wrong_edge_slots[4:6]:
                formatted_f2l += "R' U R "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                for face in cube_scheme:
                    if "L6" in face.values():
                        greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                    else:
                        continue
            greenr_f2l = [greenr_corner_position, greenr_edge_position]
            arg = greenr_f2l
            formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if greenr_corner_position in upper_corner_slots:
        # U1
        if greenr_corner_position in upper_corner_slots[0:3]:
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            formatted_f2l += "U2 "
            for face in cube_scheme:
                if "L9" in face.values():
                    greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
                else:
                    continue
            for face in cube_scheme:
                if "L6" in face.values():
                    greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                else:
                    continue
            greenr_f2l = [greenr_corner_position, greenr_edge_position]
            if greenr_edge_position in edge_slots:
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if greenr_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                greenr_f2l = [greenr_corner_position, greenr_edge_position]
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U3
        if greenr_corner_position in upper_corner_slots[3:6]:
            u(up, right, front, left, back)
            formatted_f2l += "U "
            for face in cube_scheme:
                if "L9" in face.values():
                    greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
                else:
                    continue
            for face in cube_scheme:
                if "L6" in face.values():
                    greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                else:
                    continue
            greenr_f2l = [greenr_corner_position, greenr_edge_position]
            if greenr_edge_position in edge_slots:
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if greenr_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                greenr_f2l = [greenr_corner_position, greenr_edge_position]
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        # U7
        if greenr_corner_position in upper_corner_slots[6:9]:
            uprime(up, right, front, left, back)
            formatted_f2l += "U' "
            for face in cube_scheme:
                if "L9" in face.values():
                    greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
                else:
                    continue
            for face in cube_scheme:
                if "L6" in face.values():
                    greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                else:
                    continue
            greenr_f2l = [greenr_corner_position, greenr_edge_position]
            if greenr_edge_position in edge_slots:
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if greenr_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                greenr_f2l = [greenr_corner_position, greenr_edge_position]
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    else:
        wrong_greenr = True

    if wrong_greeno:
        if "F5" in right["r5"]:
            y(up, right, front, down, left, back)
            formatted_f2l += "y "
        if "F5" in left["l5"]:
            yprime(up, right, front, down, left, back)
            formatted_f2l += "y' "
        if "F5" in back["b5"]:
            y(up, right, front, down, left, back)
            y(up, right, front, down, left, back)
            formatted_f2l += "y2 "
        for face in cube_scheme:
            if "F9" in face.values():
                greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
            else:
                continue
        for face in cube_scheme:
            if "F6" in face.values():
                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
            else:
                continue
        greeno_f2l = [greeno_corner_position, greeno_edge_position]
        # greenorg_f2l = greeno_f2l
        if greeno_corner_position in corner_slots:
            if greeno_edge_position in edge_slots:
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if greeno_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                if greeno_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "F6" in face.values():
                            greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                        else:
                            continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                arg = greeno_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if greeno_corner_position in upper_corner_slots:
            # U1
            if greeno_corner_position in upper_corner_slots[0:3]:
                formatted_f2l += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "F9" in face.values():
                        greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                if greeno_edge_position in edge_slots:
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if greeno_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    greeno_f2l = [greeno_corner_position, greeno_edge_position]
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U3
            if greeno_corner_position in upper_corner_slots[3:6]:
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "F9" in face.values():
                        greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                if greeno_edge_position in edge_slots:
                    formatted_f2l += "U "
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U "
                    if greeno_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    greeno_f2l = [greeno_corner_position, greeno_edge_position]
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U7
            if greeno_corner_position in upper_corner_slots[6:9]:
                uprime(up, right, front, left, back)
                for face in cube_scheme:
                    if "F9" in face.values():
                        greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                if greeno_edge_position in edge_slots:
                    formatted_f2l += "U' "
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U' "
                    if greeno_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    greeno_f2l = [greeno_corner_position, greeno_edge_position]
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if greeno_corner_position in wrong_corner_slots:
            # D1
            if greeno_corner_position in wrong_corner_slots[0:3]:
                if greeno_edge_position == "u2" or "b2":
                    formatted_f2l += "U' "
                    uprime(up, right, front, left, back)
                formatted_f2l += "L' U' L "
                lprime(up, front, down, left, back)
                uprime(up, right, front, left, back)
                l(up, front, down, left, back)
                for face in cube_scheme:
                    if "F9" in face.values():
                        greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                if greeno_edge_position in edge_slots:
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if greeno_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    greeno_f2l = [greeno_corner_position, greeno_edge_position]
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # D7
            if greeno_corner_position in wrong_corner_slots[3:6]:
                if greeno_edge_position == "u2" or "b2":
                    formatted_f2l += "U "
                    u(up, right, front, left, back)
                formatted_f2l += "L U' L' U2 "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                uprime(up, right, front, left, back)
                uprime(up, right, front, left, back)
                for face in cube_scheme:
                    if "F9" in face.values():
                        greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                if greeno_edge_position in edge_slots:
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if greeno_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    greeno_f2l = [greeno_corner_position, greeno_edge_position]
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # D9
            if greeno_corner_position in wrong_corner_slots[6:9]:
                if greeno_edge_position == "u2" or "b2":
                    formatted_f2l += "U' "
                    uprime(up, right, front, left, back)
                formatted_f2l += "R' U R U "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "F9" in face.values():
                        greeno_corner_position = list(face.keys())[list(face.values()).index("F9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "F6" in face.values():
                        greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                    else:
                        continue
                greeno_f2l = [greeno_corner_position, greeno_edge_position]
                if greeno_edge_position in edge_slots:
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if greeno_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    if greeno_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "F6" in face.values():
                                greeno_edge_position = list(face.keys())[list(face.values()).index("F6")]
                            else:
                                continue
                    greeno_f2l = [greeno_corner_position, greeno_edge_position]
                    arg = greeno_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if wrong_blueo:
        if "R5" in right["r5"]:
            y(up, right, front, down, left, back)
            formatted_f2l += "y "
        if "R5" in left["l5"]:
            yprime(up, right, front, down, left, back)
            formatted_f2l += "y' "
        if "R5" in back["b5"]:
            y(up, right, front, down, left, back)
            y(up, right, front, down, left, back)
            formatted_f2l += "y2 "
        for face in cube_scheme:
            if "R9" in face.values():
                blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
            else:
                continue
        for face in cube_scheme:
            if "R6" in face.values():
                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
            else:
                continue
        blueo_f2l = [blueo_corner_position, blueo_edge_position]
        # blueorg_f2l = blueo_f2l
        if blueo_corner_position in corner_slots:
            if blueo_edge_position in edge_slots:
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if blueo_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                if blueo_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "R6" in face.values():
                            blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                        else:
                            continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                arg = blueo_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if blueo_corner_position in upper_corner_slots:
            # U1
            if blueo_corner_position in upper_corner_slots[0:3]:
                formatted_f2l += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "R9" in face.values():
                        blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                if blueo_edge_position in edge_slots:
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if blueo_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    blueo_f2l = [blueo_corner_position, blueo_edge_position]
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U3
            if blueo_corner_position in upper_corner_slots[3:6]:
                u(up, right, front, left, back)
                formatted_f2l += "U "
                for face in cube_scheme:
                    if "R9" in face.values():
                        blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                if blueo_edge_position in edge_slots:
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if blueo_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    blueo_f2l = [blueo_corner_position, blueo_edge_position]
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U7
            if blueo_corner_position in upper_corner_slots[6:9]:
                uprime(up, right, front, left, back)
                for face in cube_scheme:
                    if "R9" in face.values():
                        blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                if blueo_edge_position in edge_slots:
                    formatted_f2l += "U' "
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U' "
                    if blueo_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    blueo_f2l = [blueo_corner_position, blueo_edge_position]
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if blueo_corner_position in wrong_corner_slots:
            # D1
            if blueo_corner_position in wrong_corner_slots[0:3]:
                if blueo_edge_position == "u2" or "b2":
                    formatted_f2l += "U' "
                    uprime(up, right, front, left, back)
                formatted_f2l += "L' U' L "
                lprime(up, front, down, left, back)
                uprime(up, right, front, left, back)
                l(up, front, down, left, back)
                for face in cube_scheme:
                    if "R9" in face.values():
                        blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                if blueo_edge_position in edge_slots:
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if blueo_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    blueo_f2l = [blueo_corner_position, blueo_edge_position]
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # D7
            if blueo_corner_position in wrong_corner_slots[3:6]:
                if blueo_edge_position == "u2" or "b2":
                    formatted_f2l += "U "
                    u(up, right, front, left, back)
                formatted_f2l += "L U' L' U2 "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                uprime(up, right, front, left, back)
                uprime(up, right, front, left, back)
                for face in cube_scheme:
                    if "R9" in face.values():
                        blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                if blueo_edge_position in edge_slots:
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if blueo_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    blueo_f2l = [blueo_corner_position, blueo_edge_position]
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # D9
            if blueo_corner_position in wrong_corner_slots[6:9]:
                if blueo_edge_position == "u2" or "b2":
                    formatted_f2l += "U' "
                    uprime(up, right, front, left, back)
                formatted_f2l += "R' U R U "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "R9" in face.values():
                        blueo_corner_position = list(face.keys())[list(face.values()).index("R9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "R6" in face.values():
                        blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                    else:
                        continue
                blueo_f2l = [blueo_corner_position, blueo_edge_position]
                if blueo_edge_position in edge_slots:
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if blueo_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    if blueo_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "R6" in face.values():
                                blueo_edge_position = list(face.keys())[list(face.values()).index("R6")]
                            else:
                                continue
                    blueo_f2l = [blueo_corner_position, blueo_edge_position]
                    arg = blueo_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if wrong_bluer:
        if "B5" in right["r5"]:
            y(up, right, front, down, left, back)
            formatted_f2l += "y "
        if "B5" in left["l5"]:
            yprime(up, right, front, down, left, back)
            formatted_f2l += "y' "
        if "B5" in back["b5"]:
            y(up, right, front, down, left, back)
            y(up, right, front, down, left, back)
            formatted_f2l += "y2 "
        for face in cube_scheme:
            if "B9" in face.values():
                bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
            else:
                continue
        for face in cube_scheme:
            if "B6" in face.values():
                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
            else:
                continue
        bluer_f2l = [bluer_corner_position, bluer_edge_position]
        # bluerorg_f2l = bluer_f2l
        if bluer_corner_position in corner_slots:
            if bluer_edge_position in edge_slots:
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if bluer_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                if bluer_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "B6" in face.values():
                            bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                        else:
                            continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                arg = bluer_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if bluer_corner_position in upper_corner_slots:
            # U1
            if bluer_corner_position in upper_corner_slots[0:3]:
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                formatted_f2l += "U2 "
                for face in cube_scheme:
                    if "B9" in face.values():
                        bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                if bluer_edge_position in edge_slots:
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if bluer_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    bluer_f2l = [bluer_corner_position, bluer_edge_position]
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U3
            if bluer_corner_position in upper_corner_slots[3:6]:
                u(up, right, front, left, back)
                formatted_f2l += "U "
                for face in cube_scheme:
                    if "B9" in face.values():
                        bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                if bluer_edge_position in edge_slots:
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if bluer_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    bluer_f2l = [bluer_corner_position, bluer_edge_position]
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U7
            if bluer_corner_position in upper_corner_slots[6:9]:
                uprime(up, right, front, left, back)
                formatted_f2l += "U' "
                for face in cube_scheme:
                    if "B9" in face.values():
                        bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                if bluer_edge_position in edge_slots:
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if bluer_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    bluer_f2l = [bluer_corner_position, bluer_edge_position]
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if bluer_corner_position in wrong_corner_slots:
            # D1
            if bluer_corner_position in wrong_corner_slots[0:3]:
                if bluer_edge_position == "u2" or "b2":
                    formatted_f2l += "U' "
                    uprime(up, right, front, left, back)
                formatted_f2l += "L' U' L "
                lprime(up, front, down, left, back)
                uprime(up, right, front, left, back)
                l(up, front, down, left, back)
                for face in cube_scheme:
                    if "B9" in face.values():
                        bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                if bluer_edge_position in edge_slots:
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if bluer_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    bluer_f2l = [bluer_corner_position, bluer_edge_position]
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # D7
            if bluer_corner_position in wrong_corner_slots[3:6]:
                if bluer_edge_position == "u2" or "b2":
                    formatted_f2l += "U "
                    u(up, right, front, left, back)
                formatted_f2l += "L U' L' U2 "
                l(up, front, down, left, back)
                uprime(up, right, front, left, back)
                lprime(up, front, down, left, back)
                uprime(up, right, front, left, back)
                uprime(up, right, front, left, back)
                for face in cube_scheme:
                    if "B9" in face.values():
                        bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                if bluer_edge_position in edge_slots:
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if bluer_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    bluer_f2l = [bluer_corner_position, bluer_edge_position]
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # D9
            if bluer_corner_position in wrong_corner_slots[6:9]:
                if bluer_edge_position == "u2" or "b2":
                    formatted_f2l += "U' "
                    uprime(up, right, front, left, back)
                formatted_f2l += "R' U R U "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                for face in cube_scheme:
                    if "B9" in face.values():
                        bluer_corner_position = list(face.keys())[list(face.values()).index("B9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "B6" in face.values():
                        bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                    else:
                        continue
                bluer_f2l = [bluer_corner_position, bluer_edge_position]
                if bluer_edge_position in edge_slots:
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    formatted_f2l += "U2 "
                    if bluer_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    if bluer_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "B6" in face.values():
                                bluer_edge_position = list(face.keys())[list(face.values()).index("B6")]
                            else:
                                continue
                    bluer_f2l = [bluer_corner_position, bluer_edge_position]
                    arg = bluer_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    if wrong_greenr:

        if "L5" in right["r5"]:
            y(up, right, front, down, left, back)
            formatted_f2l += "y "
        if "L5" in left["l5"]:
            yprime(up, right, front, down, left, back)
            formatted_f2l += "y' "
        if "L5" in back["b5"]:
            y(up, right, front, down, left, back)
            y(up, right, front, down, left, back)
            formatted_f2l += "y2 "
        for face in cube_scheme:
            if "L9" in face.values():
                greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
            else:
                continue
        for face in cube_scheme:
            if "L6" in face.values():
                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
            else:
                continue
        greenr_f2l = [greenr_corner_position, greenr_edge_position]
        greenrorg_f2l = greenr_f2l
        if greenr_corner_position in corner_slots:
            if greenr_edge_position in edge_slots:
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            else:
                if greenr_edge_position in wrong_edge_slots[0:2]:
                    formatted_f2l += "F U F' "
                    f(up, right, front, down, left)
                    u(up, right, front, left, back)
                    fprime(up, right, front, down, left)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[2:4]:
                    formatted_f2l += "L U' L' U "
                    l(up, front, down, left, back)
                    uprime(up, right, front, left, back)
                    lprime(up, front, down, left, back)
                    u(up, right, front, left, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                if greenr_edge_position in wrong_edge_slots[4:6]:
                    formatted_f2l += "R' U R "
                    rprime(up, right, front, down, back)
                    u(up, right, front, left, back)
                    r(up, right, front, down, back)
                    for face in cube_scheme:
                        if "L6" in face.values():
                            greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                        else:
                            continue
                greenr_f2l = [greenr_corner_position, greenr_corner_position]
                arg = greenr_f2l
                formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
        if greenr_corner_position in upper_corner_slots:
            # U1
            if greenr_corner_position in upper_corner_slots[0:3]:
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                formatted_f2l += "U2 "
                for face in cube_scheme:
                    if "L9" in face.values():
                        greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "L6" in face.values():
                        greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                    else:
                        continue
                greenr_f2l = [greenr_corner_position, greenr_edge_position]
                if greenr_edge_position in edge_slots:
                    arg = greenr_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if greenr_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    if greenr_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    if greenr_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    greenr_f2l = [greenr_corner_position, greenr_edge_position]
                    arg = greenr_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U3
            if greenr_corner_position in upper_corner_slots[3:6]:
                u(up, right, front, left, back)
                formatted_f2l += "U "
                for face in cube_scheme:
                    if "L9" in face.values():
                        greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "L6" in face.values():
                        greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                    else:
                        continue
                greenr_f2l = [greenr_corner_position, greenr_edge_position]
                if greenr_edge_position in edge_slots:
                    arg = greenr_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if greenr_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    if greenr_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    if greenr_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    greenr_f2l = [greenr_corner_position, greenr_edge_position]
                    arg = greenr_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
            # U7
            if greenr_corner_position in upper_corner_slots[6:9]:
                uprime(up, right, front, left, back)
                formatted_f2l += "U' "
                for face in cube_scheme:
                    if "L9" in face.values():
                        greenr_corner_position = list(face.keys())[list(face.values()).index("L9")]
                    else:
                        continue
                for face in cube_scheme:
                    if "L6" in face.values():
                        greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                    else:
                        continue
                greenr_f2l = [greenr_corner_position, greenr_edge_position]
                if greenr_edge_position in edge_slots:
                    arg = greenr_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
                else:
                    if greenr_edge_position in wrong_edge_slots[0:2]:
                        formatted_f2l += "F U F' "
                        f(up, right, front, down, left)
                        u(up, right, front, left, back)
                        fprime(up, right, front, down, left)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    if greenr_edge_position in wrong_edge_slots[2:4]:
                        formatted_f2l += "L U' L' U "
                        l(up, front, down, left, back)
                        uprime(up, right, front, left, back)
                        lprime(up, front, down, left, back)
                        u(up, right, front, left, back)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    if greenr_edge_position in wrong_edge_slots[4:6]:
                        formatted_f2l += "R' U R "
                        rprime(up, right, front, down, back)
                        u(up, right, front, left, back)
                        r(up, right, front, down, back)
                        for face in cube_scheme:
                            if "L6" in face.values():
                                greenr_edge_position = list(face.keys())[list(face.values()).index("L6")]
                            else:
                                continue
                    greenr_f2l = [greenr_corner_position, greenr_edge_position]
                    arg = greenr_f2l
                    formatted_f2l += str(solvepair(up, right, front, down, left, back, arg))
    i = 0
    # f2l_pairs = [greenorg_f2l, blueorg_f2l, bluerorg_f2l, greenrorg_f2l]
    formatted_f2l_list = formatted_f2l.split()
    while i < len(formatted_f2l_list) - 1:
        item = formatted_f2l_list[i]
        next_item = formatted_f2l_list[i + 1]
        if item[:1] == next_item[:1]:
            if len(item) == 1:
                if len(next_item) == 1:
                    final_f2l += item + "2 "
                if next_item[-1:] == "2":
                    final_f2l += item + "' "
            if item[-1:] == "'":
                if next_item[-1:] == "2":
                    final_f2l += item[:1] + " "
                if next_item[-1:] == "'":
                    final_f2l += item[:1] + "2 "
            if item[-1:] == "2":
                if len(next_item) == 1:
                    final_f2l += item[:1] + "' "
                if next_item[-1:] == "'":
                    final_f2l += item[:1] + " "
            i += 2
        else:
            final_f2l += item + " "
            i += 1
    final_f2l += formatted_f2l_list[-1] + " "
    formatted_f2l_list = final_f2l.split()
    formatted_f2l = ""
    i = 0
    while i < len(formatted_f2l_list) - 1:
        item = formatted_f2l_list[i]
        next_item = formatted_f2l_list[i + 1]
        if item[:1] == next_item[:1]:
            if len(item) == 1:
                if len(next_item) == 1:
                    formatted_f2l += item + "2 "
                if next_item[-1:] == "2":
                    formatted_f2l += item + "' "
            if item[-1:] == "'":
                if next_item[-1:] == "2":
                    formatted_f2l += item[:1] + " "
                if next_item[-1:] == "'":
                    formatted_f2l += item[:1] + "2 "
            if item[-1:] == "2":
                if len(next_item) == 1:
                    formatted_f2l += item[:1] + "' "
                if next_item[-1:] == "'":
                    formatted_f2l += item[:1] + " "
            i += 2
        else:
            formatted_f2l += str(item) + " "
            i += 1
    formatted_f2l += formatted_f2l_list[-1] + " "
    return formatted_f2l


def solvepair(up, right, front, down, left, back, arg):
    """Executes the algorithm to make the F2L pair and insert it."""
    if arg[0] == "d3":
        if arg[1] == "u2":
            formatted_f2l = "U R U R' U' R U R' "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u4":
            formatted_f2l = "U2 R U R' U' R U R' "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u6":
            formatted_f2l = "R U R' U' R U R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u8":
            formatted_f2l = "U' R U R' U' R U R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f2":
            formatted_f2l = "R U R' U' F R' F' R "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "b2":
            formatted_f2l = "U2 R U R' U' F R' F' R "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "r2":
            formatted_f2l = "U R U R' U' F R' F' R "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "l2":
            formatted_f2l = "U' R U R' U' F R' F' R "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f6":
            formatted_f2l = "R U R' U2 R U' R' U R U R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "r4":
            formatted_f2l = "R U F R U R' U' F' R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            rprime(up, right, front, down, back)
            return formatted_f2l
    if arg[0] == "r7":
        if arg[1] == "u2":
            formatted_f2l = "U R U' R' U R U' R' "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u4":
            formatted_f2l = "U2 R U' R' U R U' R' "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u6":
            formatted_f2l = "R U' R' U R U' R' "
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u8":
            formatted_f2l = "U' R U' R' U R U' R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f2":
            formatted_f2l = "R' F R F' R' F R F' "
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "r2":
            formatted_f2l = "U R' F R F' R' F R F' "
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "l2":
            formatted_f2l = "U' R' F R F' R' F R F' "
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "b2":
            formatted_f2l = "U2 R' F R F' R' F R F' "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "f6":
            formatted_f2l = "R U R' U' R U2 R' U' R U R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "r4":
            formatted_f2l = "R U' R' F R U R' U' F' R U' R' "
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
    if arg[0] == "f9":
        if arg[1] == "u2":
            formatted_f2l = "U R' F' R U R U' R' F "
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "u4":
            formatted_f2l = "U2 R' F' R U R U' R' F "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "u6":
            formatted_f2l = "R' F' R U R U' R' F "
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "u8":
            formatted_f2l = "U' R' F' R U R U' R' F "
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "f2":
            formatted_f2l = "U R U' R' U' F' U F "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "r2":
            formatted_f2l = "U2 R U' R' U' F' U F "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "l2":
            formatted_f2l = "R U' R' U' F' U F "
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "b2":
            formatted_f2l = "U' R U' R' U' F' U F "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "f6":
            formatted_f2l = ""
            return formatted_f2l
        if arg[1] == "r4":
            formatted_f2l = "R2 U2 F R2 F' U2 R' U R' "
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
    if arg[0] == "u9":
        if arg[1] == "u2":
            formatted_f2l = "U' R U R' U2 R U' R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u4":
            formatted_f2l = "U' R U2 R' U2 R U' R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u6":
            formatted_f2l = "U R U' R' "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u8":
            formatted_f2l = "R U R' U2 R U' R' U R U' R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f6":
            formatted_f2l = "U' R U' R' U2 R U' R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "r4":
            formatted_f2l = "U' R U R' U F' U' F "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            fprime(up, right, front, down, left)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "f2":
            formatted_f2l = "y' U R' U R U' R' U' R y "
            yprime(up, right, front, down, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            y(up, right, front, down, left, back)
            return formatted_f2l
        if arg[1] == "r2":
            formatted_f2l = "U' R U2 R' U F' U' F "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            fprime(up, right, front, down, left)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "l2":
            formatted_f2l = "F' U' F "
            fprime(up, right, front, down, left)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "b2":
            formatted_f2l = "U' R U' R' U F' U' F "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            fprime(up, right, front, down, left)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
    if arg[0] == "r1":
        if arg[1] == "u2":
            formatted_f2l = "U R U2 R' U R U' R' "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u4":
            formatted_f2l = "R U' R' U2 R U R' "
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u6":
            formatted_f2l = "R U2 R' U' R U R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u8":
            formatted_f2l = "U2 R2 U2 R' U' R U' R2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f2":
            formatted_f2l = "y' R' U2 R U R' U' R y "
            yprime(up, right, front, down, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            y(up, right, front, down, left, back)
            return formatted_f2l
        if arg[1] == "l2":
            formatted_f2l = "y' U' R' U2 R U' R' U R y "
            yprime(up, right, front, down, left, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            y(up, right, front, down, left, back)
            return formatted_f2l
        if arg[1] == "r2":
            formatted_f2l = "F U R U' R' F' R U' R' "
            f(up, right, front, down, left)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "b2":
            formatted_f2l = "F' L' U2 L F "
            fprime(up, right, front, down, left)
            lprime(up, front, down, left, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            l(up, front, down, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "r4":
            formatted_f2l = "U' R' F R F' R U' R' "
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f6":
            formatted_f2l = "R U R' U' R U R' U' R U R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
    if arg[0] == "f3":
        if arg[1] == "u2":
            formatted_f2l = "R U R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u4":
            formatted_f2l = "U' R U R' U R U R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u6":
            formatted_f2l = "U' R U' R' U R U R' "
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "u8":
            formatted_f2l = "R' U2 R2 U R2 U R "
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "f2":
            formatted_f2l = "F R' F' R "
            f(up, right, front, down, left)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "r2":
            formatted_f2l = "R U' R' U2 F' U' F "
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            fprime(up, right, front, down, left)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            return formatted_f2l
        if arg[1] == "l2":
            formatted_f2l = "d R' U' R U2 R' U R d' "
            lowerd(right, front, down, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            lowerdprime(right, front, down, left, back)
            return formatted_f2l
        if arg[1] == "b2":
            formatted_f2l = "d R' U2 R U2 R' U R d' "
            lowerd(right, front, down, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            lowerdprime(right, front, down, left, back)
            return formatted_f2l
        if arg[1] == "f6":
            formatted_f2l = "U R U R' U2 R U R' "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
        if arg[1] == "r4":
            formatted_f2l = "U F' U' F U' R U R' "
            u(up, right, front, left, back)
            fprime(up, right, front, down, left)
            uprime(up, right, front, left, back)
            f(up, right, front, down, left)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            return formatted_f2l
