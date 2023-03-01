from math import ceil

def RoundUP(n, decimals=0):
    multiplier = 10 ** decimals
    return ceil(n * multiplier) / multiplier