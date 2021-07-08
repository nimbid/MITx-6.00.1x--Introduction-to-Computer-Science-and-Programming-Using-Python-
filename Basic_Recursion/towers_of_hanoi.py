def print_move(fr, to):
    print("Move from "+str(fr)+" to "+str(to))

def towers(size, fr, to, spare):
    if size == 1:
        print_move(fr, to)
    else:
        towers(size-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(size-1, spare, to, fr)
print(towers(3, 'P1', 'P2', 'P3'))
