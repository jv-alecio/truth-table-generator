def or_(x,y):
    add = x + y
    if add > 0:
        return 1
    else: return 0

def and_(x,y):
    return x * y

def not_(x,y):
    if y == 0:
        return 1
    else: return 0

def xor_(x,y):
    if x + y == 1:
        return 1
    else: return 0