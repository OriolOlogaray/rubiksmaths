from Moves import u, uprime, r, rprime, f, fprime, l, lprime, lowerd, lowerdprime, lowerr, lowerrprime, m, mprime, d
from Moves import dprime, b, bprime, x, xprime, loweru, loweruprime, y, yprime


def pll(up, right, front, down, left, back):
    """Return the moves to complete the upper layer"""
    formatted_pll = ""
    edges = []
    case = pll_cases(right, front, left, back)
    pll_case = []
    i = 0
    for face in case:
        stickers = face.strip()
        edges.append(stickers[1])
        if stickers[0] == stickers[1] and stickers[1] == stickers[2]:
            pll_case.append("Stripe")
        elif stickers[0] == stickers[2]:
            pll_case.append("Headlights")
        elif stickers[0] == stickers[1]:
            pll_case.append("ShortStripe0")
        elif stickers[2] == stickers[1]:
            pll_case.append("ShortStripe2")
        else:
            pll_case.append("Nothing")
    pll_case2 = 2 * pll_case
    edges *= 2
    if "Stripe" in pll_case:
        if "Headlights" in pll_case:
            if pll_case.index("Stripe") == 1:
                formatted_pll += "U' "
                uprime(up, right, front, left, back)
            if pll_case.index("Stripe") == 2:
                formatted_pll += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
            if pll_case.index("Stripe") == 3:
                formatted_pll += "U "
                u(up, right, front, left, back)
            if right["r2"][:1] == front["f3"][:1]:
                formatted_pll += "R2 U R U R' U' R' U' R' U R' "
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
            else:
                formatted_pll += "R U' R U R U R U' R' U' R2 "
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
        elif "ShortStripe0" in pll_case:
            if pll_case.index("Stripe") == 0:
                formatted_pll += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
            if pll_case.index("Stripe") == 1:
                formatted_pll += "U "
                u(up, right, front, left, back)
            if pll_case.index("Stripe") == 3:
                formatted_pll += "U' "
                uprime(up, right, front, left, back)
            formatted_pll += "R' U L' U2 R U' R' U2 R L "
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            lprime(up, front, down, left, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            l(up, front, down, left, back)
        elif "ShortStripe2" in pll_case:
            if pll_case.index("Stripe") == 0:
                formatted_pll += "U' "
                uprime(up, right, front, left, back)
            if pll_case.index("Stripe") == 1:
                formatted_pll += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
            if pll_case.index("Stripe") == 2:
                formatted_pll += "U "
                u(up, right, front, left, back)
            formatted_pll += "R U R' F' R U R' U' R' F R2 U' R' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
        else:
            if pll_case.index("Stripe") == 0:
                formatted_pll += "U' "
                uprime(up, right, front, left, back)
            if pll_case.index("Stripe") == 1:
                formatted_pll += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
            if pll_case.index("Stripe") == 2:
                formatted_pll += "U "
                u(up, right, front, left, back)
            formatted_pll += "R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R "
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
    elif "Headlights" in pll_case:
        if pll_case.count("Headlights") > 2:
            if back["b2"][:1] == front["f3"][:1]:
                print(back["b2"])
                print(front["f3"])
                formatted_pll += "M2 U M2 U2 M2 U M2 "
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
            elif back["b1"][:1] == left["l2"][:1]:
                formatted_pll += "U M' U M2 U M2 U M' U2 M2 "
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
            else:
                formatted_pll += "M' U M2 U M2 U M' U2 M2 "
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                mprime(up, front, down, back)
                mprime(up, front, down, back)
        if "ShortStripe0" in pll_case and "ShortStripe2" in pll_case:
            if pll_case2[pll_case2.index("Headlights") + 1] == "ShortStripe0":
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 3:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                formatted_pll += "x R2 D2 R U R' D2 R U' R x' "
                x(up, front, right, down, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                d(right, front, down, left, back)
                d(right, front, down, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                d(right, front, down, left, back)
                d(right, front, down, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                xprime(up, right, front, down, left, back)
            elif pll_case2[pll_case2.index("Headlights") + 1] == "ShortStripe2":
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)

                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "R U R' U' R' F R2 U' R' U' R U R' F' "
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                f(up, right, front, down, left)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                fprime(up, right, front, down, left)
            else:
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 3:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "x R' U R' D2 R U' R' D2 R2 x' "
                x(up, right, front, down, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                d(right, front, down, left, back)
                d(right, front, down, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                d(right, front, down, left, back)
                d(right, front, down, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                xprime(up, right, front, down, left, back)
        elif "ShortStripe0" in pll_case:
            if pll_case2[pll_case2.index("Headlights") + 1] == "ShortStripe0":
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "R2 u' R U' R U R' u R2 y R U' R' "
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                loweruprime(up, right, front, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                loweru(up, right, front, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                y(up, right, front, down, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
            elif pll_case2[pll_case2.index("Headlights") + 2] == "ShortStripe0":
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "R U R' y' R2 u' R U' R' U R' u R2 "
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                yprime(up, right, front, down, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                loweruprime(up, right, front, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                loweru(up, right, front, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
            else:
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "R U' R' U' R U R D R' U' R D' R' U2 R' "
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                d(right, front, down, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                dprime(right, front, down, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
        elif "ShortStripe2" in pll_case:
            if pll_case2[pll_case2.index("Headlights") + 1] == "ShortStripe2":
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 3:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                formatted_pll += "R' U2 R U2 R' F R U R' U' R' F' R2 "
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                f(up, right, front, down, left)
                r(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                fprime(up, right, front, down, left)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
            elif pll_case2[pll_case2.index("Headlights") + 2] == "ShortStripe2":
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "R' U' R y R2 u R' U R U' R u' R2 "
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                y(up, right, front, down, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                loweru(up, right, front, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                loweruprime(up, right, front, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
            else:
                if pll_case.index("Headlights") == 0:
                    formatted_pll += "U' "
                    uprime(up, right, front, left, back)
                if pll_case.index("Headlights") == 1:
                    formatted_pll += "U2 "
                    u(up, right, front, left, back)
                    u(up, right, front, left, back)
                if pll_case.index("Headlights") == 2:
                    formatted_pll += "U "
                    u(up, right, front, left, back)
                formatted_pll += "R2 u R' U R' U' R u' R2 y' R' U R "
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                loweru(up, right, front, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                rprime(up, right, front, down, back)
                uprime(up, right, front, left, back)
                r(up, right, front, down, back)
                loweruprime(up, right, front, left, back)
                r(up, right, front, down, back)
                r(up, right, front, down, back)
                yprime(up, right, front, down, left, back)
                rprime(up, right, front, down, back)
                u(up, right, front, left, back)
                r(up, right, front, down, back)
    elif "ShortStripe0" and "ShortStripe2" in pll_case:
        if pll_case2[pll_case2.index("ShortStripe0") + 1] == "ShortStripe2":
            if pll_case.index("ShortStripe0") == 0:
                formatted_pll += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
            if pll_case.index("ShortStripe0") == 1:
                formatted_pll += "U "
                u(up, right, front, left, back)
            if pll_case.index("ShortStripe0") == 3:
                formatted_pll += "U' "
                uprime(up, right, front, left, back)
            formatted_pll += "R' U R' d' R' F' R2 U' R' U R' F R F "
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            lowerdprime(right, front, down, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            f(up, right, front, down, left)
        else:
            if pll_case.index("ShortStripe0") == 0:
                formatted_pll += "U2 "
                u(up, right, front, left, back)
                u(up, right, front, left, back)
            if pll_case.index("ShortStripe0") == 1:
                formatted_pll += "U "
                u(up, right, front, left, back)
            if pll_case.index("ShortStripe0") == 3:
                formatted_pll += "U' "
                uprime(up, right, front, left, back)
            formatted_pll += "F R U' R' U' R U R' F' R U R' U' R' F R F' "
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            fprime(up, right, front, down, left)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            uprime(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
    elif "ShortStripe0" in pll_case:
        formatted_pll += "R' U L' U2 R U' L R' U L' U2 R U' L "
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        lprime(up, front, down, left, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        lprime(up, front, down, left, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
    elif "ShortStripe2" in pll_case:
        formatted_pll += "R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        fprime(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
    else:
        if "F" or "R" or "B" or "L" not in right["r1"] and back["b2"]:
            formatted_pll += "U "
            u(up, right, front, left, back)
        formatted_pll += "x' R U' R' D R U R' D' R U R' D R U' R' D' x "
        xprime(up, front, right, down, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        d(right, front, down, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        dprime(right, front, down, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        d(right, front, down, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        dprime(right, front, down, left, back)
        x(up, front, right, down, left, back)
    return formatted_pll


def pll_cases(right, front, left, back):
    """Determine the PLL case from the stickers in the last layer"""
    pll = []
    backs = ""
    rights = ""
    fronts = ""
    lefts = ""
    for i in range(0, 3):
        if "F" in list(back.values())[i]:
            backs += "F"
        if "R" in list(back.values())[i]:
            backs += "R"
        if "B" in list(back.values())[i]:
            backs += "B"
        if "L" in list(back.values())[i]:
            backs += "L"
    for i in range(0, 3):
        if "F" in list(right.values())[i]:
            rights += "F"
        if "R" in list(right.values())[i]:
            rights += "R"
        if "B" in list(right.values())[i]:
            rights += "B"
        if "L" in list(right.values())[i]:
            rights += "L"
    for i in range(0, 3):
        if "F" in list(front.values())[i]:
            fronts += "F"
        if "R" in list(front.values())[i]:
            fronts += "R"
        if "B" in list(front.values())[i]:
            fronts += "B"
        if "L" in list(front.values())[i]:
            fronts += "L"
    for i in range(0, 3):
        if "F" in list(left.values())[i]:
            lefts += "F"
        if "R" in list(left.values())[i]:
            lefts += "R"
        if "B" in list(left.values())[i]:
            lefts += "B"
        if "L" in list(left.values())[i]:
            lefts += "L"
    pll.append(backs)
    pll.append(rights)
    pll.append(fronts)
    pll.append(lefts)
    return pll
