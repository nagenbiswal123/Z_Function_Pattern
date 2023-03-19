def print_star_space(col=None):
    if col!=None:
        print('*',end=' ')
    else:
        print(' ',end=' ')

def print_row(*col):
    for i in range(5):
        if i in col:
            print_star_space(i)
        else:
            print_star_space()
    print()

print_row(0,1,2,3,4)
print_row(4)
print_row(3)
print_row(2)
print_row(1)
print_row(0)
print_row(0,1,2,3,4)
