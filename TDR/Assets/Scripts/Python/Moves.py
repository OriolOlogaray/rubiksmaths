up = {}
right = {}
front = {}
down = {}
left = {}
back = {}
up2 = {}
right2 = {}
front2 = {}
down2 = {}
left2 = {}
back2 = {}
cube_scheme = [up, right, front, down, left, back]
cube_scheme2 = [up2, right2, front2, down2, left2, back2]
letters = ["u", "r", "f", "d", "l", "b"]
k = 0
h = 0
for face in cube_scheme:
    for i in range(1, 10):
        face[letters[k] + str(i)] = letters[k].upper() + str(i)
    k += 1
for face2 in cube_scheme2:
    for i in range(1, 10):
        face2[letters[h] + str(i)] = letters[h].upper() + str(i)
    h += 1


def u(up, right, front, left, back):
    """Updates stickers' position after rotating the upper face 90º clockwise"""
    up2["u1"] = up["u7"]
    up2["u2"] = up["u4"]
    up2["u3"] = up["u1"]
    up2["u4"] = up["u8"]
    up2["u6"] = up["u2"]
    up2["u7"] = up["u9"]
    up2["u8"] = up["u6"]
    up2["u9"] = up["u3"]
    right2["r1"] = back["b1"]
    right2["r2"] = back["b2"]
    right2["r3"] = back["b3"]
    front2["f1"] = right["r1"]
    front2["f2"] = right["r2"]
    front2["f3"] = right["r3"]
    left2["l1"] = front["f1"]
    left2["l2"] = front["f2"]
    left2["l3"] = front["f3"]
    back2["b1"] = left["l1"]
    back2["b2"] = left["l2"]
    back2["b3"] = left["l3"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    back.update(back2)


def uprime(up, right, front, left, back):
    """Updates stickers' position after rotating the upper face 90º anticlockwise"""
    up2["u7"] = up["u1"]
    up2["u4"] = up["u2"]
    up2["u1"] = up["u3"]
    up2["u8"] = up["u4"]
    up2["u2"] = up["u6"]
    up2["u9"] = up["u7"]
    up2["u6"] = up["u8"]
    up2["u3"] = up["u9"]
    back2["b1"] = right["r1"]
    back2["b2"] = right["r2"]
    back2["b3"] = right["r3"]
    right2["r1"] = front["f1"]
    right2["r2"] = front["f2"]
    right2["r3"] = front["f3"]
    front2["f1"] = left["l1"]
    front2["f2"] = left["l2"]
    front2["f3"] = left["l3"]
    left2["l1"] = back["b1"]
    left2["l2"] = back["b2"]
    left2["l3"] = back["b3"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    back.update(back2)


def r(up, right, front, down, back):
    """Updates stickers' position after rotating the right face 90º clockwise"""
    right2["r1"] = right["r7"]
    right2["r2"] = right["r4"]
    right2["r3"] = right["r1"]
    right2["r4"] = right["r8"]
    right2["r6"] = right["r2"]
    right2["r7"] = right["r9"]
    right2["r8"] = right["r6"]
    right2["r9"] = right["r3"]
    up2["u3"] = front["f3"]
    up2["u6"] = front["f6"]
    up2["u9"] = front["f9"]
    front2["f3"] = down["d3"]
    front2["f6"] = down["d6"]
    front2["f9"] = down["d9"]
    down2["d3"] = back["b7"]
    down2["d6"] = back["b4"]
    down2["d9"] = back["b1"]
    back2["b7"] = up["u3"]
    back2["b4"] = up["u6"]
    back2["b1"] = up["u9"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    back.update(back2)


def rprime(up, right, front, down, back):
    """Updates stickers' position after rotating the right face 90º anticlockwise"""
    right2["r7"] = right["r1"]
    right2["r4"] = right["r2"]
    right2["r1"] = right["r3"]
    right2["r8"] = right["r4"]
    right2["r2"] = right["r6"]
    right2["r9"] = right["r7"]
    right2["r6"] = right["r8"]
    right2["r3"] = right["r9"]
    front2["f3"] = up["u3"]
    front2["f6"] = up["u6"]
    front2["f9"] = up["u9"]
    down2["d3"] = front["f3"]
    down2["d6"] = front["f6"]
    down2["d9"] = front["f9"]
    back2["b7"] = down["d3"]
    back2["b4"] = down["d6"]
    back2["b1"] = down["d9"]
    up2["u3"] = back["b7"]
    up2["u6"] = back["b4"]
    up2["u9"] = back["b1"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    back.update(back2)


def f(up, right, front, down, left):
    """Updates stickers' position after rotating the front face 90º clockwise"""
    front2["f1"] = front["f7"]
    front2["f2"] = front["f4"]
    front2["f3"] = front["f1"]
    front2["f4"] = front["f8"]
    front2["f6"] = front["f2"]
    front2["f7"] = front["f9"]
    front2["f8"] = front["f6"]
    front2["f9"] = front["f3"]
    right2["r1"] = up["u7"]
    right2["r4"] = up["u8"]
    right2["r7"] = up["u9"]
    down2["d3"] = right["r1"]
    down2["d2"] = right["r4"]
    down2["d1"] = right["r7"]
    left2["l3"] = down["d1"]
    left2["l6"] = down["d2"]
    left2["l9"] = down["d3"]
    up2["u9"] = left["l3"]
    up2["u8"] = left["l6"]
    up2["u7"] = left["l9"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    down.update(down2)


def fprime(up, right, front, down, left):
    """Updates stickers' position after rotating the upper face 90º anticlockwise"""
    front2["f7"] = front["f1"]
    front2["f4"] = front["f2"]
    front2["f1"] = front["f3"]
    front2["f8"] = front["f4"]
    front2["f2"] = front["f6"]
    front2["f9"] = front["f7"]
    front2["f6"] = front["f8"]
    front2["f3"] = front["f9"]
    up2["u7"] = right["r1"]
    up2["u8"] = right["r4"]
    up2["u9"] = right["r7"]
    right2["r1"] = down["d3"]
    right2["r4"] = down["d2"]
    right2["r7"] = down["d1"]
    down2["d1"] = left["l3"]
    down2["d2"] = left["l6"]
    down2["d3"] = left["l9"]
    left2["l3"] = up["u9"]
    left2["l6"] = up["u8"]
    left2["l9"] = up["u7"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    down.update(down2)


def d(right, front, down, left, back):
    """Updates stickers' position after rotating the lower face 90º clockwise"""
    down2["d1"] = down["d7"]
    down2["d2"] = down["d4"]
    down2["d3"] = down["d1"]
    down2["d4"] = down["d8"]
    down2["d6"] = down["d2"]
    down2["d7"] = down["d9"]
    down2["d8"] = down["d6"]
    down2["d9"] = down["d3"]
    right2["r7"] = front["f7"]
    right2["r8"] = front["f8"]
    right2["r9"] = front["f9"]
    front2["f7"] = left["l7"]
    front2["f8"] = left["l8"]
    front2["f9"] = left["l9"]
    left2["l7"] = back["b7"]
    left2["l8"] = back["b8"]
    left2["l9"] = back["b9"]
    back2["b7"] = right["r7"]
    back2["b8"] = right["r8"]
    back2["b9"] = right["r9"]
    down.update(down2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    back.update(back2)


def dprime(right, front, down, left, back):
    """Updates stickers' position after rotating the lower face 90º anticlockwise"""
    down2["d7"] = down["d1"]
    down2["d4"] = down["d2"]
    down2["d1"] = down["d3"]
    down2["d8"] = down["d4"]
    down2["d2"] = down["d6"]
    down2["d9"] = down["d7"]
    down2["d6"] = down["d8"]
    down2["d3"] = down["d9"]
    front2["f7"] = right["r7"]
    front2["f8"] = right["r8"]
    front2["f9"] = right["r9"]
    left2["l7"] = front["f7"]
    left2["l8"] = front["f8"]
    left2["l9"] = front["f9"]
    back2["b7"] = left["l7"]
    back2["b8"] = left["l8"]
    back2["b9"] = left["l9"]
    right2["r7"] = back["b7"]
    right2["r8"] = back["b8"]
    right2["r9"] = back["b9"]
    down.update(down2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    back.update(back2)


def l(up, front, down, left, back):
    """Updates stickers' position after rotating the left face 90º clockwise"""
    left2["l1"] = left["l7"]
    left2["l2"] = left["l4"]
    left2["l3"] = left["l1"]
    left2["l4"] = left["l8"]
    left2["l6"] = left["l2"]
    left2["l7"] = left["l9"]
    left2["l8"] = left["l6"]
    left2["l9"] = left["l3"]
    front2["f1"] = up["u1"]
    front2["f4"] = up["u4"]
    front2["f7"] = up["u7"]
    down2["d1"] = front["f1"]
    down2["d4"] = front["f4"]
    down2["d7"] = front["f7"]
    back2["b9"] = down["d1"]
    back2["b6"] = down["d4"]
    back2["b3"] = down["d7"]
    up2["u1"] = back["b9"]
    up2["u4"] = back["b6"]
    up2["u7"] = back["b3"]
    up.update(up2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def lprime(up, front, down, left, back):
    """Updates stickers' position after rotating the left face 90º anticlockwise"""
    left2["l7"] = left["l1"]
    left2["l4"] = left["l2"]
    left2["l1"] = left["l3"]
    left2["l8"] = left["l4"]
    left2["l2"] = left["l6"]
    left2["l9"] = left["l7"]
    left2["l6"] = left["l8"]
    left2["l3"] = left["l9"]
    up2["u1"] = front["f1"]
    up2["u4"] = front["f4"]
    up2["u7"] = front["f7"]
    front2["f1"] = down["d1"]
    front2["f4"] = down["d4"]
    front2["f7"] = down["d7"]
    down2["d1"] = back["b9"]
    down2["d4"] = back["b6"]
    down2["d7"] = back["b3"]
    back2["b9"] = up["u1"]
    back2["b6"] = up["u4"]
    back2["b3"] = up["u7"]
    up.update(up2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def b(up, right, down, left, back):
    """Updates stickers' position after rotating the back face 90º clockwise"""
    back2["b1"] = back["b7"]
    back2["b2"] = back["b4"]
    back2["b3"] = back["b1"]
    back2["b4"] = back["b8"]
    back2["b6"] = back["b2"]
    back2["b7"] = back["b9"]
    back2["b8"] = back["b6"]
    back2["b9"] = back["b3"]
    up2["u1"] = right["r3"]
    up2["u2"] = right["r6"]
    up2["u3"] = right["r9"]
    right2["r3"] = down["d9"]
    right2["r6"] = down["d8"]
    right2["r9"] = down["d7"]
    down2["d7"] = left["l1"]
    down2["d8"] = left["l4"]
    down2["d9"] = left["l7"]
    left2["l1"] = up["u3"]
    left2["l4"] = up["u2"]
    left2["l7"] = up["u1"]
    up.update(up2)
    right.update(right2)
    left.update(left2)
    down.update(down2)
    back.update(back2)


def bprime(up, right, down, left, back):
    """Updates stickers' position after rotating the back face 90º anticlockwise"""
    back2["b7"] = back["b1"]
    back2["b4"] = back["b2"]
    back2["b1"] = back["b3"]
    back2["b8"] = back["b4"]
    back2["b2"] = back["b6"]
    back2["b9"] = back["b7"]
    back2["b6"] = back["b8"]
    back2["b3"] = back["b9"]
    right2["r3"] = up["u1"]
    right2["r6"] = up["u2"]
    right2["r9"] = up["u3"]
    down2["d9"] = right["r3"]
    down2["d8"] = right["r6"]
    down2["d7"] = right["r9"]
    left2["l1"] = down["d7"]
    left2["l4"] = down["d8"]
    left2["l7"] = down["d9"]
    up2["u1"] = left["l7"]
    up2["u2"] = left["l4"]
    up2["u3"] = left["l1"]
    up.update(up2)
    right.update(right2)
    left.update(left2)
    down.update(down2)
    back.update(back2)


def m(up, front, down, back):
    """Updates stickers' position after rotating the middle layer (between right and left layers) 90º clockwise"""
    up2["u2"] = back["b8"]
    up2["u5"] = back["b5"]
    up2["u8"] = back["b2"]
    front2["f2"] = up["u2"]
    front2["f5"] = up["u5"]
    front2["f8"] = up["u8"]
    down2["d2"] = front["f2"]
    down2["d5"] = front["f5"]
    down2["d8"] = front["f8"]
    back2["b2"] = down["d8"]
    back2["b5"] = down["d5"]
    back2["b8"] = down["d2"]
    up.update(up2)
    front.update(front2)
    down.update(down2)
    back.update(back2)


def mprime(up, front, down, back):
    """Updates stickers' position after rotating the middle layer (between right and left layers) 90º anticlockwise"""
    up2["u2"] = front["f2"]
    up2["u5"] = front["f5"]
    up2["u8"] = front["f8"]
    front2["f2"] = down["d2"]
    front2["f5"] = down["d5"]
    front2["f8"] = down["d8"]
    down2["d2"] = back["b8"]
    down2["d5"] = back["b5"]
    down2["d8"] = back["b2"]
    back2["b2"] = up["u8"]
    back2["b5"] = up["u5"]
    back2["b8"] = up["u2"]
    up.update(up2)
    front.update(front2)
    down.update(down2)
    back.update(back2)


def x(up, right, front, down, left, back):
    """Updates stickers' position after rotating the cube (like an R move) 90º clockwise"""
    right2["r1"] = right["r7"]
    right2["r2"] = right["r4"]
    right2["r3"] = right["r1"]
    right2["r4"] = right["r8"]
    right2["r6"] = right["r2"]
    right2["r7"] = right["r9"]
    right2["r8"] = right["r6"]
    right2["r9"] = right["r3"]
    up2["u3"] = front["f3"]
    up2["u6"] = front["f6"]
    up2["u9"] = front["f9"]
    front2["f3"] = down["d3"]
    front2["f6"] = down["d6"]
    front2["f9"] = down["d9"]
    down2["d3"] = back["b7"]
    down2["d6"] = back["b4"]
    down2["d9"] = back["b1"]
    back2["b7"] = up["u3"]
    back2["b4"] = up["u6"]
    back2["b1"] = up["u9"]
    left2["l7"] = left["l1"]
    left2["l4"] = left["l2"]
    left2["l1"] = left["l3"]
    left2["l8"] = left["l4"]
    left2["l2"] = left["l6"]
    left2["l9"] = left["l7"]
    left2["l6"] = left["l8"]
    left2["l3"] = left["l9"]
    up2["u1"] = front["f1"]
    up2["u4"] = front["f4"]
    up2["u7"] = front["f7"]
    front2["f1"] = down["d1"]
    front2["f4"] = down["d4"]
    front2["f7"] = down["d7"]
    down2["d1"] = back["b9"]
    down2["d4"] = back["b6"]
    down2["d7"] = back["b3"]
    back2["b9"] = up["u1"]
    back2["b6"] = up["u4"]
    back2["b3"] = up["u7"]
    up2["u2"] = front["f2"]
    up2["u5"] = front["f5"]
    up2["u8"] = front["f8"]
    front2["f2"] = down["d2"]
    front2["f5"] = down["d5"]
    front2["f8"] = down["d8"]
    down2["d2"] = back["b8"]
    down2["d5"] = back["b5"]
    down2["d8"] = back["b2"]
    back2["b2"] = up["u8"]
    back2["b5"] = up["u5"]
    back2["b8"] = up["u2"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def xprime(up, right, front, down, left, back):
    """Updates stickers' position after rotating the cube (like an R' move) 90º anticlockwise"""
    right2["r7"] = right["r1"]
    right2["r4"] = right["r2"]
    right2["r1"] = right["r3"]
    right2["r8"] = right["r4"]
    right2["r2"] = right["r6"]
    right2["r9"] = right["r7"]
    right2["r6"] = right["r8"]
    right2["r3"] = right["r9"]
    front2["f3"] = up["u3"]
    front2["f6"] = up["u6"]
    front2["f9"] = up["u9"]
    down2["d3"] = front["f3"]
    down2["d6"] = front["f6"]
    down2["d9"] = front["f9"]
    back2["b7"] = down["d3"]
    back2["b4"] = down["d6"]
    back2["b1"] = down["d9"]
    up2["u3"] = back["b7"]
    up2["u6"] = back["b4"]
    up2["u9"] = back["b1"]
    left2["l1"] = left["l7"]
    left2["l2"] = left["l4"]
    left2["l3"] = left["l1"]
    left2["l4"] = left["l8"]
    left2["l6"] = left["l2"]
    left2["l7"] = left["l9"]
    left2["l8"] = left["l6"]
    left2["l9"] = left["l3"]
    front2["f1"] = up["u1"]
    front2["f4"] = up["u4"]
    front2["f7"] = up["u7"]
    down2["d1"] = front["f1"]
    down2["d4"] = front["f4"]
    down2["d7"] = front["f7"]
    back2["b9"] = down["d1"]
    back2["b6"] = down["d4"]
    back2["b3"] = down["d7"]
    up2["u1"] = back["b9"]
    up2["u4"] = back["b6"]
    up2["u7"] = back["b3"]
    up2["u2"] = back["b8"]
    up2["u5"] = back["b5"]
    up2["u8"] = back["b2"]
    front2["f2"] = up["u2"]
    front2["f5"] = up["u5"]
    front2["f8"] = up["u8"]
    down2["d2"] = front["f2"]
    down2["d5"] = front["f5"]
    down2["d8"] = front["f8"]
    back2["b2"] = down["d8"]
    back2["b5"] = down["d5"]
    back2["b8"] = down["d2"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def y(up, right, front, down, left, back):
    """Updates stickers' position after rotating the cube (like a U move) 90º clockwise"""
    up2["u1"] = up["u7"]
    up2["u2"] = up["u4"]
    up2["u3"] = up["u1"]
    up2["u4"] = up["u8"]
    up2["u6"] = up["u2"]
    up2["u7"] = up["u9"]
    up2["u8"] = up["u6"]
    up2["u9"] = up["u3"]
    right2["r1"] = back["b1"]
    right2["r2"] = back["b2"]
    right2["r3"] = back["b3"]
    front2["f1"] = right["r1"]
    front2["f2"] = right["r2"]
    front2["f3"] = right["r3"]
    left2["l1"] = front["f1"]
    left2["l2"] = front["f2"]
    left2["l3"] = front["f3"]
    back2["b1"] = left["l1"]
    back2["b2"] = left["l2"]
    back2["b3"] = left["l3"]
    down2["d7"] = down["d1"]
    down2["d4"] = down["d2"]
    down2["d1"] = down["d3"]
    down2["d8"] = down["d4"]
    down2["d2"] = down["d6"]
    down2["d9"] = down["d7"]
    down2["d6"] = down["d8"]
    down2["d3"] = down["d9"]
    front2["f7"] = right["r7"]
    front2["f8"] = right["r8"]
    front2["f9"] = right["r9"]
    left2["l7"] = front["f7"]
    left2["l8"] = front["f8"]
    left2["l9"] = front["f9"]
    back2["b7"] = left["l7"]
    back2["b8"] = left["l8"]
    back2["b9"] = left["l9"]
    right2["r7"] = back["b7"]
    right2["r8"] = back["b8"]
    right2["r9"] = back["b9"]
    front2["f4"] = right["r4"]
    front2["f5"] = right["r5"]
    front2["f6"] = right["r6"]
    right2["r4"] = back["b4"]
    right2["r5"] = back["b5"]
    right2["r6"] = back["b6"]
    back2["b4"] = left["l4"]
    back2["b5"] = left["l5"]
    back2["b6"] = left["l6"]
    left2["l4"] = front["f4"]
    left2["l5"] = front["f5"]
    left2["l6"] = front["f6"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def yprime(up, right, front, down, left, back):
    """Updates stickers' position after rotating the cube (like a U' move) 90º anticlockwise"""
    up2["u7"] = up["u1"]
    up2["u4"] = up["u2"]
    up2["u1"] = up["u3"]
    up2["u8"] = up["u4"]
    up2["u2"] = up["u6"]
    up2["u9"] = up["u7"]
    up2["u6"] = up["u8"]
    up2["u3"] = up["u9"]
    back2["b1"] = right["r1"]
    back2["b2"] = right["r2"]
    back2["b3"] = right["r3"]
    right2["r1"] = front["f1"]
    right2["r2"] = front["f2"]
    right2["r3"] = front["f3"]
    front2["f1"] = left["l1"]
    front2["f2"] = left["l2"]
    front2["f3"] = left["l3"]
    left2["l1"] = back["b1"]
    left2["l2"] = back["b2"]
    left2["l3"] = back["b3"]
    down2["d1"] = down["d7"]
    down2["d2"] = down["d4"]
    down2["d3"] = down["d1"]
    down2["d4"] = down["d8"]
    down2["d6"] = down["d2"]
    down2["d7"] = down["d9"]
    down2["d8"] = down["d6"]
    down2["d9"] = down["d3"]
    right2["r7"] = front["f7"]
    right2["r8"] = front["f8"]
    right2["r9"] = front["f9"]
    front2["f7"] = left["l7"]
    front2["f8"] = left["l8"]
    front2["f9"] = left["l9"]
    left2["l7"] = back["b7"]
    left2["l8"] = back["b8"]
    left2["l9"] = back["b9"]
    back2["b7"] = right["r7"]
    back2["b8"] = right["r8"]
    back2["b9"] = right["r9"]
    front2["f4"] = left["l4"]
    front2["f5"] = left["l5"]
    front2["f6"] = left["l6"]
    right2["r4"] = front["f4"]
    right2["r5"] = front["f5"]
    right2["r6"] = front["f6"]
    back2["b4"] = right["r4"]
    back2["b5"] = right["r5"]
    back2["b6"] = right["r6"]
    left2["l4"] = back["b4"]
    left2["l5"] = back["b5"]
    left2["l6"] = back["b6"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def lowerd(right, front, down, left, back):
    """Updates stickers' position after rotating the two lower layers of the cube 90º clockwise"""
    front2["f4"] = left["l4"]
    front2["f5"] = left["l5"]
    front2["f6"] = left["l6"]
    right2["r4"] = front["f4"]
    right2["r5"] = front["f5"]
    right2["r6"] = front["f6"]
    back2["b4"] = right["r4"]
    back2["b5"] = right["r5"]
    back2["b6"] = right["r6"]
    left2["l4"] = back["b4"]
    left2["l5"] = back["b5"]
    left2["l6"] = back["b6"]
    down2["d1"] = down["d7"]
    down2["d2"] = down["d4"]
    down2["d3"] = down["d1"]
    down2["d4"] = down["d8"]
    down2["d6"] = down["d2"]
    down2["d7"] = down["d9"]
    down2["d8"] = down["d6"]
    down2["d9"] = down["d3"]
    right2["r7"] = front["f7"]
    right2["r8"] = front["f8"]
    right2["r9"] = front["f9"]
    front2["f7"] = left["l7"]
    front2["f8"] = left["l8"]
    front2["f9"] = left["l9"]
    left2["l7"] = back["b7"]
    left2["l8"] = back["b8"]
    left2["l9"] = back["b9"]
    back2["b7"] = right["r7"]
    back2["b8"] = right["r8"]
    back2["b9"] = right["r9"]
    right.update(right2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def lowerdprime(right, front, down, left, back):
    """Updates stickers' position after rotating the two lower layers of the cube 90º anticlockwise"""
    down2["d7"] = down["d1"]
    down2["d4"] = down["d2"]
    down2["d1"] = down["d3"]
    down2["d8"] = down["d4"]
    down2["d2"] = down["d6"]
    down2["d9"] = down["d7"]
    down2["d6"] = down["d8"]
    down2["d3"] = down["d9"]
    front2["f7"] = right["r7"]
    front2["f8"] = right["r8"]
    front2["f9"] = right["r9"]
    left2["l7"] = front["f7"]
    left2["l8"] = front["f8"]
    left2["l9"] = front["f9"]
    back2["b7"] = left["l7"]
    back2["b8"] = left["l8"]
    back2["b9"] = left["l9"]
    right2["r7"] = back["b7"]
    right2["r8"] = back["b8"]
    right2["r9"] = back["b9"]
    front2["f4"] = right["r4"]
    front2["f5"] = right["r5"]
    front2["f6"] = right["r6"]
    right2["r4"] = back["b4"]
    right2["r5"] = back["b5"]
    right2["r6"] = back["b6"]
    back2["b4"] = left["l4"]
    back2["b5"] = left["l5"]
    back2["b6"] = left["l6"]
    left2["l4"] = front["f4"]
    left2["l5"] = front["f5"]
    left2["l6"] = front["f6"]
    right.update(right2)
    front.update(front2)
    down.update(down2)
    left.update(left2)
    back.update(back2)


def lowerf(up, right, front, down, left):
    """Updates stickers' position after rotating the two front layers of the cube 90º clockwise"""
    front2["f1"] = front["f7"]
    front2["f2"] = front["f4"]
    front2["f3"] = front["f1"]
    front2["f4"] = front["f8"]
    front2["f6"] = front["f2"]
    front2["f7"] = front["f9"]
    front2["f8"] = front["f6"]
    front2["f9"] = front["f3"]
    right2["r1"] = up["u7"]
    right2["r4"] = up["u8"]
    right2["r7"] = up["u9"]
    down2["d3"] = right["r1"]
    down2["d2"] = right["r4"]
    down2["d1"] = right["r7"]
    left2["l3"] = down["d1"]
    left2["l6"] = down["d2"]
    left2["l9"] = down["d3"]
    up2["u9"] = left["l3"]
    up2["u8"] = left["l6"]
    up2["u7"] = left["l9"]
    up2["u4"] = left["l8"]
    up2["u5"] = left["l5"]
    up2["u6"] = left["l2"]
    right2["r2"] = up["u4"]
    right2["r5"] = up["u5"]
    right2["r8"] = up["u6"]
    down2["d6"] = right["r2"]
    down2["d5"] = right["r5"]
    down2["d4"] = right["r8"]
    left2["l2"] = down["d4"]
    left2["l5"] = down["d5"]
    left2["l8"] = down["d6"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    down.update(down2)


def lowerfprime(up, right, front, down, left):
    """Updates stickers' position after rotating the two front layers of the cube 90º anticlockwise"""
    front2["f7"] = front["f1"]
    front2["f4"] = front["f2"]
    front2["f1"] = front["f3"]
    front2["f8"] = front["f4"]
    front2["f2"] = front["f6"]
    front2["f9"] = front["f7"]
    front2["f6"] = front["f8"]
    front2["f3"] = front["f9"]
    up2["u7"] = right["r1"]
    up2["u8"] = right["r4"]
    up2["u9"] = right["r7"]
    right2["r1"] = down["d3"]
    right2["r4"] = down["d2"]
    right2["r7"] = down["d1"]
    down2["d1"] = left["l3"]
    down2["d2"] = left["l6"]
    down2["d3"] = left["l9"]
    left2["l3"] = up["u9"]
    left2["l6"] = up["u8"]
    left2["l9"] = up["u7"]
    up2["u4"] = right["r2"]
    up2["u5"] = right["r5"]
    up2["u6"] = right["r8"]
    right2["r2"] = down["d6"]
    right2["r5"] = down["d5"]
    right2["r8"] = down["d4"]
    down2["d4"] = left["l2"]
    down2["d5"] = left["l5"]
    down2["d6"] = left["l8"]
    left2["l2"] = up["u6"]
    left2["l5"] = up["u5"]
    left2["l8"] = up["u4"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    down.update(down2)


def lowerr(up, right, front, down, back):
    """Updates stickers' position after rotating the two right layers of the cube 90º clockwise"""
    right2["r1"] = right["r7"]
    right2["r2"] = right["r4"]
    right2["r3"] = right["r1"]
    right2["r4"] = right["r8"]
    right2["r6"] = right["r2"]
    right2["r7"] = right["r9"]
    right2["r8"] = right["r6"]
    right2["r9"] = right["r3"]
    up2["u3"] = front["f3"]
    up2["u6"] = front["f6"]
    up2["u9"] = front["f9"]
    front2["f3"] = down["d3"]
    front2["f6"] = down["d6"]
    front2["f9"] = down["d9"]
    down2["d3"] = back["b7"]
    down2["d6"] = back["b4"]
    down2["d9"] = back["b1"]
    back2["b7"] = up["u3"]
    back2["b4"] = up["u6"]
    back2["b1"] = up["u9"]
    up2["u2"] = front["f2"]
    up2["u5"] = front["f5"]
    up2["u8"] = front["f8"]
    front2["f2"] = down["d2"]
    front2["f5"] = down["d5"]
    front2["f8"] = down["d8"]
    down2["d2"] = back["b8"]
    down2["d5"] = back["b5"]
    down2["d8"] = back["b2"]
    back2["b2"] = up["u8"]
    back2["b5"] = up["u5"]
    back2["b8"] = up["u2"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    back.update(back2)


def lowerrprime(up, right, front, down, back):
    """Updates stickers' position after rotating the two right layers of the cube 90º anticlockwise"""
    right2["r7"] = right["r1"]
    right2["r4"] = right["r2"]
    right2["r1"] = right["r3"]
    right2["r8"] = right["r4"]
    right2["r2"] = right["r6"]
    right2["r9"] = right["r7"]
    right2["r6"] = right["r8"]
    right2["r3"] = right["r9"]
    front2["f3"] = up["u3"]
    front2["f6"] = up["u6"]
    front2["f9"] = up["u9"]
    down2["d3"] = front["f3"]
    down2["d6"] = front["f6"]
    down2["d9"] = front["f9"]
    back2["b7"] = down["d3"]
    back2["b4"] = down["d6"]
    back2["b1"] = down["d9"]
    up2["u3"] = back["b7"]
    up2["u6"] = back["b4"]
    up2["u9"] = back["b1"]
    up2["u2"] = back["b8"]
    up2["u5"] = back["b5"]
    up2["u8"] = back["b2"]
    front2["f2"] = up["u2"]
    front2["f5"] = up["u5"]
    front2["f8"] = up["u8"]
    down2["d2"] = front["f2"]
    down2["d5"] = front["f5"]
    down2["d8"] = front["f8"]
    back2["b2"] = down["d8"]
    back2["b5"] = down["d5"]
    back2["b8"] = down["d2"]
    up.update(up2)
    front.update(front2)
    down.update(down2)
    back.update(back2)
    up.update(up2)
    right.update(right2)
    front.update(front2)
    down.update(down2)
    back.update(back2)


def loweru(up, right, front, left, back):
    """Updates stickers' position after rotating the two upper layers of the cube 90º clockwise"""
    up2["u1"] = up["u7"]
    up2["u2"] = up["u4"]
    up2["u3"] = up["u1"]
    up2["u4"] = up["u8"]
    up2["u6"] = up["u2"]
    up2["u7"] = up["u9"]
    up2["u8"] = up["u6"]
    up2["u9"] = up["u3"]
    right2["r1"] = back["b1"]
    right2["r2"] = back["b2"]
    right2["r3"] = back["b3"]
    front2["f1"] = right["r1"]
    front2["f2"] = right["r2"]
    front2["f3"] = right["r3"]
    left2["l1"] = front["f1"]
    left2["l2"] = front["f2"]
    left2["l3"] = front["f3"]
    back2["b1"] = left["l1"]
    back2["b2"] = left["l2"]
    back2["b3"] = left["l3"]
    front2["f4"] = right["r4"]
    front2["f5"] = right["r5"]
    front2["f6"] = right["r6"]
    right2["r4"] = back["b4"]
    right2["r5"] = back["b5"]
    right2["r6"] = back["b6"]
    back2["b4"] = left["l4"]
    back2["b5"] = left["l5"]
    back2["b6"] = left["l6"]
    left2["l4"] = front["f4"]
    left2["l5"] = front["f5"]
    left2["l6"] = front["f6"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    back.update(back2)


def loweruprime(up, right, front, left, back):
    """Updates stickers' position after rotating the two upper layers of the cube 90º anticlockwise"""
    up2["u7"] = up["u1"]
    up2["u4"] = up["u2"]
    up2["u1"] = up["u3"]
    up2["u8"] = up["u4"]
    up2["u2"] = up["u6"]
    up2["u9"] = up["u7"]
    up2["u6"] = up["u8"]
    up2["u3"] = up["u9"]
    back2["b1"] = right["r1"]
    back2["b2"] = right["r2"]
    back2["b3"] = right["r3"]
    right2["r1"] = front["f1"]
    right2["r2"] = front["f2"]
    right2["r3"] = front["f3"]
    front2["f1"] = left["l1"]
    front2["f2"] = left["l2"]
    front2["f3"] = left["l3"]
    left2["l1"] = back["b1"]
    left2["l2"] = back["b2"]
    left2["l3"] = back["b3"]
    front2["f4"] = left["l4"]
    front2["f5"] = left["l5"]
    front2["f6"] = left["l6"]
    right2["r4"] = front["f4"]
    right2["r5"] = front["f5"]
    right2["r6"] = front["f6"]
    back2["b4"] = right["r4"]
    back2["b5"] = right["r5"]
    back2["b6"] = right["r6"]
    left2["l4"] = back["b4"]
    left2["l5"] = back["b5"]
    left2["l6"] = back["b6"]
    up.update(up2)
    right.update(right2)
    front.update(front2)
    left.update(left2)
    back.update(back2)
