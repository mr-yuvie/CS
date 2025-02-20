# not finished yet, doesn't work as intended.
seed = int(input("Enter seed:"))
for i in range(150):
    seed = seed * seed
    seed = int(str(seed)[len(str(seed)) // 2 - 1 : len(str(seed)) // 2 + 2])
    print(seed, end="")
