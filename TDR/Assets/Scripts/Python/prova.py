item = "y"
next_item = "y2"
final_f2l = ""
if item[:1] == next_item[:1]:
    print("hey ")
    if len(item) == 1:
        print("what's ")
        print(next_item[:-1])
        if len(next_item) == 1:
            final_f2l += item + "2 "
        if next_item[-1:] == "2":
            print("up")
            final_f2l += item + "' "
    if item[:-1] == "'":
        if next_item[:-1] == "2":
            final_f2l += item[:1] + " "
        if next_item[:-1] == "'":
            final_f2l += item[:1] + "2 "
    if item[:-1] == "2":
        if len(next_item) == 1:
            final_f2l += item + "' "
        if next_item[:-1] == "'":
            final_f2l += item[:1] + " "
print(final_f2l)