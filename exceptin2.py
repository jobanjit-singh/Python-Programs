class error(Exception):
    pass
class tosmall(error):
    pass
a =5
b= 4
try:
    if a<6:
        raise tosmall
except tosmall:
    print("TO small")
finally:
    print("byebye")
