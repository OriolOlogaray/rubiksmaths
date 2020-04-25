import kociemba
from Moves import u, uprime, r, rprime, f, fprime, d, dprime, l, lprime, b, bprime, up, right, front, down, left, back
from Moves import cube_scheme
from Cross import cross
from F2L import f2l
from OLL import oll
from PLL import pll
solution = ""
final_solution = ""
print("Enter a scramble: ")
scramble = input().split()
for move in scramble:
    if move == "U":
        u(up, right, front, left, back)
    if move == "U'":
        uprime(up, right, front, left, back)
    if move == "U2":
        u(up, right, front, left, back)
        u(up, right, front, left, back)
    if move == "R":
        r(up, right, front, down, back)
    if move == "R'":
        rprime(up, right, front, down, back)
    if move == "R2":
        r(up, right, front, down, back)
        r(up, right, front, down, back)
    if move == "F":
        f(up, right, front, down, left)
    if move == "F'":
        fprime(up, right, front, down, left)
    if move == "F2":
        f(up, right, front, down, left)
        f(up, right, front, down, left)
    if move == "D":
        d(right, front, down, left, back)
    if move == "D'":
        dprime(right, front, down, left, back)
    if move == "D2":
        d(right, front, down, left, back)
        d(right, front, down, left, back)
    if move == "L":
        l(up, front, down, left, back)
    if move == "L'":
        lprime(up, front, down, left, back)
    if move == "L2":
        l(up, front, down, left, back)
        l(up, front, down, left, back)
    if move == "B":
        b(up, right, down, left, back)
    if move == "B'":
        bprime(up, right, down, left, back)
    if move == "B2":
        b(up, right, down, left, back)
        b(up, right, down, left, back)
print("If you want the most optimal solution, using Kociemba's algorithm, press 1")
print("If you want the CFOP method solution, press 2")
method = str(input())
if method == "1":
    formatted_cube = ""
    for face in cube_scheme:
        for key in face:
            formatted_cube += str(face[key])[:1]
    solve = str(kociemba.solve(str(formatted_cube)))
    print(solve)

if method == "2":
    solution += cross(up, right, front, down, left, back)
    solution += f2l(up, right, front, down, left, back)
    solution += oll(up, right, front, down, left, back)
    solution += pll(up, right, front, down, left, back)
    if front["f5"][:1] in back["b2"]:
        solution += "U2"
        u(up, right, front, left, back)
        u(up, right, front, left, back)
    if left["l5"][:1] in back["b2"]:
        solution += "U'"
        uprime(up, right, front, left, back)
    if right["r5"][:1] in back["b2"]:
        solution += "U"
        u(up, right, front, left, back)
    i = 0
    solution_list = solution.split()
    while i < len(solution_list) - 1:
        item = solution_list[i]
        next_item = solution_list[i + 1]
        if item[:1] == next_item[:1]:
            if len(item) == 1:
                if len(next_item) == 1:
                    final_solution += item + "2 "
                if next_item[-1:] == "2":
                    final_solution += item + "' "
            if item[-1:] == "'":
                if next_item[-1:] == "2":
                    final_solution += item[:1] + " "
                if next_item[-1:] == "'":
                    final_solution += item[:1] + "2 "
            if item[-1:] == "2":
                if len(next_item) == 1:
                    final_solution += item[:1] + "' "
                if next_item[-1:] == "'":
                    final_solution += item[:1] + " "
            i += 2
        else:
            final_solution += item + " "
            i += 1
    final_solution += solution_list[-1] + " "
    print(final_solution)
    # print(pll(up, right, front, down, left, back))
