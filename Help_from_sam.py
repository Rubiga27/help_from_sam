def help(num):
    count=1
    point=1
    while (point<num):
        point=point*2
    if point>num:
        point//=2
        b=num-point
        return count+b
    if point==num:
        return count
print(help(int(input())))