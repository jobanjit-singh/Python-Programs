import sys
a = 0
b= 1
try:
    print(d)
    c=b/a
except NameError:
    print("oops!",sys.exc_info()[0],"is occurred")
except:
    print("oops!",sys.exc_info()[0],"is occurred")
finally:
    print("bye byee")