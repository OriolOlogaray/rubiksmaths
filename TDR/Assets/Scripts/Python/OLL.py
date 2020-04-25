from Moves import u, uprime, r, rprime, f, fprime, l, lprime, lowerf, lowerfprime, lowerr, lowerrprime, m, mprime, d
from Moves import dprime, b, bprime


def oll(up, right, front, down, left, back):
    """Return the moves to complete the upper face"""
    formatted_oll = ""
    oll_case = oll_cases(up, right, front, left, back)
    oll_1 = ["000010000111010111010", "000010000010111010111"]
    oll_2 = ["000010000011010110111", "000010000010110111011", "000010000110111011010", "000010000111011010110"]
    oll_3 = ["000010001110111010110", "001010000110010110110", "100010000010110110110", "000010100110110110010"]
    oll_4 = ["001010000010011011011", "100010000011011011010", "000010100011011010011", "000010001011010011011"]
    oll_5 = ["000011011110100000110", "011011000100000110110", "110110000000110110100", "000110110110110100000"]
    oll_6 = ["011011000000001011011", "110110000001011011000", "000110110011011000001", "000011011011000001011"]
    oll_7 = ["010110100100110110000", "000110011110110000100", "001011010110000100110", "110011000000100110110"]
    oll_8 = ["010011001001000011011", "011110000000011011001", "100110010011011001000", "000011110011001000011"]
    oll_9 = ["010110001001010011001", "001110010010011001001", "100011010011001001010", "010011100001001010011"]
    oll_10 = ["001110010110010100100", "100011010010100100110", "010011100100100110010", "010110001100110010100"]
    oll_11 = ["000011110110100100010", "010011001100100010110", "011110000100010110100", "100110010010110100100"]
    oll_12 = ["001011010010001001011", "110011000001001011010", "010110100001011010001", "0001100011011010001001"]
    oll_13 = ["000111100110100110000", "010010011100110000110", "001111000110000110100", "110010010000110100110"]
    oll_14 = ["000111001011000011001", "011010010000011001011", "100111000011001011000", "010010110001011000011"]
    oll_15 = ["000111001110100010100", "011010010100010100110", "100111000010100110100", "010010110100110100010"]
    oll_16 = ["001111000010001011001", "110010010001011001010", "000111100011001010001", "010010011001010001011"]
    oll_17 = ["100010001011010010110", "001010100010010110011", "100010001010110011010", "001010100110011010010"]
    oll_18 = ["101010000010010111010", "100010100010111010010", "000010101111010010010", "001010001010010010111"]
    oll_19 = ["101010000010011010110", "100010100011010110010", "000010101010110010011", "001010001110010011010"]
    oll_20 = ["101010101010010010010"]
    oll_21 = ["010111010101000101000", "010111010000101000101"]
    oll_22 = ["010111010001000100101", "010111010000100101001", "010111010100101001000", "010111010101001000100"]
    oll_23 = ["111111010000000101000", "110111110000101000000", "010111111101000000000", "011111011000000000101"]
    oll_24 = ["011111011100000001000", "111111010000001000100", "110111110001000100000", "010111111000100000001"]
    oll_25 = ["011111110000000100001", "110111011000100001000", "011111110100001000000", "110111011001000000100"]
    oll_26 = ["011111010000001001001", "110111010001001001000", "010111110001001000001", "010111011001000001001"]
    oll_27 = ["010111110100100100000", "010111011100100000100", "011111010100000100100", "110111010000100100100"]
    oll_28 = ["111110101000010010000", "101110111010010000000", "101011111010000000010", "111011101000000010010"]
    oll_29 = ["101110010010011000100", "100011110011000100010", "010011101000100010011", "011110001100010011000"]
    oll_30 = ["101011010010001000110", "110011100001000110010", "010110101000110010001", "001110011110010001000"]
    oll_31 = ["011011001100000011010", "111110000000011010100", "100110110011010100000", "000011111010100000011"]
    oll_32 = ["001011011110000001010", "111011000000001010110", "110110100001010110000", "000110111010110000001"]
    oll_33 = ["001111001110000011000", "111010010000011000110", "100111100011000110000", "010010111000110000011"]
    oll_34 = ["000111101010100010001", "011010011100010001010", "101111000010001010100", "110010110001010100010"]
    oll_35 = ["100011011010100001010", "011011100100001010010", "110110001001010010100", "001110110010010100001"]
    oll_36 = ["110011001001000010110", "011110100000010110001", "100110011010110001000", "001011110110001000010"]
    oll_37 = ["110110001000110011000", "001110110110011000000", "100011011011000100110", "011011100000000110011"]
    oll_38 = ["011110100100011010000", "100110011011010000100", "001011110010000100011", "110011001000100011010"]
    oll_39 = ["001111100110001010000", "110010011001010000110", "001111100010000110001", "110010011000110001010"]
    oll_40 = ["100111001011000010100", "011010110000010100011", "100111001010100011000", "011010110100011000010"]
    oll_41 = ["010110101101010010000", "001110011010010000101", "101011010010000101010", "110011100000101010010"]
    oll_42 = ["101110010010010101000", "100011110010101000010", "010011101101000010010", "011110001000010010101"]
    oll_43 = ["100110110010111000000", "000011111111000000010", "011011001000000010111", "111110000000010111000"]
    oll_44 = ["001011011010000000111", "111011000000000111010", "110110100000111010000", "000110111111010000000"]
    oll_45 = ["001111001010000010101", "111010010000010101010", "100111100010101010000", "010010111101010000010"]
    oll_46 = ["110010110000111000010", "000111101111000010000", "011010011000010000111", "101111000010000111000"]
    oll_47 = ["010011000100101011010", "010110000101011010100", "000110010011010100101", "000011010010100101011"]
    oll_48 = ["010110000001010110101", "000110010010110101001", "000011010110101001010", "010011000101001010110"]
    oll_49 = ["010011000001000110111", "010110000000110111001", "000110010110111001000", "000011010111001000110"]
    oll_50 = ["000011010011000100111", "010011000000100111011", "010110000100111011000", "000110010111011000100"]
    oll_51 = ["000111000011000110101", "010010010000110101011", "000111000110101011000", "010010010101011000110"]
    oll_52 = ["010010010100111001010", "000111000111001010100", "010010010001010100111", "000111000010100111001"]
    oll_53 = ["000011010010101000111", "010011000101000111010", "010110000000111010101", "000110010111010101000"]
    oll_54 = ["010011000000101010111", "010110000101010111000", "000110010010111000101", "000011010111000101010"]
    oll_55 = ["010010010000111000111", "000111000111000111000"]
    oll_56 = ["000111000010101010101", "010010010101010101010"]
    oll_57 = ["101111101010000010000", "111010111000010000010"]
    if oll_case in oll_1:
        if oll_case == oll_1[0]:
            formatted_oll += "R U2 R2 F R F' U2 R' F R F' "
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
        if oll_case == oll_1[1]:
            formatted_oll += "U R U2 R2 F R F' U2 R' F R F' "
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            r(up, right, front, down, back)
            r(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
            u(up, right, front, left, back)
            u(up, right, front, left, back)
            rprime(up, right, front, down, back)
            f(up, right, front, down, left)
            r(up, right, front, down, back)
            fprime(up, right, front, down, left)
    if oll_case in oll_2:
        if oll_case in oll_2[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_2[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_2[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F R U R' U' F' f R U R' U' f' "
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
        lowerf(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerfprime(up, right, front, down, left)
    if oll_case in oll_3:
        if oll_case in oll_3[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_3[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_3[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "f R U R' U' f' U' F R U R' U' F' "
        lowerf(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerfprime(up, right, front, down, left)
        uprime(up, right, front, left, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_4:
        if oll_case in oll_4[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_4[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_4[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "f R U R' U' f' U F R U R' U' F' "
        lowerf(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerfprime(up, right, front, down, left)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_5:
        if oll_case in oll_5[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_5[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_5[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll = "r' U2 R U R' U r "
        lowerrprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
    if oll_case in oll_6:
        if oll_case in oll_6[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_6[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_6[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U2 R' U' R U' r' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_7:
        if oll_case in oll_7[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_7[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_7[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U R' U R U2 r' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_8:
        if oll_case in oll_8[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_8[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_8[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U2 R' U2 R' F R F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_9:
        if oll_case in oll_9[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_9[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_9[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U' R' F R2 U R' U' F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_10:
        if oll_case in oll_10[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_10[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_10[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U R' F R F' R U2 R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_11:
        if oll_case in oll_11[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_11[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_11[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r' R2 U R' U R U2 R' U M' "
        lowerrprime(up, right, front, down, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        mprime(up, front, down, back)
    if oll_case in oll_12:
        if oll_case in oll_12[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_12[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_12[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F R U R' U' F' U F R U R' U' F' "
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_13:
        if oll_case in oll_13[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_13[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_13[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U' r' U' r U r' F' U F "
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        fprime(up, right, front, down, left)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
    if oll_case in oll_14:
        if oll_case in oll_14[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_14[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_14[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R' F R U R' F' R F U' F' "
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        fprime(up, right, front, down, left)
        r(up, right, front, down, back)
        f(up, right, front, down, left)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_15:
        if oll_case in oll_15[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_15[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_15[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r' U' r R' U' R U r' U r "
        lowerrprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
    if oll_case in oll_16:
        if oll_case in oll_16[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_16[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_16[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U r' R U R' U' r U' r' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_17:
        if oll_case in oll_17[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_17[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_17[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U R' F R F' U2 R' F R F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        fprime(up, right, front, down, left)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_18:
        if oll_case in oll_18[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_18[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_18[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U R' U R U2 r2 U' R U' R' U2 r "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
    if oll_case in oll_19:
        if oll_case in oll_19[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_19[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_19[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "M U R U R' U' M' R' F R F' "
        m(up, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        mprime(up, front, down, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case == oll_20:
        formatted_oll += "M U R U R' U' M2 U R U' r' "
        m(up, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        mprime(up, front, down, back)
        mprime(up, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_21:
        if oll_case == oll_1[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        formatted_oll += "R U2 R' U' R U R' U' R U' R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_22:
        if oll_case in oll_22[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_22[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_22[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U2 R2 U' R2 U' R2 U2 R "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
    if oll_case in oll_23:
        if oll_case in oll_23[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_23[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_23[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R2 D R' U2 R D' R' U2 R' "
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        d(right, front, down, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        dprime(right, front, down, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
    if oll_case in oll_24:
        if oll_case in oll_24[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_24[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_24[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U R' U' r' F R F' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_25:
        if oll_case in oll_25[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_25[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_25[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F' r U R' U' r' F R "
        fprime(up, right, front, down, left)
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
    if oll_case in oll_26:
        if oll_case in oll_26[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_26[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_26[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U2 R' U' R U' R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_27:
        if oll_case in oll_27[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_27[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_27[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U R U2 R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_28:
        if oll_case in oll_28[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_28[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_28[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U R' U' M U R U' R' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        m(up, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_29:
        if oll_case in oll_29[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_29[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_29[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "M U R U R' U' R' F R F' M' "
        m(up, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
        mprime(up, front, down, back)
    if oll_case in oll_30:
        if oll_case in oll_30[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_30[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_30[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "M U' L' U' L U L F' L' F M' "
        m(up, front, down, back)
        uprime(up, right, front, left, back)
        lprime(up,  front, down, left, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        u(up, right, front, left, back)
        l(up, front, down, left, back)
        fprime(up, right, front, down, left)
        lprime(up, front, down, left, back)
        f(up, right, front, down, left)
        mprime(up, front, down, back)
    if oll_case in oll_31:
        if oll_case in oll_31[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_31[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_31[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R' U' F U R U' R' F' R "
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        f(up, right, front, down, left)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        fprime(up, right, front, down, left)
        r(up, right, front, down, back)
    if oll_case in oll_32:
        if oll_case in oll_32[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_32[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_32[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U B' U' R' U R B R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        bprime(up, right, down, left, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        b(up, right, down, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_33:
        if oll_case in oll_33[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_33[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_33[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U' R' F R F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_34:
        if oll_case in oll_34[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_34[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_34[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R2 U' R' F R U R U' F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_35:
        if oll_case in oll_35[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_35[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_35[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U2 R2 F R F' R U2 R' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
    if oll_case in oll_36:
        if oll_case in oll_36[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_36[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_36[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "L' U' L U' L' U L U L F' L' F "
        lprime(up, front, down, left, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        uprime(up, right, front, left, back)
        lprime(up, front, down, left, back)
        u(up, right, front, left, back)
        l(up, front, down, left, back)
        u(up, right, front, left, back)
        l(up, front, down, left, back)
        fprime(up, right, front, down, left)
        lprime(up, front, down, left, back)
        f(up, right, front, down, left)
    if oll_case in oll_37:
        if oll_case in oll_37[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_37[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_37[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F R U' R' U' R U R' F' "
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_38:
        if oll_case in oll_38[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_38[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_38[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U R U' R' U' R' F R F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_39:
        if oll_case in oll_39[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_39[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_39[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "L F' L' U' L U F U' L' "
        l(up, front, down, left, back)
        fprime(up, right, front, down, left)
        lprime(up, front, down, left, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
        uprime(up, right, front, left, back)
        lprime(up, front, down, left, back)
    if oll_case in oll_40:
        if oll_case in oll_40[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_40[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_40[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R' F R U R' U' F' U R "
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
    if oll_case in oll_41:
        if oll_case in oll_41[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_41[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_41[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R U R' U R U2 R' F R U R' U' F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
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
    if oll_case in oll_42:
        if oll_case in oll_42[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_42[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_42[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R' U' R U' R' U2 R F R U R' U' F' "
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_43:
        if oll_case in oll_43[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_43[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_43[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "f' L' U' L U f "
        lowerfprime(up, right, front, down, left)
        lprime(up, front, down, left, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        u(up, right, front, left, back)
        lowerf(up, right, front, down, left)
    if oll_case in oll_44:
        if oll_case in oll_44[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_44[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_44[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "f R U R' U' f' "
        lowerf(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerfprime(up, right, front, down, left)
    if oll_case in oll_45:
        if oll_case in oll_45[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_45[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_45[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F R U R' U' F' "
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_46:
        if oll_case in oll_46[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_46[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_46[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R' U' R' F R F' U R "
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
    if oll_case in oll_47:
        if oll_case in oll_47[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_47[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_47[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F' L' U' L U L' U' L U F "
        fprime(up, right, front, down, left)
        lprime(up, front, down, left, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        u(up, right, front, left, back)
        lprime(up, front, down, left, back)
        uprime(up, right, front, left, back)
        l(up, front, down, left, back)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
    if oll_case in oll_48:
        if oll_case in oll_48[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_48[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_48[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "F R U R' U' R U R' U' F' "
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_49:
        if oll_case in oll_49[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_49[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_49[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U' r2 U r2 U r2 U' r "
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
    if oll_case in oll_50:
        if oll_case in oll_50[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_50[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_50[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r' U r2 U' r2 U' r2 U r' "
        lowerrprime(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerr(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_51:
        if oll_case in oll_51[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_51[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_51[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "f R U R' U' R U R' U' f' "
        lowerf(up, right, front, down, left)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerfprime(up, right, front, down, left)
    if oll_case in oll_52:
        if oll_case in oll_52[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_52[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_52[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "R' U' R U' R' U F' U F R "
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        fprime(up, right, front, down, left)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
    if oll_case in oll_53:
        if oll_case in oll_53[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_53[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_53[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r' U' R U' R' U R U' R' U2 r "
        lowerrprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        lowerr(up, right, front, down, back)
    if oll_case in oll_54:
        if oll_case in oll_54[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        if oll_case in oll_54[2]:
            formatted_oll += "U2 "
            u(up, right, front, left, back)
            u(up, right, front, left, back)
        if oll_case in oll_54[3]:
            formatted_oll += "U' "
            uprime(up, right, front, left, back)
        formatted_oll += "r U R' U R U' R' U R U2 r' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_55:
        if oll_case == oll_55[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        formatted_oll += "R U2 R2 U' R U' R' U2 F R F' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        u(up, right, front, left, back)
        f(up, right, front, down, left)
        r(up, right, front, down, back)
        fprime(up, right, front, down, left)
    if oll_case in oll_56:
        if oll_case == oll_56[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        formatted_oll += "r U r' U R U' R' U R U' R' r U' r' "
        lowerr(up, right, front, down, back)
        u(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        rprime(up, right, front, down, back)
        lowerr(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    if oll_case in oll_57:
        if oll_case == oll_57[1]:
            formatted_oll += "U "
            u(up, right, front, left, back)
        formatted_oll += "R U R' U' M' U R U' r' "
        r(up, right, front, down, back)
        u(up, right, front, left, back)
        rprime(up, right, front, down, back)
        uprime(up, right, front, left, back)
        mprime(up, front, down, back)
        u(up, right, front, left, back)
        r(up, right, front, down, back)
        uprime(up, right, front, left, back)
        lowerrprime(up, right, front, down, back)
    return str(formatted_oll)


def oll_cases(up, right, front, left, back):
    """Determine the OLL case from the stickers in the last layer"""
    oll = ""
    for sticker in up.values():
        if "U" in sticker:
            oll += "1"
        else:
            oll += "0"
    for i in range(0, 3):
        if "U" in list(back.values())[2 - i]:
            oll += "1"
        else:
            oll += "0"
    for i in range(0, 3):
        if "U" in list(right.values())[2 - i]:
            oll += "1"
        else:
            oll += "0"
    for i in range(0, 3):
        if "U" in list(front.values())[2 - i]:
            oll += "1"
        else:
            oll += "0"
    for i in range(0, 3):
        if "U" in list(left.values())[2 - i]:
            oll += "1"
        else:
            oll += "0"
    return oll
