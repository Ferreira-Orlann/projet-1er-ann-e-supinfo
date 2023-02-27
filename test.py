bar = []

for i in range(1,9*2):
            if (i % 2 == 0):
                bar.append([None]*9)
            else:
                bar.append([None]*(9-1))
            print(i)
                
print(bar)