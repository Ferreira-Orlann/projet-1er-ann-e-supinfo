from math import ceil

def RoundUP(n, decimals=0):
    multiplier = 10 ** decimals
    return ceil(n * multiplier) / multiplier

def MergeTwoDictionaries(x, y):
    z = x.copy()
    z.update(y)
    return z
    
def LocalRectToGlobalRect(screen, rect, x, y):
    rect.x = ceil(screen.get_width() / x)
    rect.y = ceil(screen.get_width() / y)
    return rect